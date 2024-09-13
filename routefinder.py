import os
from Graph import *

class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'


## you implement this. Open the file filename, read in each line,
## construct a Graph object and assign it to self.mars_graph().
def read_mars_graph(filename):
    graph = Graph()

    if os.path.exists(filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                # parse line
                node_part, edges_part = line.split(':')
                node_part = node_part.strip()
                edges_part = edges_part.strip()

                # add node to graph
                if node_part not in graph.g:
                    graph.add_node(node_part)

                # add edges
                edges = edges_part.split()
                for edge_part in edges:
                    edge = Edge(src=node_part, dest=edge_part)
                    graph.add_edge(edge)

    return graph
