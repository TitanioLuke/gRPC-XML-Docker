import grpc
from concurrent import futures
import xmlrpc.client

import agriculture_pb2
import agriculture_pb2_grpc

# IMPORTANTE: Dentro do Docker, "localhost" NÃO funciona.
# O nome do serviço no docker-compose é "xmlrpc"
XMLRPC_URL = "http://xmlrpc:8000"

# Cliente XML-RPC dentro do Docker
xmlrpc_client = xmlrpc.client.ServerProxy(XMLRPC_URL)

class AgricultureServiceServicer(agriculture_pb2_grpc.AgricultureServiceServicer):

    def ListAll(self, request, context):
        data = xmlrpc_client.list_all()
        products = [agriculture_pb2.Product(**p) for p in data]
        return agriculture_pb2.ProductList(products=products)

    def GetById(self, request, context):
        p = xmlrpc_client.get_by_id(request.id)
        return agriculture_pb2.Product(**p)

    def GetByCategory(self, request, context):
        data = xmlrpc_client.get_by_category(request.category)
        products = [agriculture_pb2.Product(**p) for p in data]
        return agriculture_pb2.ProductList(products=products)

    def XPathQuery(self, request, context):
        results = xmlrpc_client.xpath_query(request.expression)
        return agriculture_pb2.XPathResponse(results=results)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    agriculture_pb2_grpc.add_AgricultureServiceServicer_to_server(
        AgricultureServiceServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    print("Servidor gRPC a correr em localhost:50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
