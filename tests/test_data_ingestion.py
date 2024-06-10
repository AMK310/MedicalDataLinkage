import unittest
from src.data_ingestion import load_csv, load_json
import os

class TestDataIngestion(unittest.TestCase):

    def test_load_csv(self):
        df = load_csv('data/drugs.csv')
        self.assertFalse(df.empty)
        self.assertIn('atccode', df.columns)
        self.assertIn('drug', df.columns)

    def test_load_json(self):
        data = load_json('data/pubmed.json')
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIn('id', data[0])
        self.assertIn('title', data[0])

if __name__ == '__main__':
    unittest.main()
