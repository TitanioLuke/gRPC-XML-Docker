# 🧩 TP2-B – Sistemas Distribuídos  
### *Integração XML-RPC → gRPC com Docker e docker-compose*

Este projeto implementa um sistema distribuído composto por:

1. **Conversão CSV → XML**
2. **Validação XML com XSD**
3. **Servidor XML-RPC** que expõe operações sobre os dados
4. **Servidor gRPC** que consome o XML-RPC e expõe a API moderna
5. **Orquestração com Docker e Docker Compose**

Todo o sistema é modular, validado e executável tanto localmente como em containers.

---

# 📁 Estrutura do Projeto

```
Codigo/
│
├── AgricultureData.csv        
├── agriculture.xml            
├── agriculture.xsd            
│
├── csv_to_xml.py              
├── validate_xml.py            
│
├── xmlrpc_server.py           
├── xmlrpc_client.py           
│
├── grpc/
│   ├── agriculture.proto       
│   ├── agriculture_pb2.py      
│   ├── agriculture_pb2_grpc.py 
│   ├── grpc_server.py          
│   ├── grpc_client.py          
│   ├── Dockerfile.grpc         
│
├── Dockerfile.xmlrpc           
└── docker-compose.yml          
```

---

# 📌 1. Conversão de CSV → XML
```bash
python csv_to_xml.py
```

# 📌 2. Validação XML com XSD
```bash
python validate_xml.py
```

# 📌 3. Servidor XML-RPC
```bash
python xmlrpc_server.py
python xmlrpc_client.py
```

# 📌 4. Servidor gRPC
```bash
cd grpc
python grpc_server.py
python grpc_client.py
```

---

# 🐳 5. Execução com Docker + Docker Compose
```bash
docker compose up --build
```

---

# ✨ Autor
**Afonso Araújo**
