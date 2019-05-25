from neo4jrestclient.client import GraphDatabase
gdb = GraphDatabase("http://localhost:7474", username="neo4j", password="CristopherBarrios")

def agregarRestaurante(nombre):
    rest= gdb.nodes.create(name=nombre)
    rest.labels.add("CadenaDeRestaurantes")
