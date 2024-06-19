# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 13:51:43 2024

@author: IvanaMihanović
"""

import networkx as nx
import matplotlib.pyplot as plt
import heapq
import numpy as np

vertices = {}
def read_pajek(file_path):
    G = nx.DiGraph()
    with open(file_path, 'r') as file:
        lines = file.readlines()
        arcs_section = False
        vertices_section = False
        for line in lines:
            if '*vertices' in line:
                vertices_section = True
                continue
            if '*arcs' in line:
                arcs_section = True
                vertices_section = False
                continue
            if vertices_section:
                linija = line.split()
                vertices[int(linija[0])]=(int(linija[2]),int(linija[3]))
            if arcs_section and line.strip():
                source, target, weight = map(int, line.strip().split())
                G.add_edge(source, target, weight=weight)
    return G

# Dijkstra
def dijkstraAlgorithm(graph, source):
    return nx.single_source_dijkstra_path_length(graph, source)

# Bellman-Ford
def bellmanFordAlgorithm(graph, source):
    return nx.single_source_bellman_ford_path_length(graph, source)

# Greedy BFS
def greedyBfs(graph, source, target):
    visited = set()
    queue = [(source, [source])]
    
    def heuristic(graph, node1, node2):
        dist = np.sqrt((vertices[node1][0]-vertices[node2][0])**2+(vertices[node1][1]-vertices[node2][1])**2)
        return dist
    
    while queue:
        current_node, shortest_path = queue.pop(0)
        
        if current_node == target:
            return shortest_path
        
        if current_node not in visited:
            visited.add(current_node)
            neighbors = list(graph.neighbors(current_node))
            
            neighbors.sort(key=lambda neighbor: heuristic(graph, current_node, neighbor))
            
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append((neighbor, shortest_path + [neighbor]))
    return None

# A*
def aStarAlgorithm(graph, source, target):
    return nx.astar_path(graph, source=source, target=target, heuristic=None, weight="weight")

# SLIKA GRAFA
def graphDraw(graph):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_weight='bold', node_size=700)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()
    

if __name__ == "__main__":
    
    file_path = "graph-airports-koord.net.txt"
    G = read_pajek(file_path)
    graphDraw(G)

    source = 1
    #DIJKSTRA
    print("Dijkstra od cvora ", source, ": ",dijkstraAlgorithm(G, source))
    print()
    #Bellman-Ford
    print("Bellman-Ford od cvora", source, ": ",bellmanFordAlgorithm(G, source))
    print()
    #Greedy BFS
    destinationGreedy = 8
    print("Greedy BFS od vrha", source, "do vrha ", destinationGreedy,": ",greedyBfs(G, source, destinationGreedy))
    print()
    # A* 
    destinationAstar = 8
    print("A* od vrha", source, "do vrha ", destinationAstar,": ", aStarAlgorithm(G, source, destinationAstar))
