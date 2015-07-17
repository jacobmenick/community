import unittest
import numpy as np
from community.util import adj_dict_to_adj_mat, modularity, get_B, make_diagonal
from community.data import get_patent_adj
from community.detect import CommunityDetector

# global vars - toy examples.
_wiki_adj_dict = {
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
_wiki_init_S = np.array(
    [[1,0,0] for _ in range(3)] +
    [[0,1,0] for _ in range(3)] + 
    [[0,0,1] for _ in range(3)],
    dtype=np.float
)
_tester_adj_dict = {
                1: [2,3,4],
                2: [1,3],
                3: [1,2],
                4: [1,5,6],
                5: [4,6],
                6: [4,5]
}
_tester_init_S = np.array(
    [[0,0],[1,0],[1,0],[0,1],[0,1],[0,1]],
    dtype=np.float
)


class GenericTester(unittest.TestCase):
    def setUp(self):
        self.wiki_adj = _wiki_adj_dict
        self.wiki_A = adj_dict_to_adj_mat(self.wiki_adj)
        self.wiki_S = _wiki_init_S
        self.gener_adj = _tester_adj_dict
        self.gener_A = adj_dict_to_adj_mat(self.gener_adj)
        self.gener_S = _tester_init_S
        self.patent_adj = get_patent_adj()
        self.patent_A = adj_dict_to_adj_mat(self.patent_adj) 
        self.patent_S = make_diagonal(self.patent_A.shape[0])

# Right now, makes no assertions about the output. Only tests that they actually run. 
class TestHelpers(GenericTester):
    def TestComputeModularity(self):
        modularity(self.wiki_A, self.wiki_S)
        modularity(self.gener_A, self.gener_S)
        modularity(self.patent_A, self.patent_S)
        
    def TestComputeB(self):
        get_B(self.wiki_A)
        get_B(self.gener_A)
        get_B(self.patent_A)

class TestCommunityDetectorMethods(GenericTester):
    def setUp(self):
        super(TestCommunityDetectorMethods, self).setUp()
        self.wiki_detector = CommunityDetector(self.wiki_adj)
        self.gener_detector = CommunityDetector(self.gener_adj)
        self.patent_detector = CommunityDetector(self.patent_adj)
    
    def TestWikiCommunities(self):
        """ Make sure that the toy wikipedia network has 3 communities. """
        self.assertEqual(3, len(self.wiki_detector.run()))
