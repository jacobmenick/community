import networkx as nx
import matplotlib.pyplot as plt
from community import detect, visualize, data
import numpy as np

wiki_adj_dict = {
               1:  [2,3,10],
               2:  [1,3],
               3:  [1,2],
               4:  [5,6,10],
               5:  [4,6],
               6:  [4,5],
               7:  [8,9,10],
               8:  [7,9],
               9:  [7,8],
               10: [1,4,7],
               }

# what detector.A and detector.S after a phase1 and phase2
A = np.array([[ 4.,  1.,  1.],
            [ 1.,  3.,  0.],
            [ 1.,  0.,  3.]])
S = np.array([[ 1.,  0.,  0.],
        [ 0.,  1.,  0.],
        [ 0.,  0.,  1.]])

# Build a community detector object and run the algorithm
detector = detect.CommunityDetector(wiki_adj_dict)
communities = detector.run()
n_communities = len(communities)

# Build a lookup table for node to color.
community_lookup = {}
for i,c in enumerate(communities):
    for pno in c:
        community_lookup[pno] = i

colors = visualize.discrete_color_scheme(n_communities+1)


# Get a graph from the adjacency list.
G = visualize.get_graph(patent_adj)
node_colors = [colors[community_lookup[node]] for node in G.nodes()]

# Set the ancestor to its own color.
node_colors[G.nodes().index(G.graph['ancestor'])] = colors[n_communities]
nx.draw(G, cmap=plt.get_cmap('jet'), node_color=node_colors)
#
