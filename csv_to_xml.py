import csv
import xml.etree.ElementTree as ET

CSV_PATH = "AgricultureData.csv"
XML_PATH = "agriculture.xml"

def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for child in elem:
            indent(child, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

def csv_to_xml(csv_path=CSV_PATH, xml_path=XML_PATH):
    root = ET.Element("agriculture")

    with open(csv_path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            product = ET.SubElement(
                root,
                "product",
                attrib={
                    "id": row["product_id"],
                    "category": row["category"]
                }
            )

            ET.SubElement(product, "name").text = row["product_name"]
            ET.SubElement(product, "price_per_kg").text = row["price_per_kg"]
            ET.SubElement(product, "units_shipped_kg").text = row["units_shipped_kg"]
            ET.SubElement(product, "units_sold_kg").text = row["units_sold_kg"]
            ET.SubElement(product, "units_on_hand_kg").text = row["units_on_hand_kg"]
            ET.SubElement(product, "supplier").text = row["supplier"]
            ET.SubElement(product, "farm_location").text = row["farm_location"]
            ET.SubElement(product, "sale_date").text = row["sale_date"]

    indent(root)

    tree = ET.ElementTree(root)
    tree.write(xml_path, encoding="utf-8", xml_declaration=True)
    print(f"XML formatado e salvo em {xml_path}")

if __name__ == "__main__":
    csv_to_xml()
