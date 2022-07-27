# -*- coding: utf-8 -*-
from lcapy import Circuit
from sympy.printing.c import ccode
from os import mkdir
from os.path import isdir
from netlists import *
from matplotlib.pyplot import close
from varname import nameof

"""
Created on Wed Jul 20 10:20:35 2022

Helper class which wraps a bunch of lcapy and sympy functions, designed to
output symbolic equations and schematics for copy/paste to the moodle "Formulas"
plugin.

Currently tested for DC analysis only - AC support will be added in late 2022
when the need crops up in the ENME313 course.

Once complex values start cropping up, a format option will be added to switch
output format to a STACK-friendly form (mostly just swapping ; for =).



How to use:
    The niggly manual part is creating netlists. According to the lcapy
    documentation, the easiest way to do this is to draw the circuit on paper
    and enumerate nodes. Label major nodes (where you want a node label and
    voltage) as a number e.g. 1, and other sub-nodes with underscores e.g. 1_1,
    1_2, etc.
    More detail in the Lcapy notes:
        https://lcapy.readthedocs.io/en/latest/netlists.html

    Initialise with netlist and optional filepath for saving figures (default
    is ./schematics/)

    The moodle_question class inherits all of lcapy's "Circuit" methods and
    attributes, so you can use it in exactly the same way. The additions for
    moodle are:

    get_node_voltages():
       Save and return a dict, keyed by Vn where n representsa node number
       of moodle-readable node voltages at primary nodes.

    get_component_currents():
        Save and return a dict, keyed by component name, of moodle-readable
        component currents.

    get_R_eq(load_component):
        return thevenin/norton equivalent resistance from the perspective of
        load component. Default load component is P1 - create your circuits
        with this to make it easier.
        returns and saves moodle-readable string to self.Thevenin_eq_v

    get_thev_v(load_component):
        return thevenin equivalent voltage from the perspective of
        load component. Default load component is P1 - create your circuits
        with this to make it easier.
        returns and saves moodle-readable string to self.Thevenin_eq_v

    get_nort_i(load_component):
        return norton equivalent current from the perspective of
        load component. Default load component is P1 - create your circuits
        with this to make it easier.
        returns and saves moodle-readable string to self.Norton_eq_i

    print_*(load_component):
        *: node_voltages, thev_v, nort_i, R_eq. Calls get_* if no data exists,
        then prints moodle-readable equation to console for easy copy paste

    export_schematic(filename):
        save consistently-formatted circuit diagram to figpath/filename.pdf

Example code:

#Uncomment these when using code - the triple-quote confuses things.
     norton_1_netlist = """
# R_1 0_1 1_1 {R_1}; up
# W 0_1 0; right
# W 1_1 1; right
# I_1 1 0 {I_1}; down
# R_2 1 2 {R_2}; right
# R_3 2 0_3 {R_3}; down
# W 0 0_3; right
# V_1 3 0_3 {V_1}; left
# W 2 2_2; right
# R_4 3 2_2 {R_4}; up
# W 2_2 2_3; right
# W 3 3_2; right
# P1 3_2 2_3; up
# A1 2_3; l=a, anchor=north
# A2 3_2; l=b, anchor=south
# ; node_spacing=4, scale=1
"""

    circuit_name = "norton_2"
    figpath = "./schematics/"

    cct = moodle_question(norton_1_netlist, figpath=figpath)
    cct.print_node_voltages()
    cct.print_thev_v()
    cct.print_nort_i()
    cct.print_R_eq()

    cct.export_schematic(circuit_name)


@author: cca78
"""


class moodle_question(Circuit):
    def __init__(self,
                 netlist,
                 name="example",
                 figpath="./schematics/"):
        super(moodle_question, self).__init__(netlist)
        self.node_voltages = {}
        self.mesh_currents = {}
        self.R_eq = 0
        self.Thevenin_eq_v = 0
        self.Norton_eq_i = 0
        self.component_currents = {}

        self.figpath = figpath

        if isdir(figpath) is not True:
            mkdir(figpath)

    def get_node_voltages(self):
        """Get voltage equation at each primary node (up to node 100,
        arbitrarily chosen). Requires primary nodes to be assigned in ascending
        order from 0.

        Returns and saves a dict of {node: voltage equation string)}"""

        # TODO: create list from cct.nodes and pick integer-only values to avoid
        # reliance on incremental node labelling.
        for i in range(100):
            try:
                code = ccode(self[i].v)
                code = code.splitlines()[-1]
                self.node_voltages[str(i)] = code
            except AttributeError:
                break

        return self.node_voltages

    def print_node_voltages(self):
        """Get and print node voltages to console"""
        if self.node_voltages == {}:
            self.get_node_voltages()

        for node, voltage in self.node_voltages.items():
            print("V" + node + "= " + voltage + ";")

    def get_component_currents(self):
        """Save and return a dict, keyed by component name, of moodle-readable
        component currents. """

        for component in self.cpts:
            if any(comp in component for comp in ['W', 'A', 'P', 'X']):
                pass
            else:
                raw_current = self[component].i
                c_current = ccode(raw_current).splitlines()[-1] + ";"
                self.component_currents[component] = c_current

        return self.component_currents

    def print_component_currents(self):
        """Get (if necessary) and print to console moodle-readable current
        equation strings for each component. """
        if self.component_currents == {}:
            self.get_component_currents()
        for component, current in self.component_currents.items():
            print("I_" + component + " = " + current)

    def get_R_eq(self, load_component="P1"):
        """Get, save, and return the equation of the thevenin/norton equivalent
        resistance from the perspective of load_component"""

        self.R_eq = ccode(self[load_component].thevenin().Z).splitlines()[-1]

        return self.R_eq

    def print_R_eq(self, load_component="P1"):
        """Get and print R_eq to console in moodle-readable format"""
        if self.R_eq == 0:
            self.get_R_eq(load_component)

        print("R_eq= " + self.R_eq + ";")

        return self.R_eq

    def get_thev_v(self, load_component="P1"):
        """Get, save, and return the equation of the thevenin equivalent
        voltage  VThfrom the perspective of load_component"""
        self.Thevenin_eq_v = ccode(
            self[load_component].thevenin().v
        ).splitlines()[-1]

        return self.Thevenin_eq_v

    def print_thev_v(self, load_component="P1"):
        """Get and print R_eq to console in moodle-readable format"""
        if self.Thevenin_eq_v == 0:
            self.get_thev_v(load_component)

        print("VTh= " + self.Thevenin_eq_v + ";")

    def get_nort_i(self, load_component="P1"):
        """Get, save, and return the equation of the norton equivalent
        current INo from the perspective of load_component"""
        self.Norton_eq_i = ccode(
            self[load_component].norton().Isc['t']
        ).splitlines()[-1]

        return self.Norton_eq_i

    def print_nort_i(self, load_component="P1"):
        """Get and print INo to console in moodle-readable format"""
        if self.Norton_eq_i == 0:
            self.get_nort_i(load_component)
        print("INo= " + self.Norton_eq_i + ";")

    def export_schematic(self, filename):
        self.draw(
            self.figpath + filename + ".pdf",
            draw_nodes="primary",
            label_nodes="primary",
        )
