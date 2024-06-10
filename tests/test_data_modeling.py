import unittest
from src.data_modeling import create_graph, export_to_json
import os
import json

class TestDataModeling(unittest.TestCase):

    def setUp(self):
        self.mentions = [
            {'drug': 'DIPHENHYDRAMINE', 'atccode': 'A04AD', 'journal': 'journal1', 'date': '01/01/2019'},
            {'drug': 'TETRACYCLINE', 'atccode': 'S03AA', 'journal': 'journal2', 'date': '02/01/2019'}
        ]
        self.output_file = 'output/test_drug_mentions.json'

    def test_create_graph(self):
        graph = create_graph(self.mentions)
        self.assertIn('DIPHENHYDRAMINE', graph)
        self.assertEqual(len(graph['DIPHENHYDRAMINE']), 1)

    def test_export_to_json(self):
        graph = create_graph(self.mentions)
        export_to_json(graph, self.output_file)
        self.assertTrue(os.path.exists(self.output_file))
        with open(self.output_file, 'r') as f:
            data = json.load(f)
            self.assertIn('DIPHENHYDRAMINE', data)

if __name__ == '__main__':
    unittest.main()
