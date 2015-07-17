import networkx as nx
import matplotlib.pyplot as plt
from community import detect, visualize, data
from community.util import get_community_lookup

# load data.
patent_adj = data.get_patent_adj()

# Build a community detector object and run the algorithm
detector = detect.CommunityDetector(patent_adj)
communities = detector.run()
n_communities = len(communities)

#Build a lookup table for node to color.
community_lookup = get_community_lookup(communities)
colors = visualize.discrete_color_scheme(n_communities+1)

# Get a graph from the adjacency list.
G = visualize.get_graph(patent_adj)
G.graph['ancestor'] = 4723129
node_colors = [colors[community_lookup[node]] for node in G.nodes()]

# Set the ancestor to its own color.
node_colors[G.nodes().index(G.graph['ancestor'])] = colors[n_communities]
nx.draw(
    G, 
    nx.spring_layout(G, iterations=5000), 
    cmap=plt.get_cmap('jet'), node_color=node_colors, 
    node_size=100
)






