import networkx as nx
import matplotlib.pyplot as plt
from community import detect, visualize, data
import numpy as np

# import the wiki adjaceny dict.
wiki_adj_dict = data.get_wiki_adj()

# Build a community detector object and run the algorithm
detector = detect.CommunityDetector(wiki_adj_dict)
communities = detector.run()
n_communities = len(communities)

# Build a lookup table for node to color.
community_lookup = get_commmunity_lookup(communities)
colors = visualize.discrete_color_scheme(n_communities)

# Get a graph from the adjacency list.
G = visualize.get_graph(wiki_adj_dict)
node_colors = [colors[community_lookup[node]] for node in G.nodes()]

nx.draw(
    G, 
    nx.spring_layout(G, iterations=5000), 
    cmap=plt.get_cmap('jet'), node_color=node_colors, 
    node_size=100
)
