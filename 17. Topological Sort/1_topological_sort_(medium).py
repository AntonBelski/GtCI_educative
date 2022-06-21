from collections import defaultdict
from queue import Queue


def topological_sort(vertices, edges):
    free_courses = Queue()
    graph = defaultdict(list)
    inc_degrees = [0] * vertices
    top_sort = []

    for p in edges:
        graph[p[0]].append(p[1])
        inc_degrees[p[1]] += 1

    for node, req in enumerate(inc_degrees):
        if req == 0:
            free_courses.put(node)

    while not free_courses.empty():
        node = free_courses.get()
        top_sort.append(node)

        for node_to in graph[node]:
            inc_degrees[node_to] -= 1
            if inc_degrees[node_to] == 0:
                free_courses.put(node_to)

    if len(top_sort) == vertices:
        return top_sort
    else:
        return -1


def main():
    print("Topological sort: " + str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " + str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
