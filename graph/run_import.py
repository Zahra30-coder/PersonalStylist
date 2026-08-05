'''
from sql_reader import read_table
from test_neo4j import get_driver
from import_nodes import import_nodes
'''
from .sql_reader import read_table
from .test_neo4j import get_driver
from .import_nodes import import_nodes


driver = get_driver()
total = 0
TABLES = [

    ("Products","Product","article_id"),
    ("departments","departments","department_no"),
    ("ProductTypes","ProductTypes","product_type_no"),
    ("Appearances","Appearances","graphical_appearance_no"),
    ("Sections","Sections","section_no"),
    ("GarmentGroups","GarmentGroup","garment_group_no"),
    ("Colors","Colors","colour_group_code"),
    ("ColorValues","ColorValues","perceived_colour_value_id"),
    ("ColorMasters","ColorMasters","perceived_colour_master_id"),
    ("Indices","Indices","index_code"),
    ("IndexGroup","IndexGroup","index_group_no")
]

for table,label,pk in TABLES:

    df = read_table(table)
    total += import_nodes(driver,label,pk,df)
    print(f"\nTotal nodes imported: {total}")

driver.close()