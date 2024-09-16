import math
import os
from queue import PriorityQueue
from Graph import *

class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph="./MarsMap",
                 prev_state=None, g=0,h=0):
        self.location = location
        self.mars_graph = read_mars_graph(mars_graph)
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


## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0


## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    if not state.location:
        print("Error: Location is empty or None.")
        return -1
    x, y = map(int, state.location.split(','))
    return math.sqrt((x - 1)**2 + (y - 1)**2)


def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    state_count = 0
    search_queue.put(start_state)

    while not search_queue.empty():
        current_state = search_queue.get()
        state_count += 1

        if goal_test(current_state):
            print("Goal found")
            print(f"Number of states generated: {state_count}")
            return current_state

        if use_closed_list:
            closed_list[current_state] = current_state

        # explore neighbors
        # print("current loc:", current_state.location)
        for neighbor in current_state.mars_graph.get_edges(current_state.location):
            new_state = map_state(location=neighbor.dest, prev_state=current_state)
            new_state.g = current_state.g + 1
            new_state.h = heuristic_fn(new_state)
            new_state.f = new_state.g + new_state.h
            # print("f:", new_state.f)

            if use_closed_list and new_state in closed_list:
                continue

            search_queue.put(new_state)

    print("No goal found")
    print(f"Number of states generated: {state_count}")
    return None


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
                    # print("node part:", node_part)
                    graph.add_node(node_part)

                # add edges
                edges = edges_part.split()
                # print("edges:")
                for edge_part in edges:
                    # print(edge_part)
                    graph.add_edge(Edge(src=node_part, dest=edge_part))

    return graph

def routefinder_submission():
    print("* routefinder_submission *\n")
    print("sld heuristic")
    s1 = map_state(location="8,8")
    s1.h = sld(s1)
    s1.f = s1.h
    s1 = a_star(s1, sld, map_state.is_goal)
    print("\nh1 heuristic")
    s2 = map_state(location="8,8")
    s2.h = h1(s2)
    s2.f = s2.h
    s2 = a_star(s2, h1, map_state.is_goal)
    print("---\n")
