import numpy as np
# Utilities for community detection

def _is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        return False

def make_diagonal(n, entries = 1):
    """ makes a diagonal matrix with the specified entry on the diagonal(s)."""
    A = np.zeros((n,n))
    if _is_number(entries):
        diags = [entries for _ in range(n)]
    else:
        assert(len(entries) == n)
        diags = entries
    for i in range(n):
        A[i,i] = diags[i]

def adj_dict_to_adj_mat(adj_dict, directed=False):
    """ Convert an adjacency list representation of a graph
    to a dense adjacency matrix representation. If directed
    is false, the adjacency matrix is symmetric.
    """
    nodes = adj_dict.keys()
    A = np.zeros((len(nodes), len(nodes)))
    for i, _ in enumerate(A):
        for j in range(i+1):
            node1 = nodes[i]
            node2 = nodes[j]
            flag = False
            if node1 in adj_dict and node2 in adj_dict[node1]:
                flag = True
            elif node2 in adj_dict and node1 in adj_dict[node2]:
                flag = True
            if not directed:
                A[i,j] = A[j,i] = 1 if flag else 0
            else:
                A[i,j] = 1 if flag else 0
    return A

def modularity(A, S):
    """
    computes modularity, Q, where Q = 1/2m * Tr(S^t B S)
    """
    B = get_B(A)
    num_stubs = np.sum(A)*2
    return float(1 / num_stubs) * np.trace(np.dot(np.transpose(S), np.dot(B,S)))

def get_B(A):
    """
    make B, the modularity matrix, which has dimensions num_nodes by num_nodes.
    B[i,j] = A[i,j] - ((k_i * k_j) / (2m))
    where m is the number of edges (2m = num_stubs)
    and where A is adjacency matrix and k_i is degree.
    """

    def edge_deg(node_idx):
        return np.sum(A[node_idx])

    num_stubs = np.sum(A)*2
    num_nodes = A.shape[0]
    B = np.zeros((num_nodes, num_nodes))
    for i, row in enumerate(B):
        for j in range(i+1):
            B[i,j] = B[j,i] = A[i,j] - float((edge_deg(i) * edge_deg(j)) / (num_stubs))
    return B
