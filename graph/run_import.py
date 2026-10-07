'''
from sql_reader import read_table
from test_neo4j import get_driver
from import_nodes import import_nodes
'''
from .sql_reader import read_table
from .test_neo4j import get_driver
from .import_nodes import import_nodes
from .import_relationships import import_relationships
from database.db import get_connection

conn = get_connection()

IMPORT_NODES = False
IMPORT_RELATIONSHIPS = True

driver = get_driver()

# --------------        IMPORT NODES     -----------------------
if IMPORT_NODES:
    total = 0
    TABLES = [
        ("Products","Products","article_id"),
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

    try:
        for table, label, pk in TABLES:
            df = read_table(conn, table)
            total += import_nodes(driver, label, pk, df)
            print(f"\nTotal nodes imported: {total}")

    finally:
        conn.close()

# --------------        IMPORT RELATIONSHIPS     ----------------------

if IMPORT_RELATIONSHIPS:

    print("\nReading Products table...")
    conn = get_connection()
    products = read_table(conn,"Products")

    RELATIONSHIPS = [

        (
            "Products",
            "article_id",
            "ProductType",
            "product_type_no",
            "product_type_no",
            "HAS_TYPE"
        ),

        (
            "Product",
            "article_id",
            "Department",
            "department_no",
            "department_no",
            "BELONGS_TO"
        ),

        (
            "Product",
            "article_id",
            "Section",
            "section_no",
            "section_no",
            "IN_SECTION"
        ),

        (
            "Product",
            "article_id",
            "GarmentGroup",
            "garment_group_no",
            "garment_group_no",
            "IN_GARMENT_GROUP"
        ),

        (
            "Product",
            "article_id",
            "Colour",
            "colour_group_code",
            "colour_group_code",
            "HAS_COLOUR"
        ),

        (
            "Product",
            "article_id",
            "ColourValue",
            "perceived_colour_value_id",
            "perceived_colour_value_id",
            "HAS_COLOUR_VALUE"
        ),

        (
            "Product",
            "article_id",
            "ColourMaster",
            "perceived_colour_master_id",
            "perceived_colour_master_id",
            "HAS_COLOUR_MASTER"
        ),

        (
            "Product",
            "article_id",
            "Index",
            "index_code",
            "index_code",
            "IN_INDEX"
        ),

        (
            "Product",
            "article_id",
            "IndexGroup",
            "index_group_no",
            "index_group_no",
            "IN_INDEX_GROUP"
        ),

        (
            "Product",
            "article_id",
            "GraphicalAppearance",
            "graphical_appearance_no",
            "graphical_appearance_no",
            "HAS_APPEARANCE"
        )
    ]

    relationship_total = 0

    for (
        source_label,
        source_key,
        target_label,
        target_key,
        fk_column,
        relationship
    ) in RELATIONSHIPS:

        relationship_total += import_relationships(
            driver=driver,
            dataframe=products,
            source_label=source_label,
            source_key=source_key,
            target_label=target_label,
            target_key=target_key,
            fk_column=fk_column,
            relationship=relationship,
        )

    print(f"\nTotal relationships imported: {relationship_total}")

driver.close()