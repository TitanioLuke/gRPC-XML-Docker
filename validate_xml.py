from lxml import etree

XML_FILE = "agriculture.xml"
XSD_FILE = "agriculture.xsd"

def validate_xml():
    # carregar XML e XSD
    xml_doc = etree.parse(XML_FILE)
    xsd_doc = etree.parse(XSD_FILE)

    schema = etree.XMLSchema(xsd_doc)

    if schema.validate(xml_doc):
        print("XML válido segundo o XSD!")
    else:
        print("XML inválido!")
        print("\nErros encontrados:")
        for error in schema.error_log:
            print(" -", error.message)

if __name__ == "__main__":
    validate_xml()
