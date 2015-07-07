# visualize communities detected. 

import networkx as nx
import numpy as np

_adj_dict = np.load('alex_adj.p', mmap_mode='r')
# get only unique values (oops!)
_adj_dict = {k:list(set(v)) for k,v in _adj_dict.items()}
_pats = sorted(list(set(_adj_dict.keys()+
                        [x for xs in list(_adj_dict.values()) for x in xs]
                    )))

def get_graph(adj_dict):
    # get unique set of nodes
    G = nx.Graph()
    G.add_nodes_from(sorted(list(set(
        adj_dict.keys()+
        [x for xs in list(adj_dict.values()) for x in xs]
    ))))
    for parent,children in adj_dict.items():
        for child in children:
            G.add_edge(parent,child)
    return G
    
    

