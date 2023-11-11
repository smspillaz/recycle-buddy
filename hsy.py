import itertools

HSY_MAIN_TYPES = [
    {"name": "Vehicle battery"},
    {"name": "Asbestos waste"},
    {"name": "Bio waste"},
    {"name": "With insulators"},
    {"name": "Specially treated waste"},
    {"name": "Large objects"},
    {"name": "Cardboard packages"},
    {"name": "Plaster waste"},
    {"name": "Aggregate"},
    {"name": "Usable items"},
    {"name": "Glass packaging"},
    {"name": "Medical waste (hazardous waste)"},
    {"name": "Soil material"},
    {"name": "Metal"},
    {"name": "Plastic"},
    {"name": "Plastic packaging"},
    {"name": "Pressure impregnated wood"},
    {"name": "Non-burnable waste"},
    {"name": "Paper"},
    {"name": "Small metal"},
    {"name": "Removal textile"},
    {"name": "Wood waste"},
    {"name": "Garden waste"},
    {"name": "Construction and demolition waste"},
    {"name": "Tires"},
    {"name": "Twigs and branches"},
    {"name": "Scrap cars"},
    {"name": "Mixed waste"},
    {"name": "Scrap electrical equipment (SER)"},
    {"name": "Hazardous waste (formerly hazardous waste)"},
]

RECYCLING_STREAMS = """
Automotive batteries (lead acid)
Carton packaging
Construction waste
Electrical equipments
End-of-life textiles
Energy waste
Garden waste
Glass packaging
Hazardous waste
Impregnated wood
Lamps
Metals
Mixed waste
Other waste
Paper
Plastic packaging
Portable accumulators and batteries
Textiles (reusable)
Wood
"""

HSY_OPTIONS = [
    [
        {
            "name": "Battery - lead-acid vehicle battery",
            "options": [
                "Kivikko hazardous waste reception station",
                "Other reception points",
                "Sortti stations",
                "Sortti collection trucks (for households)",
            ],
        }
    ],
    [
        {
            "name": "Asbestos",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Ämmässuo Sortti station",
            ],
        },
        {
            "name": "Chrysotile",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Ämmässuo Sortti station",
            ],
        },
        {
            "name": "Hard drive",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Ämmässuo Sortti station",
            ],
        },
        {
            "name": "Kenitex",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Ämmässuo Sortti station",
            ],
        },
    ],
    [
        {
            "name": "Disposable cutlery, wood",
            "options": ["The property's biowaste container", "Property composter"],
        },
        {
            "name": "Grill stick",
            "options": [
                "The property's biowaste container",
                "Property's metal collection container",
                "Rinki eco point",
            ],
        },
        {
            "name": "Sushi sticks",
            "options": [
                "The property's biowaste container",
                "The property's mixed waste container",
            ],
        },
        {
            "name": "Plant",
            "options": ["The property's biowaste container", "Property composter"],
        },
        {
            "name": "Egg shells",
            "options": ["The property's biowaste container", "Property composter"],
        },
        {
            "name": "Tissue",
            "options": ["The property's biowaste container", "Property composter"],
        },
        {
            "name": "Mold",
            "options": [
                "The property's biowaste container",
                "Property composter",
                "Landfills",
                "Sortti stations",
            ],
        },
        {
            "name": "Clam, snail and crab shells",
            "options": [
                "The property's biowaste container",
                "The property's mixed waste container",
            ],
        },
        {
            "name": "Cone",
            "options": [
                "The property's biowaste container",
                "Property composter",
                "Sortti stations",
            ],
        },
        {
            "name": "Muffin tin (paper)",
            "options": ["The property's biowaste container"],
        },
    ],
    [
        {
            "name": "Insulating wool (mineral wool)",
            "options": [
                "The property's mixed waste container",
                "Truck loads / Ämmässuo eco-industry center",
                "Sortti stations",
            ],
        }
    ],
    [
        {"name": "Flare", "options": []},
        {
            "name": "Asbestos",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Ämmässuo Sortti station",
            ],
        },
        {
            "name": "Chrysotile",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Ämmässuo Sortti station",
            ],
        },
        {"name": "Projectile", "options": ["Police"]},
        {
            "name": "Railroad sleeper, telephone pole",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Other reception points",
                "Sortti stations",
            ],
        },
        {
            "name": "Data protection paper",
            "options": [
                "Kivikko hazardous waste reception station",
                "Other reception points",
            ],
        },
        {
            "name": "Furniture, clothes and textiles containing bedbugs",
            "options": ["Other reception points"],
        },
        {"name": "Dry toilet waste", "options": ["Ämmässuo eco-industry center"]},
        {"name": "Fireworks", "options": ["Other reception points", "Police"]},
        {
            "name": "Cartridge case",
            "options": [
                "Property's metal collection container",
                "The property's mixed waste container",
                "Police",
                "Rinki eco point",
            ],
        },
    ],
    [
        {
            "name": "Piano",
            "options": ["Recycling centers and flea markets", "Sortti stations"],
        },
        {
            "name": "Furniture, upholstered",
            "options": [
                "Recycling centers and flea markets",
                "Sortti stations",
                "Sortti pick-up",
                "Sortti small station",
            ],
        },
        {
            "name": "Trampoline",
            "options": ["Recycling centers and flea markets", "Sortti stations"],
        },
    ],
    [
        {
            "name": "Instructions for use, product descriptions",
            "options": ["The property's cardboard container", "Rinki eco point"],
        },
        {
            "name": "Paper wrapper",
            "options": ["The property's cardboard container", "Rinki eco point"],
        },
        {
            "name": "Cardboard",
            "options": [
                "The property's cardboard container",
                "Other reception points",
                "Rinki eco point",
                "Sortti stations",
            ],
        },
        {
            "name": "Cardboard sleeve",
            "options": ["The property's cardboard container", "Rinki eco point"],
        },
        {
            "name": "A paper bag",
            "options": ["The property's cardboard container", "Rinki eco point"],
        },
        {
            "name": "Yogurt can, cardboard",
            "options": ["The property's cardboard container", "Rinki eco point"],
        },
        {
            "name": "Potato chip tube",
            "options": ["The property's cardboard container", "Rinki eco point"],
        },
        {
            "name": "A paper bag",
            "options": ["The property's cardboard container", "Rinki eco point"],
        },
        {
            "name": "Floral wrapping paper",
            "options": ["The property's cardboard container", "Rinki eco point"],
        },
        {
            "name": "Tap wine packaging",
            "options": [
                "The property's cardboard container",
                "The property's plastic packaging container",
                "Rinki eco point",
            ],
        },
    ],
    [
        {
            "name": "Gyproc board, plasterboard",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Sortti stations",
            ],
        },
        {
            "name": "Plaster statue",
            "options": ["The property's mixed waste container", "Sortti stations"],
        },
        {
            "name": "Gypsum powder",
            "options": ["The property's mixed waste container", "Sortti stations"],
        },
    ],
    [
        {
            "name": "Marble base",
            "options": ["The property's mixed waste container", "Sortti stations"],
        },
        {
            "name": "Soil materials",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Landfills",
                "Sortti stations",
            ],
        },
        {
            "name": "Tarmac",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Sortti stations",
            ],
        },
        {
            "name": "Mold",
            "options": [
                "The property's biowaste container",
                "Property composter",
                "Landfills",
                "Sortti stations",
            ],
        },
        {"name": "Concrete", "options": ["Sortti stations"]},
        {
            "name": "Cement",
            "options": [
                "Kivikko hazardous waste reception station",
                "Sortti stations",
                "Sortti containers for hazardous waste",
            ],
        },
        {"name": "Tile", "options": ["Sortti stations"]},
        {
            "name": "Roof tile",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Sortti stations",
            ],
        },
        {
            "name": "Stove stones",
            "options": ["The property's mixed waste container", "Sortti stations"],
        },
        {"name": "Leca ingot", "options": ["Sortti stations"]},
    ],
    [
        {
            "name": "Outerwear, down jacket",
            "options": [
                "Recycling centers and flea markets",
                "The property's mixed waste container",
            ],
        },
        {
            "name": "I drew a ruler",
            "options": [
                "The point of the recycling center in Jorvak, Kiviko, Konala. At Ruskeasanna and Ämmässuo's Sortti station",
                "Recycling centers and flea markets",
                "The property's mixed waste container",
            ],
        },
        {
            "name": "Club",
            "options": [
                "The point of the recycling center in Jorvak, Kiviko, Konala. At Ruskeasanna and Ämmässuo's Sortti station",
                "Recycling centers and flea markets",
                "The property's mixed waste container",
            ],
        },
        {
            "name": "Cooler bag",
            "options": [
                "Recycling centers and flea markets",
                "The property's mixed waste container",
                "Sortti stations",
            ],
        },
        {
            "name": "Coin",
            "options": [
                "Property's metal collection container",
                "Other reception points",
                "Rinki eco point",
            ],
        },
        {
            "name": "Knitting needle, crochet hook",
            "options": [
                "Recycling centers and flea markets",
                "Property's metal collection container",
                "The property's mixed waste container",
            ],
        },
        {
            "name": "Boots",
            "options": [
                "Recycling centers and flea markets",
                "The property's mixed waste container",
            ],
        },
        {
            "name": "LP record",
            "options": [
                "Recycling centers and flea markets",
                "The property's mixed waste container",
            ],
        },
        {
            "name": "Skis, snowboard",
            "options": [
                "Recycling centers and flea markets",
                "The property's mixed waste container",
                "Sortti stations",
                "Sortti small station",
            ],
        },
        {
            "name": "CD/DVD disc",
            "options": [
                "The point of the recycling center in Jorvak, Kiviko, Konala. At Ruskeasanna and Ämmässuo's Sortti station",
                "Recycling centers and flea markets",
                "The property's mixed waste container",
            ],
        },
        {
            "name": "Boots",
            "options": [
                "Recycling centers and flea markets",
                "The property's mixed waste container",
            ],
        },
        {
            "name": "LP record",
            "options": [
                "Recycling centers and flea markets",
                "The property's mixed waste container",
            ],
        },
        {
            "name": "Skis, snowboard",
            "options": [
                "Recycling centers and flea markets",
                "The property's mixed waste container",
                "Sortti stations",
                "Sortti small station",
            ],
        },
        {
            "name": "CD/DVD disc",
            "options": [
                "The point of the recycling center in Jorvak, Kiviko, Konala. At Ruskeasanna and Ämmässuo's Sortti station",
                "Recycling centers and flea markets",
                "The property's mixed waste container",
            ],
        },
    ],
    [
        {
            "name": "Cosmetic packaging, glass",
            "options": [
                "The property's glass collection container",
                "The property's mixed waste container",
                "Rinki eco point",
            ],
        },
        {
            "name": "Glass bottle, glass jar",
            "options": [
                "The property's glass collection container",
                "Rinki eco point",
                "Sortti stations",
            ],
        },
    ],
    [
        {"name": "Eye drops", "options": ["Pharmacy"]},
        {
            "name": "Mouthwash",
            "options": ["Pharmacy", "The property's mixed waste container"],
        },
        {"name": "Asthma pipe", "options": ["Pharmacy"]},
        {"name": "Medicated patch", "options": ["Pharmacy"]},
        {"name": "Medicines", "options": ["Pharmacy"]},
        {"name": "Iodine tablets", "options": ["Pharmacy"]},
        {"name": "Syringe, needle", "options": ["Pharmacy"]},
        {
            "name": "Insulin pen",
            "options": ["Pharmacy", "Sortti collection trucks (for households)"],
        },
    ],
    [
        {
            "name": "Soil materials",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Landfills",
                "Sortti stations",
            ],
        }
    ],
    [
        {
            "name": "Metal rim",
            "options": [
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Sortti small station",
            ],
        },
        {
            "name": "Oven tray",
            "options": [
                "Property's metal collection container",
                "Rinki eco point",
                "Sortti stations",
                "Sortti collection trucks (for households)",
            ],
        },
        {
            "name": "Gas spring",
            "options": [
                "Property's metal collection container",
                "Rinki eco point",
                "Sortti stations",
                "Sortti collection trucks (for households)",
            ],
        },
        {
            "name": "Pet cage, metal",
            "options": ["Sortti stations", "Sortti collection trucks (for households)"],
        },
        {
            "name": "Copper tube",
            "options": [
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Sortti small station",
            ],
        },
        {
            "name": "Welding stick, welding wire",
            "options": [
                "Property's metal collection container",
                "Rinki eco point",
                "Sortti stations",
                "Sortti collection trucks (for households)",
            ],
        },
        {
            "name": "Gas cooker",
            "options": ["Sortti stations", "Sortti collection trucks (for households)"],
        },
        {
            "name": "Hoe, blade part",
            "options": [
                "Property's metal collection container",
                "Sortti stations",
                "Sortti collection trucks (for households)",
            ],
        },
        {
            "name": "Wheelbarrows",
            "options": ["Sortti stations", "Sortti collection trucks (for households)"],
        },
        {"name": "Roof sheet", "options": ["Sortti stations"]},
    ],
    [
        {
            "name": "Plastic box, compartment",
            "options": [
                "The property's mixed waste container",
                "Plastic collection at Sortti stations",
            ],
        },
        {
            "name": "Swimming pool, hard plastic",
            "options": ["Plastic collection at Sortti stations"],
        },
        {
            "name": "Drink bottle, plastic",
            "options": [
                "The property's mixed waste container",
                "Plastic collection at Sortti stations",
            ],
        },
        {
            "name": "Barrel, plastic",
            "options": [
                "Other reception points",
                "Plastic collection at Sortti stations",
            ],
        },
        {
            "name": "Freezer box, freezer box",
            "options": [
                "The property's mixed waste container",
                "Plastic collection at Sortti stations",
            ],
        },
        {
            "name": "Shrink plastic, shrink film",
            "options": [
                "The property's mixed waste container",
                "Plastic collection at Sortti stations",
            ],
        },
        {
            "name": "ABS plastic",
            "options": ["The property's mixed waste container", "Sortti stations"],
        },
        {
            "name": "Plastic canister",
            "options": [
                "The property's plastic packaging container",
                "The property's mixed waste container",
                "Rinki eco point",
                "Plastic collection at Sortti stations",
            ],
        },
        {
            "name": "Plastic",
            "options": [
                "The property's plastic packaging container",
                "The property's mixed waste container",
                "Rinki eco point",
                "Plastic collection at Sortti stations",
            ],
        },
        {
            "name": "Kitchen utensil, plastic",
            "options": [
                "The property's mixed waste container",
                "Plastic collection at Sortti stations",
            ],
        },
    ],
    [
        {
            "name": "Styrofoam balls and granules (package fillings)",
            "options": [
                "The property's plastic packaging container",
                "Rinki eco point",
            ],
        },
        {
            "name": "Sunflower seed bag",
            "options": [
                "The property's plastic packaging container",
                "Rinki eco point",
            ],
        },
        {
            "name": "Coffee package",
            "options": [
                "The property's plastic packaging container",
                "Rinki eco point",
            ],
        },
        {
            "name": "Plastic packaging",
            "options": [
                "The property's plastic packaging container",
                "Rinki eco point",
            ],
        },
        {
            "name": "Biodegradable plastic",
            "options": [
                "The property's plastic packaging container",
                "The property's mixed waste container",
                "Rinki eco point",
            ],
        },
        {
            "name": "Bag sealer",
            "options": [
                "Property's metal collection container",
                "The property's plastic packaging container",
                "Rinki eco point",
            ],
        },
        {
            "name": "Coffee capsule",
            "options": [
                "Property's metal collection container",
                "The property's plastic packaging container",
                "The property's mixed waste container",
                "Rinki eco point",
            ],
        },
        {
            "name": "Tube of toothpaste",
            "options": [
                "The property's plastic packaging container",
                "Rinki eco point",
            ],
        },
        {
            "name": "Tap wine packaging",
            "options": [
                "The property's cardboard container",
                "The property's plastic packaging container",
                "Rinki eco point",
            ],
        },
        {
            "name": "Cable tie",
            "options": [
                "The property's plastic packaging container",
                "The property's mixed waste container",
                "Rinki eco point",
            ],
        },
    ],
    [
        {
            "name": "Pressure impregnated wood, durable wood",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Other reception points",
                "Sortti stations",
            ],
        }
    ],
    [
        {
            "name": "Mirror glass",
            "options": ["The property's mixed waste container", "Sortti stations"],
        },
        {"name": "Stone dust", "options": ["Sortti stations"]},
        {"name": "Luginoma wall", "options": ["Sortti stations"]},
        {
            "name": "Flower pot, ceramic",
            "options": ["The property's mixed waste container"],
        },
        {
            "name": "Glassware, glassware",
            "options": ["The property's mixed waste container", "Sortti stations"],
        },
        {
            "name": "Window",
            "options": ["The property's mixed waste container", "Sortti stations"],
        },
        {
            "name": "Aquarium, terrarium",
            "options": [
                "Recycling centers and flea markets",
                "The property's mixed waste container",
                "Sortti stations",
            ],
        },
        {
            "name": "Glass brick",
            "options": ["The property's mixed waste container", "Sortti stations"],
        },
        {
            "name": "Mortar",
            "options": [
                "Kivikko hazardous waste reception station",
                "Sortti stations",
                "Sortti containers for hazardous waste",
            ],
        },
        {
            "name": "Ceramics",
            "options": ["The property's mixed waste container", "Sortti stations"],
        },
    ],
    [
        {
            "name": "Spiral folder",
            "options": [
                "Property paper bin",
                "The property's mixed waste container",
                "Rinki eco point",
            ],
        },
        {
            "name": "Office paper, white",
            "options": ["Property paper bin", "Rinki eco point"],
        },
        {"name": "Envelope", "options": ["Property paper bin", "Rinki eco point"]},
        {
            "name": "Poster",
            "options": [
                "Property paper bin",
                "The property's mixed waste container",
                "Rinki eco point",
                "Sortti stations",
            ],
        },
        {"name": "Sketch paper", "options": ["Property paper bin", "Rinki eco point"]},
        {
            "name": "Telephone directory",
            "options": ["Property paper bin", "Rinki eco point", "Sortti stations"],
        },
        {"name": "Business card", "options": ["Property paper bin", "Rinki eco point"]},
        {
            "name": "Magazines, advertisements, brochures",
            "options": ["Property paper bin", "Rinki eco point", "Sortti stations"],
        },
        {"name": "Postcard", "options": ["Property paper bin", "Rinki eco point"]},
        {
            "name": "A scrap of paper",
            "options": ["Property paper bin", "Rinki eco point"],
        },
    ],
    [
        {
            "name": "Aluminum cover, metal cover",
            "options": ["Property's metal collection container", "Rinki eco point"],
        },
        {
            "name": "Knitting needle, crochet hook",
            "options": [
                "Recycling centers and flea markets",
                "Property's metal collection container",
                "The property's mixed waste container",
            ],
        },
        {
            "name": "Grill stick",
            "options": [
                "The property's biowaste container",
                "Property's metal collection container",
                "Rinki eco point",
            ],
        },
        {
            "name": "Disposable grill",
            "options": [
                "Property's metal collection container",
                "The property's mixed waste container",
                "Sortti stations",
                "Sortti collection trucks (for households)",
            ],
        },
        {
            "name": "Key, metal",
            "options": [
                "Property's metal collection container",
                "Rinki eco point",
                "Sortti stations",
                "Sortti collection trucks (for households)",
            ],
        },
        {
            "name": "Lock",
            "options": [
                "Property's metal collection container",
                "Rinki eco point",
                "Sortti stations",
            ],
        },
        {
            "name": "Nail, nut, screw",
            "options": [
                "Property's metal collection container",
                "Rinki eco point",
                "Sortti stations",
                "Sortti collection trucks (for households)",
            ],
        },
        {
            "name": "Lighter, metal",
            "options": [
                "Property's metal collection container",
                "Rinki eco point",
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Sortti containers for hazardous waste",
            ],
        },
        {
            "name": "Coin",
            "options": [
                "Property's metal collection container",
                "Other reception points",
                "Rinki eco point",
            ],
        },
        {
            "name": "Brake pad",
            "options": [
                "Property's metal collection container",
                "Rinki eco point",
                "Sortti stations",
                "Sortti collection trucks (for households)",
            ],
        },
    ],
    [
        {
            "name": "Fabric patch, large",
            "options": [
                "Waste textile collection for households",
                "Waste textile collection for companies",
            ],
        },
        {
            "name": "Clothes, in poor condition",
            "options": [
                "The property's mixed waste container",
                "Waste textile collection for households",
                "Waste textile collection for companies",
            ],
        },
        {
            "name": "Towel",
            "options": [
                "The property's mixed waste container",
                "Waste textile collection for households",
            ],
        },
        {
            "name": "Lumppu, clean",
            "options": [
                "The property's mixed waste container",
                "Waste textile collection for households",
                "Waste textile collection for companies",
            ],
        },
        {
            "name": "Home textiles",
            "options": [
                "The property's mixed waste container",
                "Waste textile collection for households",
            ],
        },
    ],
    [
        {
            "name": "Door",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Sortti stations",
            ],
        },
        {"name": "basket", "options": ["The property's mixed waste container"]},
        {
            "name": "Venetian blind, wood",
            "options": [
                "The property's mixed waste container",
                "Sortti stations",
                "Sortti small station",
            ],
        },
        {
            "name": "Wooden box",
            "options": ["The property's mixed waste container", "Sortti stations"],
        },
        {
            "name": "Wood waste",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Sortti stations",
            ],
        },
        {
            "name": "Frame, wood",
            "options": ["The property's mixed waste container", "Sortti stations"],
        },
        {"name": "Pallet", "options": ["Sortti stations"]},
        {
            "name": "Wooden furniture",
            "options": ["Sortti stations", "Sortti pick-up", "Sortti small station"],
        },
    ],
    [
        {
            "name": "Garden waste",
            "options": [
                "The property's biowaste container",
                "Property composter",
                "Truck loads / Ämmässuo eco-industry center",
                "Sortti stations",
            ],
        },
        {
            "name": "Cone",
            "options": [
                "The property's biowaste container",
                "Property composter",
                "Sortti stations",
            ],
        },
        {"name": "Hay", "options": ["Property composter", "Sortti stations"]},
        {
            "name": "Sawdust",
            "options": [
                "The property's biowaste container",
                "Property composter",
                "The property's mixed waste container",
                "Sortti stations",
            ],
        },
        {
            "name": "Stump, rhizome",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Sortti stations",
            ],
        },
        {
            "name": "Reed, reed",
            "options": [
                "Property composter",
                "Truck loads / Ämmässuo eco-industry center",
                "Sortti stations",
            ],
        },
    ],
    [
        {
            "name": "Construction and demolition waste",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Sortti stations",
            ],
        },
        {
            "name": "Toja disc",
            "options": [
                "Truck loads / Ämmässuo eco-industry center",
                "Sortti stations",
            ],
        },
        {"name": "Vinyl plank", "options": ["Sortti stations"]},
    ],
    [{"name": "Car tire, vehicle tire", "options": ["Other reception points"]}],
    [
        {
            "name": "Branches, twigs, tree trunks",
            "options": [
                "Property composter",
                "Truck loads / Ämmässuo eco-industry center",
                "Sortti stations",
            ],
        },
        {"name": "Christmas tree", "options": ["Sortti stations"]},
    ],
    [
        {
            "name": "Battery - the driving power battery of an electric car",
            "options": ["Other reception points"],
        },
        {"name": "Scrap car", "options": ["Other reception points"]},
        {
            "name": "Scrap vehicle, trailer, moped, etc.",
            "options": ["Other reception points"],
        },
    ],
    [
        {
            "name": "Fabric patch, small",
            "options": ["The property's mixed waste container"],
        },
        {
            "name": "Sex toys",
            "options": [
                "The property's mixed waste container",
                "Other SER reception points",
                "Sortti stations",
                "Shops that sell electrical equipment",
            ],
        },
        {
            "name": "Sleeping platform, sitting platform",
            "options": ["The property's mixed waste container", "Sortti stations"],
        },
        {
            "name": "Club",
            "options": [
                "The point of the recycling center in Jorvak, Kiviko, Konala. At Ruskeasanna and Ämmässuo's Sortti station",
                "Recycling centers and flea markets",
                "The property's mixed waste container",
            ],
        },
        {
            "name": "Blind, plastic",
            "options": [
                "The property's mixed waste container",
                "Sortti stations",
                "Sortti small station",
            ],
        },
        {
            "name": "Venetian blind, wood",
            "options": [
                "The property's mixed waste container",
                "Sortti stations",
                "Sortti small station",
            ],
        },
        {
            "name": "Cooler bag",
            "options": [
                "Recycling centers and flea markets",
                "The property's mixed waste container",
                "Sortti stations",
            ],
        },
        {
            "name": "Knitting needle, crochet hook",
            "options": [
                "Recycling centers and flea markets",
                "Property's metal collection container",
                "The property's mixed waste container",
            ],
        },
        {
            "name": "Wooden box",
            "options": ["The property's mixed waste container", "Sortti stations"],
        },
        {
            "name": "Postcard, self-made",
            "options": ["The property's mixed waste container"],
        },
    ],
    [
        {
            "name": "Hot tub",
            "options": ["Other SER reception points", "Sortti stations"],
        },
        {
            "name": "Mosquito repellent",
            "options": [
                "The property's mixed waste container",
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Sortti containers for hazardous waste",
            ],
        },
        {
            "name": "Fluorescent tube lighter",
            "options": [
                "Other SER reception points",
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Sortti small station",
            ],
        },
        {
            "name": "Electronic cigarette",
            "options": [
                "Other SER reception points",
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Shops that sell electrical equipment",
            ],
        },
        {
            "name": "Hair dryer",
            "options": [
                "Other SER reception points",
                "Sortti stations",
                "Sortti collection trucks (for households)",
            ],
        },
        {
            "name": "Sex toys",
            "options": [
                "The property's mixed waste container",
                "Other SER reception points",
                "Sortti stations",
                "Shops that sell electrical equipment",
            ],
        },
        {
            "name": "A ringing children's book or toy",
            "options": [
                "Other SER reception points",
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Shops that sell electrical equipment",
            ],
        },
        {
            "name": "Electric grill",
            "options": [
                "Other SER reception points",
                "Sortti stations",
                "Sortti collection trucks (for households)",
            ],
        },
        {
            "name": "Electric stove",
            "options": [
                "Other SER reception points",
                "Sortti stations",
                "Sortti collection trucks (for households)",
            ],
        },
        {
            "name": "Electric candle, electric candle holder",
            "options": [
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Shops that sell electrical equipment",
            ],
        },
    ],
    [
        {
            "name": "Mosquito repellent",
            "options": [
                "The property's mixed waste container",
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Sortti containers for hazardous waste",
            ],
        },
        {
            "name": "Ski cream, contains dangerous substances",
            "options": [
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Sortti containers for hazardous waste",
            ],
        },
        {
            "name": "Slaked lime",
            "options": [
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Sortti containers for hazardous waste",
            ],
        },
        {
            "name": "Car wax",
            "options": [
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Sortti containers for hazardous waste",
            ],
        },
        {
            "name": "Waterproofing",
            "options": [
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Sortti containers for hazardous waste",
            ],
        },
        {
            "name": "Resin, from 3D printing",
            "options": [
                "The property's mixed waste container",
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Sortti containers for hazardous waste",
            ],
        },
        {
            "name": "Drain opener, liquid",
            "options": [
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Sortti containers for hazardous waste",
            ],
        },
        {
            "name": "Kaitafilm",
            "options": [
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Sortti containers for hazardous waste",
            ],
        },
        {
            "name": "Nail polish",
            "options": [
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Sortti containers for hazardous waste",
            ],
        },
        {
            "name": "Clutch fluid",
            "options": [
                "Sortti stations",
                "Sortti collection trucks (for households)",
                "Sortti containers for hazardous waste",
            ],
        },
    ],
]

THREADED_HSY_OPTIONS = list(itertools.chain.from_iterable([
    [
        dict(category=m["name"], **x)
        for x in e
    ]
    for m, e in zip(
        HSY_MAIN_TYPES, HSY_OPTIONS
    )
]))