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
    plt.title(f"BFS Step: {node}")
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)

    nx.draw_networkx_nodes(G, pos, node_color='lightblue', nodelist=list(set(G.nodes()) - set(visited_nodes)))
    nx.draw_networkx_nodes(G, pos, node_color='lightgreen', nodelist=visited_nodes)

    if frame == len(bfs_queue) - 1:
        all_vertices_reached = set(G.nodes()) == set(bfs_queue)
        if all_vertices_reached:
            plt.title("DFS completo: O grafo é conexo")
        else:
            plt.title("DFS completo: O grafo não é conexo")
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

G = nx.Graph(graph)

pos = nx.spring_layout(G)

bfs_queue = bfs(graph, list(graph.keys())[0])

fig = plt.figure()
ani = animation.FuncAnimation(fig, update_animation, frames=len(bfs_queue), interval=1000)

all_vertices_reached = set(G.nodes()) == set(bfs_queue)
if all_vertices_reached:
    plt.title("DFS completo: O grafo é conexo")
else:
    plt.title("DFS completo: O grafo não é conexo")

plt.show()
