import pydot

# crear el objeto de grafo
graph = pydot.Dot(graph_type='digraph')

# agregar los nodos
start_node = pydot.Node('Inicio')
room_node = pydot.Node('¿Estoy en el cuarto?')
bulb_node = pydot.Node('¿La bombilla está apagada?')
lighter_node = pydot.Node('¿Tengo un encendedor?')
action_node = pydot.Node('Accionar el encendedor')
check_node = pydot.Node('¿La bombilla se encendió?')
end_node = pydot.Node('Fin')

# agregar nodos de decision
room_decision = pydot.Node('Decision', shape='diamond', label='¿Estoy en el cuarto?')
bulb_decision = pydot.Node('Decision', shape='diamond', label='¿La bombilla está apagada?')
lighter_decision = pydot.Node('Decision', shape='diamond', label='¿Tengo un encendedor?')

# agregar los nodos al grafo
graph.add_node(start_node)
graph.add_node(room_node)
graph.add_node(bulb_node)
graph.add_node(lighter_node)
graph.add_node(action_node)
graph.add_node(check_node)
graph.add_node(end_node)

# agregar nodos de decision al grafo
graph.add_node(room_decision)
graph.add_node(bulb_decision)
graph.add_node(lighter_decision)

# agregar relaciones
graph.add_edge(pydot.Edge(start_node, room_decision))
graph.add_edge(pydot.Edge(room_decision, bulb_decision, label='Si'))
graph.add_edge(pydot.Edge(bulb_decision, lighter_decision, label='Si'))
graph.add_edge(pydot.Edge(lighter_decision, action_node, label='Si'))
graph.add_edge(pydot.Edge(action_node, check_node))
graph.add_edge(pydot.Edge(check_node, end_node, label='Si'))
graph.add_edge(pydot.Edge(room_decision, end_node, label='No'))
graph.add_edge(pydot.Edge(bulb_decision, end_node, label='No'))
graph.add_edge(pydot.Edge(lighter_decision, end_node, label='No'))

# guardar y mostrar el grafo
graph.write_png('diagrama.png')
