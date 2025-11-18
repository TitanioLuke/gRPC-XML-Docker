import xmlrpc.client

client = xmlrpc.client.ServerProxy("http://localhost:8000")

print("\n---------------------------")
print(" TESTE 1 — list_all()")
print("---------------------------")

products = client.list_all()

print(f"\nTotal de produtos: {len(products)}\n")

# Mostrar só 5 produtos resumidos
for p in products[:5]:
    print(f"- {p['name']} ({p['category']}) → {p['price_per_kg']} €/kg")

print("\n(… restantes omitidos …)\n")


print("\n---------------------------")
print(" TESTE 2 — get_by_id()")
print("---------------------------")

# usa o primeiro ID do XML
first_id = products[0]["id"]
prod = client.get_by_id(first_id)

print(f"\nProduto com ID {first_id}:")
print(f"Nome: {prod['name']}")
print(f"Categoria: {prod['category']}")
print(f"Preço/kg: {prod['price_per_kg']}\n")


print("\n---------------------------")
print(" TESTE 3 — get_by_category('Fruits')")
print("---------------------------")

fruits = client.get_by_category("Fruits")

print(f"\nTotal de produtos da categoria 'Fruits': {len(fruits)}\n")

for p in fruits[:5]:  # Mostra só 5
    print(f"- {p['name']} → {p['price_per_kg']} €/kg")

print("\n(… restantes omitidos …)\n")


print("\n---------------------------")
print(" TESTE 4 — xpath_query()")
print("---------------------------")

# Consulta XPath: obter todos os nomes de produtos
names = client.xpath_query("product/name")

print(f"\nPrimeiros 5 nomes de produtos via XPath:\n")

for n in names[:5]:
    print("-", n)

print("\n(… restantes omitidos …)\n")
