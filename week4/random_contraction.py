#coding=utf8
import copy
import random

def create_graph(lines):
    graph = {}
    for line in lines:
        vertexs = [int(vertex) for vertex in line.split()]
        start_vertex, end_vertexs = vertexs[0], vertexs[1:]
        graph[start_vertex] = end_vertexs
    return graph

def remove_element(l, e):
    while True:
        try:
            l.remove(e)
        except:
            break

def contraction(graph, start_vertex, end_vertex):
    graph[start_vertex].extend(graph[end_vertex])

    # remove self loop
    remove_element(graph[start_vertex], start_vertex)
    remove_element(graph[start_vertex], end_vertex)

    # remove edge from end_vertex -> start_vertex
    remove_element(graph[end_vertex], start_vertex)

    # move edge of end_vertex to start_vertex
    for vertex in graph[end_vertex]:
        graph[vertex].append(start_vertex)
        graph[vertex].remove(end_vertex)
    del graph[end_vertex]

    # if vertex has no edges, remove it
    if not graph[start_vertex]:
        del graph[start_vertex]

def count_edges(graph):
    sum = 0
    for start_vertex, end_vertexs in graph.items():
        sum += len(end_vertexs)
    return int(sum / 2)

def random_contraction(graph):
    init_vertex_count = len(graph)

    for i in range(init_vertex_count-2):
        vertex_count = len(graph)

        # choose random edge
        while True:
            random_start_vertex = random.randrange(1, init_vertex_count+1)
            if random_start_vertex not in graph.keys():
                continue
            break

        edge_count = len(graph[random_start_vertex])
        random_end_vertex = graph[random_start_vertex][random.randrange(0, edge_count)]

        contraction(graph, random_start_vertex, random_end_vertex)

    return count_edges(graph)

if __name__ == '__main__':
    f = open('kargerMinCut.txt', 'r')
    lines = f.readlines()

    graph = create_graph(lines)
    min_cut = 99999 
    for  i in range(1000):
        cut = random_contraction(copy.deepcopy(graph))
        print (i, cut)
        if cut < min_cut:
            min_cut = cut
    print(min_cut)
