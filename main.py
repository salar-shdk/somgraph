import sys
import json
from somgraph import Node, Graph

def main(*args):
    data_file = args[0]
    with open(data_file) as raw_data:
        data = json.loads(raw_data.read())
    graph = Graph(
        node_list=[Node(node['id']) for node in data['graph']['nodes']],
        edge_list=data['graph']['edges']
        )
    print(graph)

if __name__ == '__main__':
    args = sys.argv[1:]
    main(*args)