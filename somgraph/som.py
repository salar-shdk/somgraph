import math
import matplotlib.pyplot as plt
from . import Graph

class Som:
    def __init__(self, graph):
        self.graph = graph
    
    def _get_columns_and_rows(self, env_range):
        node_count, _ = self.graph.count()
        (min_x, max_x), (min_y, max_y) = env_range
        ratio = (max_x - min_x) / (max_y - min_y)
        columns = math.ceil(math.sqrt(node_count)) * ratio
        columns = math.floor(columns) if (columns % int(columns)) < 0.5 else math.ceil(columns)
        return columns, math.ceil(node_count/columns)

    def initialize_locations(self, env_range=((-1, 1), (-1, 1))):
        (min_x, max_x), (min_y, max_y) = env_range
        
        columns, rows = self._get_columns_and_rows(env_range)
        diff_y = (max_y - min_y) / (rows + 1)
        diff_x = (max_x - min_x) / (columns + 1)
        counter = 1
        for y in (min_y + (i * diff_y) for i in range(1, rows + 1)):
            for x in (min_x + (i * diff_x) for i in range(1, columns + 1)):
                if counter <= len(self.graph.node_list):                    
                    self.graph.node_list[counter].location = (x, y)
                    counter += 1

    def update_graph(self, move_ratio, weight_effect, reverse = False):
        for edge in self.graph.edge_list:
            source = self.graph.node_list[edge['source']]
            target = self.graph.node_list[edge['target']]
            weight = edge['weight'] if weight_effect else 1
            source.location = (
                source.location[0] + (target.location[0] - source.location[0]) * move_ratio * weight * (-1 if reverse else 1),
                source.location[1] + (target.location[1] - source.location[1]) * move_ratio * weight * (-1 if reverse else 1))
            target.location = (
                target.location[0] + (source.location[0] - target.location[0]) * move_ratio * weight * (-1 if reverse else 1),
                target.location[1] + (source.location[1] - target.location[1]) * move_ratio * weight * (-1 if reverse else 1))


    def start(self, epochs, move_ratio = 0.05, weight_effect = False):
        self.show()
        for epoch in range(epochs):
            self.update_graph(move_ratio, weight_effect)
            self.show()
        self.show(dynamic=False)

    def show(self, dynamic=True):
        plt.cla()
        plt.scatter([node.location[0] for node in self.graph.node_list.values()] , [node.location[1] for node in self.graph.node_list.values()])
        for edge in self.graph.edge_list:
            plt.plot((self.graph.node_list[edge['source']].location[0], self.graph.node_list[edge['target']].location[0]),
                (self.graph.node_list[edge['source']].location[1], self.graph.node_list[edge['target']].location[1]))
        
        if dynamic:
            plt.draw()
            plt.pause(0.001)
        else:
            plt.show()