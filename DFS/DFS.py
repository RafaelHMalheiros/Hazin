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
    node = dfs_stack[frame]
    visited_nodes = dfs_stack[:frame + 1]

    plt.clf()
    plt.title(f"DFS Step: {node}")
    nx.draw_networkx_edges(G, pos)
    nx.draw_networkx_labels(G, pos)

    nx.draw_networkx_nodes(G, pos, node_color='lightblue', nodelist=list(set(G.nodes()) - set(visited_nodes)))
    nx.draw_networkx_nodes(G, pos, node_color='lightgreen', nodelist=visited_nodes)

    if frame == len(dfs_stack) - 1:
        all_vertices_connected = set(G.nodes()) == set(dfs_stack)
        if all_vertices_connected:
            plt.title("DFS completo: O grafo é conexo")
        else:
            plt.title("DFS completo: O grafo não é conexo")
        ani.event_source.stop()

def dfs(graph, start):
    visited = set()
    stack = [start]
    dfs_stack = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            stack.extend(graph[node])
            dfs_stack.append(node)

    return dfs_stack

G = nx.Graph(graph)

pos = nx.spring_layout(G)

dfs_stack = dfs(graph, list(graph.keys())[0])

fig = plt.figure()
ani = animation.FuncAnimation(fig, update_animation, frames=len(dfs_stack), interval=1000)

plt.show()
