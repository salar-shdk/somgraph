class Node:
    def __init__(self, id, location=(0,0)):
        self.id = id
        self.location = location
    
    def __str__(self):
        return str({'node': self.id})
    
class Graph:
    def __init__(self, node_list={}, edge_list=[]):
        self.node_list = node_list
        self.edge_list = edge_list
    
    def add_node(id, node):
        self.node_list[id] = node
    
    def remove_node(id):
        del self.node_list[id]
        for i, edge in enumerate(edge_list):
            if edge['source'] == id or edge['target'] == id:
                del self.edge_list[i]
    
    def add_edge(*edges):
        self.edge_list += edges
    
    def remove_edge(edge):
        for i, graph_edge in enumerate(edge_list):
            if graph_edge == edge:
                del self.edge_list[i]
    
    def __str__(self):
        return str({
            'nodes': self.node_list,
            'edges': self.edge_list
        })


# Edge value sample:
        # {
		# 	"source": 1,
		# 	"target": 15,
		# 	"weight": 8
		# },
# NOTE: we are not verifying edge values, please ensure they follow the given pattern.