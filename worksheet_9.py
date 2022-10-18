##########################################################
## BME 210:  Worksheet 9 Python code                    ##
##  ______     ______     __  __                        ##
## /\  __ \   /\  ___\   /\ \/\ \                       ##
## \ \  __ \  \ \___  \  \ \ \_\ \                      ##
##  \ \_\ \_\  \/\_____\  \ \_____\                     ##
##   \/_/\/_/   \/_____/   \/_____/                     ##
## @Developed by: BME 210 class                         ##
##   (https://plaisierlab.engineering.asu.edu/)         ##
##   Arizona State University                           ##
##   242 ISTB1, 550 E Orange St                         ##
##   Tempe, AZ  85281                                   ##
## @Author:  Chris Plaisier                             ##
## @License:  GNU GPLv3                                 ##
##                                                      ##
## If this program is used in your analysis please      ##
## mention who built it. Thanks. :-)                    ##
##########################################################

## Your name
# <Replace with your name>




## Import required packages




## 1. Load up periodic table of elements data
# Deliverables:
#   a. Open the 'periodic_table_lookup.json' file
#   b. Load periodic table of elements data into variable called 'ptoe_all'
#   c. Print the keys for 'ptoe_all'
#   d. Print the key 'order'
#   e. Print the key 'carbon'
#   f. Print the atomic symbol for 'carbon'
#   g. Print the atomic mass for 'carbon'




## 2. Build a dictionary that is keyed off atomic symobl and has atomic mass as a value
#     Molecules will be given as dictionaries with atomic symbol as key and value being the
#     number of atoms. The ptoe_all is keyed off the full atom name, and we want to have the
#     atomic mass keyed off the atomic symbol. {'C': 12.011, ... }
# Deliverables:
#   a. Initialize a new dictionary 'ptoe'
#   b. Iterate through all 'ptoe_all' atoms (easiest to use ptoe_all['order'] as the iterable)
#   c. Add each atom into 'ptoe' with atomic symbol ('symbol') as the key and atomic mass
#      ('atomic_mass') as the value
#   d. Print the atomic mass of 'C' using 'ptoe'
#   e. Print the atomic mass of 'Fe' using 'ptoe'
#   f. Print the atomic mass of 'U' using 'ptoe'




## 3. Define a function 'molecular_weight' to find the molecular weight of molecules
# Deliverables:
#   a. Write a function 'molecular_weight' that:
#      - Takes two arguments 'molecule' and 'ptoe'
#        a. 'molecule' argument is a dictionary of atoms in the molecule with the value being the number of atoms
#        b. 'ptoe' the dictionary you developed above with atomic symbol as keys and atomic mass as values
#      - Use the atomic weights and the molecular composition to compute the molecular weight
#      - Return the molecular weight
#      - Docstrings to document the function
#   b. Print the results of these tests using the following molecules:
#      - Glycine = C2H5NO2
#      - Glucose = C6H12O6
#      - Palmitic acid = C16H32O2
#      - ATP = C10H16N5O13P3
#      - Dichlorodifluoromethane = CCl2F2
#      - Selenocysteine = C3H7NO2Se
#      - Heme B = C34H32O4N4Fe
#   c. Check molecular weights on the web to make sure your code, function, and tests are working correctly




