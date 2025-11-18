import grpc
import agriculture_pb2
import agriculture_pb2_grpc

def run():
    channel = grpc.insecure_channel("localhost:50051")
    stub = agriculture_pb2_grpc.AgricultureServiceStub(channel)

    print("\n--- Teste gRPC: ListAll (curto) ---")
    all_products = stub.ListAll(agriculture_pb2.Empty())
    for p in all_products.products[:5]:
        print(f"- {p.name} ({p.category}) → {p.price_per_kg} €/kg")

    print("\n--- Teste gRPC: GetById ---")
    pid = all_products.products[0].id
    prod = stub.GetById(agriculture_pb2.ProductIdRequest(id=pid))
    print(f"{prod.name} ({prod.category}) → {prod.price_per_kg} €/kg")

    print("\n--- Teste gRPC: GetByCategory('Fruits') ---")
    fruits = stub.GetByCategory(agriculture_pb2.CategoryRequest(category="Fruits"))
    for p in fruits.products[:5]:
        print(f"- {p.name}")

    print("\n--- Teste gRPC: XPathQuery ---")
    names = stub.XPathQuery(
        agriculture_pb2.XPathRequest(expression="product/name")
    )
    print("Primeiros 5 resultados:")
    for n in names.results[:5]:
        print("-", n)

if __name__ == "__main__":
    run()
