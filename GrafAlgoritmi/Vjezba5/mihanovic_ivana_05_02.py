# -*- coding: utf-8 -*-
"""
Napišite program u kojem se za usmjereni graf ispituje broj komponenti u grafu, 
te veličina najveće komponente. Za testiranje za vrijeme izrade programa možete 
koristiti datoteku football .net, koji možete slobodno modificirati, ili neku 
manju koji sami napravite.
Nakon toga testirajte program za dataset EVA. Dataset EVA je velika mreža telekom i
medijskih kompanija ekstrahirana iz godišnjeg izvještaja U.S. Securities and Exchange
Commission (SEC) u kojoj čvorovi predstavljaju kompanije, a veze vlasništvo jedne
kompanije nad drugom. Mreža ima 8343 čvorova i 6726 veza.
Ispišite prvih deset kompanija i za svaku broj kompanija koje posjeduje.
"""
from collections import defaultdict

def readF(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    adj_list = {}

    in_vertices_section = False
    in_arcs_section = False

    for line in lines:
        line = line.strip()

        if line.startswith('*vertices'):
            in_vertices_section = True
            continue
        elif line.startswith('*arcs'):
            in_vertices_section = False
            in_arcs_section = True
            continue

        if in_vertices_section:
            vertex_id, vertex_name = line.split(' ', 1)
            vertex_id = int(vertex_id)
            vertex_name = vertex_name.strip('"')
            adj_list[vertex_id] = []

        elif in_arcs_section:
            source_id, target_id = map(int, line.split())
            
            adj_list[source_id].append(target_id)

    return adj_list

def readFWeighted(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
    vertices = {}
    adj_list = defaultdict(list)
    mode = None
    for line in lines:
        if line.startswith('*Vertices'):
            mode = 'vertices'
            continue
        elif line.startswith('*Arcs'):
            mode = 'arcs'
            continue
        elif line.startswith('*Edges'):
            continue
        if mode == 'vertices':
            index, name = line.split()
            vertices[int(index)] = name.strip('"')
        elif mode == 'arcs':
            start, end, weight = map(int, line.split())
            adj_list[vertices[start]].append((vertices[end], weight))
    return dict(adj_list)

def pretragaDubina(graph, node, visited):
    if node not in graph:
        return
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            pretragaDubina(graph, neighbor, visited)

def number_of_components(graph):
    visited = set()
    components = 0
    max_component_size = 0
    
    for node in graph:
        if node not in visited:
            components += 1
            current_component_size = len(visited)
            pretragaDubina(graph, node, visited)
            new_component_size = len(visited) - current_component_size
            max_component_size = max(max_component_size, new_component_size)

    vertex_degrees = {node: len(edges) for node, edges in graph.items()}
    top_10_vertices = sorted(vertex_degrees.items(), key=lambda item: item[1], reverse=True)[:10]
    
    return components, max_component_size, top_10_vertices

def main():
    
    g = readF('eva.net.txt')
    komponente, najvecaKomponenta, top10 = number_of_components(g)
    print("EVA:")
    print("Broj komponenti:", komponente,"\nNajveca komponenta:",najvecaKomponenta,"\nTop 10:",top10)
    print()
    
    print("FOOTBALL:")
    g2  = readFWeighted('football.net.txt')
    komponente, najvecaKomponenta, top10 = number_of_components(g2)
    print("Broj komponenti:", komponente,"\nNajveca komponenta:",najvecaKomponenta,"\nTop 10:",top10)
    
if __name__ == '__main__':
    main()
    
