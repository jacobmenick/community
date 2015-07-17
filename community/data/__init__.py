import os
import numpy as np
# import cPickle

_this_dir = os.path.dirname(os.path.realpath(__file__))
_patent_subset = '/'.join([_this_dir, 'adj.p'])

def get_patent_adj():
    return np.load(_patent_subset, mmap_mode='r')

def get_wiki_adj():
    return {
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

# def pickle_save(filename, obj):
#     with open(filename, 'wb') as outfile:
#         cPickle.dump(obj, outfile)
