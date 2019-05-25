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
def recomendar(cliente, clientes,restaurante,restaurantes):
        
    inicioCliente = buscar(cliente,clientes)
    inicioRestaurante = buscar(restaurante,restaurantes)
    
    tamañoCliente = len(clientes)
    tamañoRestaurante = len(restaurantes)

    preferenciasClientes = Preferencias(cliente, clientes)
    preferenciasRestaurantes = Preferencias(restaurante, restaurantes)
    for i in range(0,tamañoCliente):
        com=comun(preferenciasClientes[inicioCliente],preferenciasClientes[i])
    for i in range(0,tamañoRestaurante):
        com=comun(tamañoRestaurante[inicioRestaurante],tamañoRestaurante[i])
    return com


    
    
def buscar(objeto, listaObjeto):
    a=-1
    if objeto in listaObjeto:
        a=listaCliente.index(objeto)
    return a

def Preferencia(name):
    buscar="match (Cliente{nombre:'"+name+"'})-[x]->(d) return x,d"
    resul = gdb.query(buscar, data_contents=True)
    lista = resul.rows
    y=[]
    if lista is not None:
        for x in lista:  
            for i in x: 
                for c in i:
                    if c is not None:
                        y.append(i[c])
    return y

def Preferencias(objeto, listaObjeto):
    y=[]
    for x in listaObjeto:
        a=Preferencia(x)
        if a is not None:
            y.append(a)
    return y

def comun(busca, buscado):
    y=[]
    for x in buscado:
        if x in busca:
            if x not in y:
                y.append(x)
    return y


