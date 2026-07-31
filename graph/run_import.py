from app.graph.sql_reader import read_table
from app.graph.neo4j_connection import get_driver
from app.graph.import_nodes import import_nodes

driver = get_driver()

TABLES = [

    ("Products","Product","article_id"),

    ("Departments","Department","department_no"),

    ("ProductTypes","ProductType","product_type_no"),

    ("Sections","Section","section_no"),

    ("GarmentGroups","GarmentGroup","garment_group_no"),

    ("Colours","Colour","colour_group_code"),

    ("ColourValues","ColourValue","perceived_colour_value_id"),

    ("ColourMasters","ColourMaster","perceived_colour_master_id"),

    ("Indices","Index","index_code"),

    ("IndexGroups","IndexGroup","index_group_no"),

    ("GraphicalAppearances",
     "GraphicalAppearance",
     "graphical_appearance_no")
]

for table,label,pk in TABLES:

    df = read_table(table)

    import_nodes(driver,label,pk,df)

driver.close()