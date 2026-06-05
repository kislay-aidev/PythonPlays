import networkx as nx
import matplotlib.pyplot as plt

# Create a directed graph
G = nx.DiGraph()

# Add weighted edges
edges = [
    ('A', 'B', 4), ('A', 'C', 5),
    ('B', 'D', 9),
    ('C', 'E', 3),
    ('D', 'E', 11),
    ('E', 'F', 6)
]
G.add_weighted_edges_from(edges)

# Compute shortest paths from A
distances, paths = nx.single_source_dijkstra(G, source='A')

# Draw graph
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1500, font_size=12)
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): w for u, v, w in edges})
plt.title("Dijkstra's Shortest Paths from Node A")
plt.show()