import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx
from collections import deque

num_vertices = int(input("Digite o número de vertices: "))
num_edges = int(input("Digite o número de arestas: "))

graph = {}

print("Diga os as arestas no seguinte formato (u v):")
for _ in range(num_edges):
    u, v = input().split()
    if u not in graph:
        graph[u] = []
    if v not in graph:
        graph[v] = []
    graph[u].append(v)
    graph[v].append(u)

for vertex in range(1, num_vertices + 1):
    if str(vertex) not in graph:
        graph[str(vertex)] = []

def update_animation(frame):
    node = bfs_queue[frame]
    visited_nodes = bfs_queue[:frame + 1]

    plt.clf()
    plt.title(f"ARTICULATION POINT Step: {node}")
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)

    nx.draw_networkx_nodes(G, pos, node_color='lightblue', nodelist=list(set(G.nodes()) - set(visited_nodes)))
    nx.draw_networkx_nodes(G, pos, node_color='lightgreen', nodelist=visited_nodes)

    if frame == len(bfs_queue) - 1:
        all_vertices_reached = set(G.nodes()) == set(bfs_queue)
        if all_vertices_reached:
            plt.title("ARTICULATION POINT completo: O grafo é conexo")
        else:
            plt.title("ARTICULATION POINT completo: O grafo não é conexo")
        ani.event_source.stop()

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    bfs_queue = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            queue.extend(graph[node])
            bfs_queue.append(node)

    return bfs_queue

def find_articulation_points(graph):
    visited = set()
    parent = {node: None for node in graph}
    disc = {}
    low = {}
    articulation_points = set()

    def ap_util(node):
        nonlocal articulation_points
        visited.add(node)
        disc[node] = ap_util.time
        low[node] = ap_util.time
        ap_util.time += 1

        children = 0

        for neighbor in graph[node]:
            if neighbor not in visited:
                children += 1
                parent[neighbor] = node
                ap_util(neighbor)

                low[node] = min(low[node], low[neighbor])

                if parent[node] is None and children > 1:
                    articulation_points.add(node)
                if parent[node] is not None and low[neighbor] >= disc[node]:
                    articulation_points.add(node)

            elif neighbor != parent[node]:
                low[node] = min(low[node], disc[neighbor])

    ap_util.time = 0

    for vertex in graph:
        if vertex not in visited:
            ap_util(vertex)

    return articulation_points

G = nx.Graph(graph)
pos = nx.spring_layout(G)

articulation_points = find_articulation_points(graph)

print("Articulation Points:")
for vertex in articulation_points:
    print(vertex)

start_vertex = list(graph.keys())[0]
bfs_queue = bfs(graph, start_vertex)

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update_animation, frames=len(bfs_queue), interval=1000, repeat=False)

plt.show()
