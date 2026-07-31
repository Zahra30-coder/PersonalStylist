relationships = [

("product_type_no",
 "Product",
 "ProductType",
 "HAS_TYPE"),

("department_no",
 "Product",
 "Department",
 "BELONGS_TO"),

("section_no",
 "Product",
 "Section",
 "IN_SECTION"),

("garment_group_no",
 "Product",
 "GarmentGroup",
 "HAS_GARMENT_GROUP"),

("colour_group_code",
 "Product",
 "Colour",
 "HAS_COLOUR"),

("perceived_colour_value_id",
 "Product",
 "ColourValue",
 "HAS_COLOUR_VALUE"),

("perceived_colour_master_id",
 "Product",
 "ColourMaster",
 "HAS_COLOUR_MASTER"),

("graphical_appearance_no",
 "Product",
 "GraphicalAppearance",
 "HAS_GRAPHICAL_APPEARANCE"),

("index_code",
 "Product",
 "Index",
 "IN_INDEX")
]