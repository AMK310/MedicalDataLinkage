import argparse
from src.data_ingestion import load_csv, load_json
from src.data_cleaning import assign_missing_id, fix_date_format, clean_clinical_trials, fix_trailing_comma_in_json
from src.data_processing import merge_datasets, extract_mentions
from src.data_modeling import create_graph, export_to_json
import pandas as pd
from src.adhoc_processing import journal_with_most_mentions, related_drugs_for_journal

def main():
    parser = argparse.ArgumentParser(description='Process data and perform ad-hoc analysis.')
    parser.add_argument('-adhoc', action='store_true', help='Perform ad-hoc analysis')
    args = parser.parse_args()

    # Chargement des données
    drugs = load_csv('data/drugs.csv')
    pubmed_csv = load_csv('data/pubmed.csv')
    pubmed_json = load_json('data/pubmed.json')
    clinical_trials = load_csv('data/clinical_trials.csv')

    # Nettoyage des données
    pubmed = fix_date_format(pubmed_csv)
    clinical_trials = clean_clinical_trials(clinical_trials)
    fix_trailing_comma_in_json('data/pubmed.json')
    pubmed_json = assign_missing_id(pubmed_json)
    pubmed = pd.concat([pubmed_csv, pubmed_json], ignore_index=True)

    # Fusion des datasets
    merged_data = merge_datasets(pubmed, clinical_trials)

    # Extraction des mentions
    mentions = extract_mentions(merged_data, drugs)

    # Modélisation des données
    graph = create_graph(mentions)

    # Export des données en JSON
    export_to_json(graph, 'output/drug_mentions.json')

    if args.adhoc:
        most_mentioned_journal = journal_with_most_mentions('output/drug_mentions.json')
        print("Journal with most mentions:", most_mentioned_journal)

        related_drugs = related_drugs_for_journal('output/drug_mentions.json', most_mentioned_journal, 'Aspirin')
        print("Related drugs for Aspirin:", related_drugs)

if __name__ == '__main__':
    main()
