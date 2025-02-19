import math
import random


N = 100_000
M = 500_000


def random_dag(nodes, k):
    edges = []
    available_parents = []
    for node in nodes:
        parents = random.choices(available_parents, k=min(k, len(available_parents)))
        for p in parents:
            edges.append((p, node))
        available_parents.append(node)
    return edges


# Very wide but narrow graph
with open("wide.in", "w") as f:
    source = 0
    sink = N - 1
    print(N, 2 * (N - 2), file=f)
    for i in range(N):
        print(i % 100, file=f)
    for i in range(1, N - 1):
        print(0, i, file=f)
        print(i, N - 1, file=f)

# Dense graph, lots of sinks
with open("dense.in", "w") as f:
    source = 0
    sink_count = 500
    choke_point = N - sink_count - 1
    edges = []
    for i in range(sink_count):
        sink = N - 1 - i
        edges.append((choke_point, sink))

    random_edges = random_dag(list(range(0, choke_point + 1)), 5)
    edges.extend(random_edges)
    # print(N, 2 * (N - 2), file=f)
    print(N, len(edges), file=f)
    for i in range(N):
        print(i % 100, file=f)
    for ai, bi in edges:
        print(ai, bi, file=f)


# Random
# with open("random.in", "w") as f:
#     print(N, M, file=f)
#     for i in range(N):
#         print(i % 100, file=f)
#     for i in range(M):
#         print(0, i, file=f)
#         print(i, N - 1, file=f)
