import matplotlib.pyplot as plt
import matplotlib.animation as animation
import networkx as nx


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
    edge = bfs_queue[frame]
    visited_edges = bfs_queue[:frame + 1]

    plt.clf()
    plt.title(f"Union-Find Step: {edge}")
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)

    visited_nodes = list(set().union(*visited_edges))

    nx.draw_networkx_nodes(G, pos, node_color='lightblue', nodelist=list(set(G.nodes()) - set(visited_nodes)))
    nx.draw_networkx_nodes(G, pos, node_color='lightgreen', nodelist=visited_nodes)

    if frame == len(bfs_queue) - 1:
        all_vertices_reached = set(G.nodes()) == set().union(*bfs_queue)
        if all_vertices_reached:
            plt.title("Union-Find completo: O grafo é conexo")
        else:
            plt.title("Union-Find completo: O grafo não é conexo")
        ani.event_source.stop()


def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def union_find(graph):
    vertices = list(graph.keys())

    parent = {}
    rank = {}

    for v in vertices:
        parent[v] = v
        rank[v] = 0

    bfs_queue = []

    for u in graph:
        for v in graph[u]:
            u_root = find(parent, u)
            v_root = find(parent, v)
            if u_root != v_root:
                union(parent, rank, u_root, v_root)
                bfs_queue.append((u, v))

    return bfs_queue

G = nx.Graph(graph)

pos = nx.spring_layout(G)

bfs_queue = union_find(graph)

fig = plt.figure()
ani = animation.FuncAnimation(fig, update_animation, frames=len(bfs_queue), interval=1000)

all_vertices_reached = set(G.nodes()) == set(bfs_queue)
if all_vertices_reached:
    plt.title("Union-Find completo: O grafo é conexo")
else:
    plt.title("Union-Find completo: O grafo não é conexo")

plt.show()
