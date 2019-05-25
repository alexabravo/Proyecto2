#Cristopher Barrios 18207
#Documentacion https://neo4j-rest-client.readthedocs.io/en/latest/
from neo4jrestclient.client import GraphDatabase
gdb = GraphDatabase("http://localhost:7474", username="neo4j", password="CristopherBarrios")


#insertando
def agregarRestaurante(name):
    CadenaDeRestaurantes= gdb.nodes.create(nombre=name)
    CadenaDeRestaurantes.labels.add("CadenaDeRestaurantes")

def agregarCliente(name,age):
    Cliente= gdb.nodes.create(nombre=name,edad=age)
    Cliente.labels.add("Cliente")
    
def agregarEstilo(name,costo):
    EstilodeComida= gdb.nodes.create(nombre=name,precio=costo)
    EstilodeComida.labels.add("EstilodeComida")
    
def agregarPreferencia(name):
    PreferenciaComida= gdb.nodes.create(nombre=name)
    PreferenciaComida.labels.add("PreferenciaComida")

#Relaciones
def clientePreferencia (name, preferencia):
    Cliente= gdb.labels.get("Cliente")
    Cliente.all()
    PreferenciaComida=gdb.labels.get("PreferenciaComida")
    PreferenciaComida.all()
    Cliente.get(nombre=name)[0].relationships.create("prefiere",PreferenciaComida.get(nombre=preferencia)[0])

def clienteEstilo (name, estilo):
    Cliente= gdb.labels.get("Cliente")
    Cliente.all()
    EstilodeComida=gdb.labels.get("EstilodeComida")
    EstilodeComida.all()
    Cliente.get(nombre=name)[0].relationships.create("prefiere",EstilodeComida.get(nombre=estilo)[0])
    
def restaurantePreferencia (name, preferencia):
    CadenaDeRestaurantes= gdb.labels.get("CadenaDeRestaurantes")
    CadenaDeRestaurantes.all()
    PreferenciaComida=gdb.labels.get("PreferenciaComida")
    PreferenciaComida.all()
    CadenaDeRestaurantes.get(nombre=name)[0].relationships.create("pertenece",PreferenciaComida.get(nombre=preferencia)[0])
    
def restauranteEstilo (name, estilo):
    CadenaDeRestaurantes= gdb.labels.get("CadenaDeRestaurantes")
    CadenaDeRestaurantes.all()
    EstilodeComida=gdb.labels.get("EstilodeComida")
    EstilodeComida.all()
    CadenaDeRestaurantes.get(nombre=name)[0].relationships.create("petenece",EstilodeComida.get(nombre=estilo)[0])
    

#Fuciones para logaritmo
def buscaruno(cliente, listaCliente):
    a=-1
    if cliente in listaCliente:
        a=listaCliente.index(cliente)
    return a
