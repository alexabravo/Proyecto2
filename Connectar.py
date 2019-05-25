from neo4jrestclient.client import GraphDatabase
gdb = GraphDatabase("http://localhost:7474", username="neo4j", password="CristopherBarrios")

def agregarRestaurante(name):
    CadenaDeRestaurantes= gdb.nodes.create(nombre=name)
    CadenaDeRestaurantes.labels.add("CadenaDeRestaurantes")
    
def agregarEstilo(name,costo):
    EstilodeComida= gdb.nodes.create(nombre=name,precio=costo)
    EstilodeComida.labels.add("EstilodeComida")
    
def agregarCliente(name,age):
    Cliente= gdb.nodes.create(nombre=name,edad=age)
    Cliente.labels.add("Cliente")

def agregarPreferencia(name,age):
    Cliente= gdb.nodes.create(nombre=name,edad=age)
    Cliente.labels.add("Cliente")
