# tests/test_data_cleaning.py

import pandas as pd
import pytest
from src.data_cleaning import clean_data, fix_date_format, clean_clinical_trials

class TestDataCleaning:
    def setup_method(self):
        self.sample_data = [
            {'id': '1', 'journal': 'Journal of emergency nursing', 'date': '01/01/2019'},
            {'id': '2', 'journal': 'Journal of emergency nursing', 'date': '01/01/2019'},
            {'id': '3', 'journal': 'The Journal of pediatrics', 'date': '02/01/2019'},
            {'id': '4', 'journal': 'Journal of emergency nursing', 'date': '01/01/2020'},
            {'id': '5', 'journal': 'Journal of emergency nursing', 'date': '01/01/2020'},
            {'id': '6', 'journal': 'Journal of emergency nursing', 'date': '01/01/2020'},
            {'id': '7', 'journal': 'Journal of food protection', 'date': '01/01/2020'}
        ]
    
    def test_fix_date_format(self):
        fixed_df = fix_date_format(pd.DataFrame(self.sample_data))
        assert fixed_df.loc[fixed_df['id'] == "6", 'date'].values[0] == '01/01/2020'

    def test_clean_data(self):
        cleaned_df = clean_data(pd.DataFrame(self.sample_data))
        assert len(cleaned_df) == 7
