from neo4jrestclient.client import GraphDatabase
gdb = GraphDatabase("http://localhost:7474", username="neo4j", password="CristopherBarrios")

def agregarRestaurante(name):
    CadenaDeRestaurantes= gdb.nodes.create(nombre=name)
    CadenaDeRestaurantes.labels.add("CadenaDeRestaurantes")
