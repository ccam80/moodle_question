# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 09:36:18 2022

@author: cca78
"""

norton_1_nl = """
            R1 0_1 1_1 {R1}; up
            W 0_1 0; right
            W 1_1 1; right
            I_1 1 0 {I1}; down
            R_2 1 2 {R2}; right
            R_3 2 0_3 {R3}; down
            W 0 0_3; right
            V_1 3 0_3 {V1}; left
            W 2 2_2; right
            R_4 3 2_2 {R4}; up
            W 2_2 2_3; right
            W 3 3_2; right
            P1 3_2 2_3; up
            A1 2_3; l=a, anchor=north
            A2 3_2; l=b, anchor=south
            ; node_spacing=4, scale=1
            """

mesh_1_nl = """
            W 0 0_3; up
            W 0 0_1; right
            W 0_1 0_2; right
            W 0_2 0_4; right
            W 0_4 0_5; right
            W 0_5 0_6; up
            V1 3_0 0_6 {V1}; right
            V2 1_0 0_3 {V2}; left
            R1 1_0 4_0 {R1}; right
            R2 4_0 3_0 {R2}; right
            R3 4_0 0_2 {R3}; down
            ; node_spacing=3, scale=1
            """

mesh_2_nl = """
            W 0 0_1; right
            W 0 0_4; up
            W 0_1 0_2; right
            W 0_2 0_3; up
            V1 4_2 0_4 {V1}; down
            W 4_2 4_1; right
            W 4_1 4_0; right
            R1 0_1 1_0 {R1}; up
            V2 2_0 1_0 {V2}; down
            R5 2_0 3_0 {R5}; right
            R4 4_0 3_0 {R4}; down
            R3 3_0 0_3 {R3}; down
            R2 2_0 4_1 {R2}; up
            ; node_spacing=3, scale=1
            """

mesh_4_nl = """
            W 0 0_3; right
            W 0 0_1; up
            W 0_1 0_2; up
            V1 3_2 0_2 {V1}; down
            W 3_2 3_1; right
            W 3_1 3_0; right
            R6 0_3 1_0 {R6}; right
            R5 1_0 2_0 {R5}; up
            R2 2_0 3_0 {R2}; up
            R1 3_1 4_0 {R1}; down
            R3 4_0 2_0 {R3}; right
            R4 0_3 5_0 {R4}; up
            V2 4_0 5_0 {V2}; down
            ; node_spacing=3, scale=1
            """

nodal_3_nl = """
            W 0 0_1; right
            I1 4_0 0 {I1}; down
            R1 4_0 1 {R1}; right
            R2 1 0_1 {R2}; down
            R3 0_1 3_0 {R3}; right
            R4 3_0 1_1 {R4}; up
            W 1 1_1; right
            ; node_spacing=4, scale=1
            """

nodal_4_nl = """
            W 0 0_1; right
            W 0_1 0_2; right
            W 0_2 0_3; right
            W 0_2 0_4; up
            I1 1_1 0 {I1}; down
            I2 2_1 0_3 {I2}; down
            W 2_1 2_2; up
            W 2_2 2; left
            W 1_1 1_2; up
            W 1_2 1; right
            R3 1 2 {R3}; right
            R1 1 3_0 {R1}; down
            R2 3_0 0_1 {R2}; down
            R4 2 0_4 {R4}; down
            ; node_spacing=2, scale=1
            """

nodal_e1_nl = """
                W 0 0_1; right
                W 0_1 0_2; right
                W 0_2 0_3; right
                I1 1 0 {I1}; down
                W 1 1_1; right
                R1 0_1 1_1 {R1}; up
                R2 1_1 2 {R2}; right
                R3 0_2 2 {R3}; up
                R4 2 3 {R4}; right
                R5 0_3 3 {R5}; up
                ; node_spacing=4, scale=1
                """


thevenin_1_nl = """
                W 0 0_1; right
                W 0_1 0_2; right
                V1 1_0 0 {V1}; down
                R1 1_0 2_0 {R1}; right
                R2 0_1 2_0 {R2};up
                W 2_0 2_1; right
                W 2_1 2_2; right
                R3 0_2 2_1; up
                R4 0_2 3_0; right
                P1 3_0 2_2; up
                A1 2_2; l=a, anchor=north
                A2 3_0; l=b, anchor=south
                ; node_spacing=4, scale=1
                """

names_list = ["Norton_1",
              "Mesh_1",
              "Mesh_2",
              "Mesh_4",
              "Nodal_3",
              "Nodal_4",
              "Nodal_e1",
              "Thevenin_1", ]

test_list = [norton_1_nl,
             mesh_1_nl,
             mesh_2_nl,
             mesh_4_nl,
             nodal_3_nl,
             nodal_4_nl,
             nodal_e1_nl,
             thevenin_1_nl,

             ]
