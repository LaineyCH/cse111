#import re
from formula import parse_formula

# Indexes for inner lists in the periodic table
NAME_INDEX = 0
ATOMIC_MASS_INDEX = 1
ATOMIC_NUMBER_INDEX = 2
# Indexes for inner lists in a symbol_quantity_list
SYMBOL_INDEX = 0
QUANTITY_INDEX = 1

def main():

    # Get a chemical formula for a molecule from the user.
    chem_formula = input("Please enter the molecular formula for your chemical sample: ")
    # Get the mass of a chemical sample in grams from the user.
    mass = float(input("Please enter the mass of the chemical sample (g): "))

    # Call the make_periodic_table function and store the periodic table in a variable.
    periodic_table = make_periodic_table()
    known_molecules_table = make_known_molecules_dictionary()

    # Call the parse_formula function to convert the chemical formula given by the user to a compound
    # list that stores element symbols and the quantity of atoms of each element in the molecule.
    compound_list = parse_formula(chem_formula, periodic_table)
    # Call the compute_molar_mass function to compute the molar mass of the molecule from the compound list.
    molar_mass = compute_molar_mass(compound_list, periodic_table)
    # Compute the number of moles in the sample.
    number_moles = compute_number_moles(mass, molar_mass)
    # Get the formula name
    formula_name = (get_formula_name(chem_formula, known_molecules_table)).title()
    # Compute the number of protonw
    number_of_ptotons = sum_protons(compound_list, periodic_table)

    # print all data to screen
    print(f"Your chemical compound is: {formula_name}")
    print(f"Molar Mass: {molar_mass} grams/mole")
    print(f"Number of moles in your sample: {number_moles: .5f} moles")
    print(f"Number of protons per molecule: {number_of_ptotons}")
    print("")

    
def make_periodic_table():
    """
    Compose a periodic table dictionary with each object in th edictionary
    representing an element in the form:
        symbol : [name, atomic mass, atomic number]
    Parameters: none
    Return: a periodic table distionary
    """
    periodic_table_list = {
        # symbol : [name, atomic_mass]
        "Ac" : ["Actinium",	227],
        "Ag" : ["Silver",	107.8682],
        "Al" : ["Aluminum",	26.9815386],
        "Ar" : ["Argon",	39.948],
        "As" : ["Arsenic",	74.9216],
        "At" : ["Astatine",	210],
        "Au" : ["Gold",	196.966569],
        "B" : ["Boron",	10.811],
        "Ba" : ["Barium",	137.327],
        "Be" : ["Beryllium",	9.012182],
        "Bi" : ["Bismuth",	208.9804],
        "Br" : ["Bromine",	79.904],
        "C" : ["Carbon",	12.0107],
        "Ca" : ["Calcium",	40.078],
        "Cd" : ["Cadmium",	112.411],
        "Ce" : ["Cerium",	140.116],
        "Cl" : ["Chlorine",	35.453],
        "Co" : ["Cobalt",	58.933195],
        "Cr" : ["Chromium",	51.9961],
        "Cs" : ["Cesium",	132.9054519],
        "Cu" : ["Copper",	63.546],
        "Dy" : ["Dysprosium",	162.5],
        "Er" : ["Erbium",	167.259],
        "Eu" : ["Europium",	151.964],
        "F" : ["Fluorine",	18.9984032],
        "Fe" : ["Iron",	55.845],
        "Fr" : ["Francium",	223],
        "Ga" : ["Gallium",	69.723],
        "Gd" : ["Gadolinium",	157.25],
        "Ge" : ["Germanium",	72.64],
        "H" : ["Hydrogen",	1.00794],
        "He" : ["Helium",	4.002602],
        "Hf" : ["Hafnium",	178.49],
        "Hg" : ["Mercury",	200.59],
        "Ho" : ["Holmium",	164.93032],
        "I" : ["Iodine",	126.90447],
        "In" : ["Indium",	114.818],
        "Ir" : ["Iridium",	192.217],
        "K" : ["Potassium",	39.0983],
        "Kr" : ["Krypton",	83.798],
        "La" : ["Lanthanum",	138.90547],
        "Li" : ["Lithium",	6.941],
        "Lu" : ["Lutetium",	174.9668],
        "Mg" : ["Magnesium",	24.305],
        "Mn" : ["Manganese",	54.938045],
        "Mo" : ["Molybdenum",	95.96],
        "N" : ["Nitrogen",	14.0067],
        "Na" : ["Sodium",	22.98976928],
        "Nb" : ["Niobium",	92.90638],
        "Nd" : ["Neodymium",	144.242],
        "Ne" : ["Neon",	20.1797],
        "Ni" : ["Nickel",	58.6934],
        "Np" : ["Neptunium",	237],
        "O" : ["Oxygen",	15.9994],
        "Os" : ["Osmium",	190.23],
        "P" : ["Phosphorus",	30.973762],
        "Pa" : ["Protactinium",	231.03588],
        "Pb" : ["Lead",	207.2],
        "Pd" : ["Palladium",	106.42],
        "Pm" : ["Promethium",	145],
        "Po" : ["Polonium",	209],
        "Pr" : ["Praseodymium",	140.90765],
        "Pt" : ["Platinum",	195.084],
        "Pu" : ["Plutonium",	244],
        "Ra" : ["Radium",	226],
        "Rb" : ["Rubidium",	85.4678],
        "Re" : ["Rhenium",	186.207],
        "Rh" : ["Rhodium",	102.9055],
        "Rn" : ["Radon",	222],
        "Ru" : ["Ruthenium",	101.07],
        "S" : ["Sulfur",	32.065],
        "Sb" : ["Antimony",	121.76],
        "Sc" : ["Scandium",	44.955912],
        "Se" : ["Selenium",	78.96],
        "Si" : ["Silicon",	28.0855],
        "Sm" : ["Samarium",	150.36],
        "Sn" : ["Tin",	118.71],
        "Sr" : ["Strontium",	87.62],
        "Ta" : ["Tantalum",	180.94788],
        "Tb" : ["Terbium",	158.92535],
        "Tc" : ["Technetium",	98],
        "Te" : ["Tellurium",	127.6],
        "Th" : ["Thorium",	232.03806],
        "Ti" : ["Titanium",	47.867],
        "Tl" : ["Thallium",	204.3833],
        "Tm" : ["Thulium",	168.93421],
        "U" : ["Uranium",	238.02891],
        "V" : ["Vanadium",	50.9415],
        "W" : ["Tungsten",	183.84],
        "Xe" : ["Xenon",	131.293],
        "Y" : ["Yttrium",	88.90585],
        "Yb" : ["Ytterbium",	173.054],
        "Zn" : ["Zinc",	65.38],
        "Zr" : ["Zirconium",	91.224],
    }

    # dictionary of atomic numbers for all 118 elements
    atomic_numbers = {
        "H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5, "C": 6, "N": 7, "O": 8, "F": 9, "Ne": 10,
        "Na": 11, "Mg": 12, "Al": 13, "Si": 14, "P": 15, "S": 16, "Cl": 17, "Ar": 18, "K": 19, "Ca": 20,
        "Sc": 21, "Ti": 22, "V": 23, "Cr": 24, "Mn": 25, "Fe": 26, "Co": 27, "Ni": 28, "Cu": 29, "Zn": 30,
        "Ga": 31, "Ge": 32, "As": 33, "Se": 34, "Br": 35, "Kr": 36, "Rb": 37, "Sr": 38, "Y": 39, "Zr": 40,
        "Nb": 41, "Mo": 42, "Tc": 43, "Ru": 44, "Rh": 45, "Pd": 46, "Ag": 47, "Cd": 48, "In": 49, "Sn": 50,
        "Sb": 51, "Te": 52, "I": 53, "Xe": 54, "Cs": 55, "Ba": 56, "La": 57, "Ce": 58, "Pr": 59, "Nd": 60,
        "Pm": 61, "Sm": 62, "Eu": 63, "Gd": 64, "Tb": 65, "Dy": 66, "Ho": 67, "Er": 68, "Tm": 69, "Yb": 70,
        "Lu": 71, "Hf": 72, "Ta": 73, "W": 74, "Re": 75, "Os": 76, "Ir": 77, "Pt": 78, "Au": 79, "Hg": 80,
        "Tl": 81, "Pb": 82, "Bi": 83, "Po": 84, "At": 85, "Rn": 86, "Fr": 87, "Ra": 88, "Ac": 89, "Th": 90,
        "Pa": 91, "U": 92, "Np": 93, "Pu": 94, "Am": 95, "Cm": 96, "Bk": 97, "Cf": 98, "Es": 99, "Fm": 100,
        "Md": 101, "No": 102, "Lr": 103, "Rf": 104, "Db": 105, "Sg": 106, "Bh": 107, "Hs": 108, "Mt": 109,
        "Ds": 110, "Rg": 111, "Cn": 112, "Nh": 113, "Fl": 114, "Mc": 115, "Lv": 116, "Ts": 117, "Og": 118
    }

    # add atomic numbers to the periodic table dictionary
    for element in periodic_table_list:
        if element in atomic_numbers:
            periodic_table_list[element].append(atomic_numbers[element])

    return periodic_table_list


def compute_molar_mass(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total molar mass of all the
    elements listed in symbol_quantity_list.
    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total molar mass of all the elements in
        symbol_quantity_list.
    For example, if symbol_quantity_list is [["H", 2], ["O", 1]],
    this function will calculate and return
    atomic_mass("H") * 2 + atomic_mass("O") * 1
    1.00794 * 2 + 15.9994 * 1
    18.01528
    """
    total_molar_mass = 0

    # Do the following for each inner list in the
    # compound symbol_quantity_list:
        # Separate the inner list into symbol and quantity.
        # Get the atomic mass for the symbol from the dictionary.
        # Multiply the atomic mass by the quantity.
        # Add the product into the total molar mass.
    for element in symbol_quantity_list:
        symbol = element[0]
        quantity = element[1]
        element_data = periodic_table_dict[symbol]
        atomic_mass = element_data[1]
        molar_mass = atomic_mass * quantity
        total_molar_mass += molar_mass

    # Return the total molar mass.
    return total_molar_mass


def compute_number_moles(mass, molar_mass):
    """
    Compute and return the number of moles for a sample of a chemical compound from its mass and molar mass
    Parameters
        mass: the mass of a chemical compound in grams
        molar_mass: the molar mass of teh chemical compound
    Return: the number of moles in the sample
    """
    return mass / molar_mass


def make_known_molecules_dictionary():
    """
    Compose a dictionary of known molecules with each object in the dictionary
    representing an element in the form:
        chemical formula : name
    Parameters: none
    Return: a dictionary of known molecules
    """
    known_molecules_dict = {
        "Al2O3": "aluminum oxide",
        "CH3OH": "methanol",
        "C2H6O": "ethanol",
        "C2H5OH": "ethanol",
        "C3H8O": "isopropyl alcohol",
        "C3H8": "propane",
        "C4H10": "butane",
        "C6H6": "benzene",
        "C6H14": "hexane",
        "C8H18": "octane",
        "CaCO3": "calcium carbonate",
        "CH3(CH2)6CH3": "octane",
        "CH3COOH": "acetic acid",
        "C13H18O2": "ibuprofen",
        "C13H16N2O2": "melatonin",
        "Fe2O3": "iron oxide",
        "FeS2": "iron pyrite",
        "H2O": "water",
        "K2CO3": "patassium carbonate",
        "Li3PO4": "lithium phosphate",
        "NH3": "ammonia",
        "Pb(NO3)2": "lead nitrate",
        "ZnCO3": "zinc carbonate"
    }
    return known_molecules_dict


def get_formula_name(formula, known_molecules_dict):
    """Try to find formula in the known_molecules_dict.
    If formula is in the known_molecules_dict, return
    the name of the chemical formula; otherwise return
    "unknown compound".
    Parameters
        formula is a string that contains a chemical formula
        known_molecules_dict is a dictionary that contains
            known chemical formulas and their names
    Return: the name of a chemical formula
    """
    if formula in known_molecules_dict:
        name = known_molecules_dict[formula]
    else:
        name = "unknown compound"
    return name


def sum_protons(symbol_quantity_list, periodic_table_dict):
    """Compute and return the total number of protons in
    all the elements listed in symbol_quantity_list.
    Parameters
        symbol_quantity_list is a compound list returned
            from the parse_formula function. Each small
            list in symbol_quantity_list has this form:
            ["symbol", quantity].
        periodic_table_dict is the compound dictionary
            returned from make_periodic_table.
    Return: the total number of protons of all
        the elements in symbol_quantity_list.
    """
    total_number_of_protons = 0

    for element in symbol_quantity_list:
        symbol = element[0]
        quantity = element[1]
        element_data = periodic_table_dict[symbol]
        atomic_number = element_data[2] 
        number_of_protons = atomic_number * quantity
        total_number_of_protons += atomic_number

    return total_number_of_protons


if __name__ == "__main__":
    main()


#def find_elements(chemical_formula, periodic_table):
#    # use regular expression that describes genreal element symbols
#        # an upper case letter followed by an optional loer case letter
#    element_symbol_pattern = r'[A-Z][a-z]?'
#    #element_and_number_pattern = r'([A-Z][a-z]?)(\d*)'
#    # Find all matches in the chem_formula string and return as list of elements
#    element_symbol_list = re.findall(element_symbol_pattern, chemical_formula)
#    
#    #print each element in the user's chemical
#    for element_symbol in element_symbol_list:
#
#        # loop through the periodic_table to find element and print
#        for element in periodic_table:
#            if element[ELEMENT_SYMBOL_INDEX] == element_symbol:
#                element_name = element[ELEMENT_NAME_INDEX]
#                atomic_mass = element[ATOMIC_MASS_INDEX]
#                print(f"{element_name} {atomic_mass}")
#                break
