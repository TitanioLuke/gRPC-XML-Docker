from xmlrpc.server import SimpleXMLRPCServer
from lxml import etree

XML_FILE = "agriculture.xml"

#Carrega XML
xml_doc = etree.parse(XML_FILE)
root = xml_doc.getroot()

def product_to_dict(p):
    #Converte um elemento <product> em dicionário
    return {
        "id": p.get("id"),
        "category": p.get("category"),
        "name": p.findtext("name"),
        "price_per_kg": float(p.findtext("price_per_kg")),
        "units_shipped_kg": int(p.findtext("units_shipped_kg")),
        "units_sold_kg": int(p.findtext("units_sold_kg")),
        "units_on_hand_kg": int(p.findtext("units_on_hand_kg")),
        "supplier": p.findtext("supplier"),
        "farm_location": p.findtext("farm_location"),
        "sale_date": p.findtext("sale_date"),
    }

def list_all():
    #Lista todos os produtos
    return [product_to_dict(p) for p in root.findall("product")]

def get_by_id(product_id):
    #Retorna um produto pelo ID
    p = root.find(f"product[@id='{product_id}']")
    return product_to_dict(p) if p is not None else {}

def get_by_category(category):
    #Busca produtos pela categoria
    products = root.xpath(f"product[@category='{category}']")
    return [product_to_dict(p) for p in products]

def xpath_query(expr):
    #Executa XPath arbitrário
    results = root.xpath(expr)
    output = []

    for r in results:
        if isinstance(r, etree._Element):
            output.append(etree.tostring(r, encoding="unicode"))
        else:
            output.append(str(r))

    return output

def run_server():
    with SimpleXMLRPCServer(("0.0.0.0", 8000), allow_none=True) as server:
        print("Servidor XML-RPC rodando em http://localhost:8000 ...")
        server.register_function(list_all, "list_all")
        server.register_function(get_by_id, "get_by_id")
        server.register_function(get_by_category, "get_by_category")
        server.register_function(xpath_query, "xpath_query")
        server.serve_forever()

if __name__ == "__main__":
    run_server()
