from collections import defaultdict


def is_scheduling_possible(tasks, prerequisites):
    free_courses = []
    graph = defaultdict(list)
    inc_degrees = [0] * tasks
    top_sort = []

    for p in prerequisites:
        graph[p[1]].append(p[0])
        inc_degrees[p[0]] += 1

    for node, req in enumerate(inc_degrees):
        if req == 0:
            free_courses.append(node)

    while free_courses:
        node = free_courses.pop()
        top_sort.append(node)

        for node_to in graph[node]:
            inc_degrees[node_to] -= 1
            if inc_degrees[node_to] == 0:
                free_courses.append(node_to)

    if len(top_sort) == tasks:
        return True
    else:
        return False


def main():
    print("Is scheduling possible: " + str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " + str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " + str(is_scheduling_possible(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])))


main()
