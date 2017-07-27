#coding=utf8
import random

def create_graph(lines):
    graph = {}
    for line in lines:
        vertexs = [int(vertex) for vertex in line.split()]
        start_vertex, end_vertexs = vertexs[0], vertexs[1:]
        graph[start_vertex] = end_vertexs
    return graph

def contraction(graph, start_vertex, end_vertex):
    graph[start_vertex].remove(end_vertex)
    graph[end_vertex].remove(start_vertex)
    graph[start_vertex].extend(graph[end_vertex])
    graph[start_vertex] = list(set(graph[start_vertex]))
    for vertex in graph[end_vertex]:
        if start_vertex not in graph[vertex]:
            graph[vertex].append(start_vertex)
        graph[vertex].remove(end_vertex)
    del graph[end_vertex]
    # if vertex has no edges, remove it
    if not graph[start_vertex]:
        del graph[start_vertex]

def count_edges(graph):
    edges = set()
    for start_vertex, end_vertexs in graph.items():
        for end_vertex in end_vertexs:
            if start_vertex < end_vertex:
                edges.add((start_vertex, end_vertex))
            else:
                edges.add((end_vertex, start_vertex))
    return len(edges)

def random_contraction(graph):
    init_vertex_count = len(graph)

    for i in range(init_vertex_count-2):
        vertex_count = len(graph)
        print 'vertex count: %s' % vertex_count

        # choose random edge
        while True:
            random_start_vertex = random.randrange(1, init_vertex_count+1)
            if random_start_vertex not in graph.keys():
                continue
            break

        edge_count = len(graph[random_start_vertex])
        random_end_vertex = graph[random_start_vertex][random.randrange(0, edge_count)]

        # remove this edge
        print '------------------remove: (%s, %s)' % (random_start_vertex, random_end_vertex)
        contraction(graph, random_start_vertex, random_end_vertex)

    return count_edges(graph)

if __name__ == '__main__':
    f = open('kargerMinCut.txt', 'r')
    lines = f.readlines()
    graph = create_graph(lines)
    print random_contraction(graph)
