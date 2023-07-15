periodic_table = [
    {"symbol": "H", "name": "Hydrogen", "bonds": 1, "colour": "gray45"},
    {"symbol": "He", "name": "Helium", "bonds": 0},
    {"symbol": "Li", "name": "Lithium", "bonds": 1},
    {"symbol": "Be", "name": "Beryllium", "bonds": 2},
    {"symbol": "B", "name": "Boron", "bonds": 3, "colour": "light slate blue"},
    {"symbol": "C", "name": "Carbon", "bonds": 4, "colour": "gray11"},
    {"symbol": "N", "name": "Nitrogen", "bonds": 3, "colour": "deep sky blue"},
    {"symbol": "O", "name": "Oxygen", "bonds": 2, "colour": "red2"},
    {"symbol": "F", "name": "Fluorine", "bonds": 1, "colour": "lime green"},
    {"symbol": "Ne", "name": "Neon", "bonds": 0},
    {"symbol": "Na", "name": "Sodium", "bonds": 1},
    {"symbol": "Mg", "name": "Magnesium", "bonds": 2},
    {"symbol": "Al", "name": "Aluminum", "bonds": 3},
    {"symbol": "Si", "name": "Silicon", "bonds": 4, "colour": "SkyBlue4"},
    {"symbol": "P", "name": "Phosphorus", "bonds": 3, "colour": "DodgerBlue4"},
    {"symbol": "S", "name": "Sulfur", "bonds": 2, "colour": "yellow3"},
    {"symbol": "Cl", "name": "Chlorine", "bonds": 1, "colour": "green yellow"},
    {"symbol": "Ar", "name": "Argon", "bonds": 0},
    {"symbol": "K", "name": "Potassium", "bonds": 1},
    {"symbol": "Ca", "name": "Calcium", "bonds": 2},
    {"symbol": "Sc", "name": "Scandium", "bonds": 3},
    {"symbol": "Ti", "name": "Titanium", "bonds": 4},
    {"symbol": "V", "name": "Vanadium", "bonds": 5},
    {"symbol": "Cr", "name": "Chromium", "bonds": 6},
    {"symbol": "Mn", "name": "Manganese", "bonds": 7},
    {"symbol": "Fe", "name": "Iron", "bonds": 8},
    {"symbol": "Co", "name": "Cobalt", "bonds": 9},
    {"symbol": "Ni", "name": "Nickel", "bonds": 10},
    {"symbol": "Cu", "name": "Copper", "bonds": 11},
    {"symbol": "Zn", "name": "Zinc", "bonds": 12},
    {"symbol": "Ga", "name": "Gallium", "bonds": 3},
    {"symbol": "Ge", "name": "Germanium", "bonds": 4},
    {"symbol": "As", "name": "Arsenic", "bonds": 3},
    {"symbol": "Se", "name": "Selenium", "bonds": 2},
    {"symbol": "Br", "name": "Bromine", "bonds": 1, "colour": "LightSalmon4"},
    {"symbol": "Kr", "name": "Krypton", "bonds": 0},
    {"symbol": "Rb", "name": "Rubidium", "bonds": 1},
    {"symbol": "Sr", "name": "Strontium", "bonds": 2},
    {"symbol": "Y", "name": "Yttrium", "bonds": 3},
    {"symbol": "Zr", "name": "Zirconium", "bonds": 4},
    {"symbol": "Nb", "name": "Niobium", "bonds": 5},
    {"symbol": "Mo", "name": "Molybdenum", "bonds": 6},
    {"symbol": "Tc", "name": "Technetium", "bonds": 7},
    {"symbol": "Ru", "name": "Ruthenium", "bonds": 8},
    {"symbol": "Rh", "name": "Rhodium", "bonds": 9},
    {"symbol": "Pd", "name": "Palladium", "bonds": 10},
    {"symbol": "Ag", "name": "Silver", "bonds": 11},
    {"symbol": "Cd", "name": "Cadmium", "bonds": 12},
    {"symbol": "In", "name": "Indium", "bonds": 3},
    {"symbol": "Sn", "name": "Tin", "bonds": 4},
    {"symbol": "Sb", "name": "Antimony", "bonds": 3},
    {"symbol": "Te", "name": "Tellurium", "bonds": 2},
    {"symbol": "I", "name": "Iodine", "bonds": 1, "colour": "blue violet"},
    {"symbol": "Xe", "name": "Xenon", "bonds": 0},
    {"symbol": "Cs", "name": "Cesium", "bonds": 1},
    {"symbol": "Ba", "name": "Barium", "bonds": 2},
    {"symbol": "La", "name": "Lanthanum", "bonds": 3},
    {"symbol": "Ce", "name": "Cerium", "bonds": 4},
    {"symbol": "Pr", "name": "Praseodymium", "bonds": 5},
    {"symbol": "Nd", "name": "Neodymium", "bonds": 6},
    {"symbol": "Pm", "name": "Promethium", "bonds": 7},
    {"symbol": "Sm", "name": "Samarium", "bonds": 8},
    {"symbol": "Eu", "name": "Europium", "bonds": 9},
    {"symbol": "Gd", "name": "Gadolinium", "bonds": 10},
    {"symbol": "Tb", "name": "Terbium", "bonds": 11},
    {"symbol": "Dy", "name": "Dysprosium", "bonds": 12},
    {"symbol": "Ho", "name": "Holmium", "bonds": 13},
    {"symbol": "Er", "name": "Erbium", "bonds": 14},
    {"symbol": "Tm", "name": "Thulium", "bonds": 15},
    {"symbol": "Yb", "name": "Ytterbium", "bonds": 16},
    {"symbol": "Lu", "name": "Lutetium", "bonds": 17},
    {"symbol": "Hf", "name": "Hafnium", "bonds": 4},
    {"symbol": "Ta", "name": "Tantalum", "bonds": 5},
    {"symbol": "W", "name": "Tungsten", "bonds": 6},
    {"symbol": "Re", "name": "Rhenium", "bonds": 7},
    {"symbol": "Os", "name": "Osmium", "bonds": 8},
    {"symbol": "Ir", "name": "Iridium", "bonds": 9},
    {"symbol": "Pt", "name": "Platinum", "bonds": 10},
    {"symbol": "Au", "name": "Gold", "bonds": 11},
    {"symbol": "Hg", "name": "Mercury", "bonds": 12},
    {"symbol": "Tl", "name": "Thallium", "bonds": 3},
    {"symbol": "Pb", "name": "Lead", "bonds": 4},
    {"symbol": "Bi", "name": "Bismuth", "bonds": 3},
    {"symbol": "Po", "name": "Polonium", "bonds": 2},
    {"symbol": "At", "name": "Astatine", "bonds": 1},
    {"symbol": "Rn", "name": "Radon", "bonds": 0},
    {"symbol": "Fr", "name": "Francium", "bonds": 1},
    {"symbol": "Ra", "name": "Radium", "bonds": 2},
    {"symbol": "Ac", "name": "Actinium", "bonds": 3},
    {"symbol": "Th", "name": "Thorium", "bonds": 4},
    {"symbol": "Pa", "name": "Protactinium", "bonds": 5},
    {"symbol": "U", "name": "Uranium", "bonds": 6},
    {"symbol": "Np", "name": "Neptunium", "bonds": 7},
    {"symbol": "Pu", "name": "Plutonium", "bonds": 8},
    {"symbol": "Am", "name": "Americium", "bonds": 9},
    {"symbol": "Cm", "name": "Curium", "bonds": 10},
    {"symbol": "Bk", "name": "Berkelium", "bonds": 11},
    {"symbol": "Cf", "name": "Californium", "bonds": 12},
    {"symbol": "Es", "name": "Einsteinium", "bonds": 13},
    {"symbol": "Fm", "name": "Fermium", "bonds": 14},
    {"symbol": "Md", "name": "Mendelevium", "bonds": 15},
    {"symbol": "No", "name": "Nobelium", "bonds": 16},
    {"symbol": "Lr", "name": "Lawrencium", "bonds": 17},
    {"symbol": "Rf", "name": "Rutherfordium", "bonds": 4},
    {"symbol": "Db", "name": "Dubnium", "bonds": 5},
    {"symbol": "Sg", "name": "Seaborgium", "bonds": 6},
    {"symbol": "Bh", "name": "Bohrium", "bonds": 7},
    {"symbol": "Hs", "name": "Hassium", "bonds": 8},
    {"symbol": "Mt", "name": "Meitnerium", "bonds": 9},
    {"symbol": "Ds", "name": "Darmstadtium", "bonds": 10},
    {"symbol": "Rg", "name": "Roentgenium", "bonds": 11},
    {"symbol": "Cn", "name": "Copernicium", "bonds": 12},
    {"symbol": "Nh", "name": "Nihonium", "bonds": 3},
    {"symbol": "Fl", "name": "Flerovium", "bonds": 2},
    {"symbol": "Mc", "name": "Moscovium", "bonds": 1},
    {"symbol": "Lv", "name": "Livermorium", "bonds": 0},
    {"symbol": "Ts", "name": "Tennessine", "bonds": 1},
    {"symbol": "Og", "name": "Oganesson", "bonds": 0},
]

radioactive_elements = {
    "U": {
        "name": "Uranium",
        "isotopes": {
            235: {"half_life": "703.8 million years", "decay_types": ["Alpha decay"]},
            238: {"half_life": "4.5 billion years", "decay_types": ["Alpha decay"]}
        }
    },
    "Th": {
        "name": "Thorium",
        "isotopes": {
            232: {"half_life": "14.1 billion years", "decay_types": ["Alpha decay"]}
        }
    },
    "Ra": {
        "name": "Radium",
        "isotopes": {
            226: {"half_life": "1600 years", "decay_types": ["Alpha decay"]}
        }
    },
    "Pu": {
        "name": "Plutonium",
        "isotopes": {
            239: {"half_life": "24,100 years", "decay_types": ["Alpha decay"]}
        }
    },
    "Cm": {
        "name": "Curium",
        "isotopes": {
            244: {"half_life": "18.1 years", "decay_types": ["Alpha decay"]},
            245: {"half_life": "8,500 years", "decay_types": ["Alpha decay"]}
        }
    },
    "Po": {
        "name": "Polonium",
        "isotopes": {
            210: {"half_life": "138 days", "decay_types": ["Alpha decay"]}
        }
    },
    "K": {
        "name": "Potassium",
        "isotopes": {
            40: {"half_life": "1.25 billion years", "decay_types": ["Beta decay"]}
        }
    },
    "C": {
        "name": "Carbon",
        "isotopes": {
            14: {"half_life": "5730 years", "decay_types": ["Beta decay"]}
        }
    },
    "H": {
        "name": "Hydrogen",
        "isotopes": {
            3: {"half_life": "12.3 years", "decay_types": ["Beta decay"]}
        }
    },
    "I": {
        "name": "Iodine",
        "isotopes": {
            131: {"half_life": "8.02 days", "decay_types": ["Beta decay"]}
        }
    },
    "Sr": {
        "name": "Strontium",
        "isotopes": {
            90: {"half_life": "28.8 years", "decay_types": ["Beta decay"]}
        }
    },
    "Tc": {
        "name": "Technetium",
        "isotopes": {
            99: {"half_life": "211,000 years", "decay_types": ["Beta decay"]}
        }
    },
    "Cs": {
        "name": "Cesium",
        "isotopes": {
            137: {"half_life": "30.17 years", "decay_types": ["Beta decay"]}
        }
    },
    "Co": {
        "name": "Cobalt",
        "isotopes": {
            60: {"half_life": "5.27 years", "decay_types": ["Beta decay"]}
        }
    },
    "Am": {
        "name": "Americium",
        "isotopes": {
            241: {"half_life": "432.2 years", "decay_types": ["Alpha decay"]}
        }
    },
    "Cf": {
        "name": "Californium",
        "isotopes": {
            252: {"half_life": "2.645 years", "decay_types": ["Alpha decay"]}
        }
    }
}