import unittest
import networkx as nx
from community import detect, visualize, data
from community.util import get_community_lookup

# make sure the examples run, without the visualization part. 
class TestExamples(unittest.TestCase):
    def setUp(self):
        self.patent_adj = data.get_patent_adj()
        self.wiki_adj = data.get_wiki_adj()

    """
    def testPatentExample(self):
        detector = detect.CommunityDetector(self.patent_adj)
        communities = detector.run()
        n_communities = len(communities)
        community_lookup = get_community_lookup(communities)
        colors = visualize.discrete_color_scheme(n_communities+1)
        G = visualize.get_graph(patent_adj)
        G.graph['ancestor'] = 4723129
        node_colors = [colors[community_lookup[node]] for node in G.nodes()]
        node_colors[G.nodes().index(G.graph['ancestor'])] = colors[n_communities]
    """

    def testWikiExample(self):
        detector = detect.CommunityDetector(self.wiki_adj)
        communities = detector.run()
        n_communities = len(communities)
        community_lookup = get_community_lookup(communities)
        colors = visualize.discrete_color_scheme(n_communities)
        G = visualize.get_graph(self.wiki_adj)
        node_colors = [colors[community_lookup[node]] for node in G.nodes()]
