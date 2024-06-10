import pandas as pd

def merge_datasets(pubmed_df, clinical_trials_df):
    """
    Fusionne deux ensembles de données PubMed et essais cliniques.

    Args:
    - pubmed_df (DataFrame): Le DataFrame des données PubMed.
    - clinical_trials_df (DataFrame): Le DataFrame des données des essais cliniques.

    Returns:
    - DataFrame: Le DataFrame fusionné des deux ensembles de données.
    """
    # Renommer les colonnes pour une fusion facile
    pubmed_df = pubmed_df.rename(columns={'title': 'title'})
    clinical_trials_df = clinical_trials_df.rename(columns={'scientific_title': 'title'})

    # Sélectionner les colonnes pertinentes
    pubmed_df = pubmed_df[['id', 'title', 'date', 'journal']]
    clinical_trials_df = clinical_trials_df[['id', 'title', 'date', 'journal']]

    # Fusionner les ensembles de données
    merged_data = pd.concat([pubmed_df, clinical_trials_df], ignore_index=True)
    return merged_data

def extract_mentions(merged_data, drugs):
    """
    Extrait les mentions de médicaments à partir des données fusionnées.

    Args:
    - merged_data (DataFrame): Le DataFrame fusionné des données.
    - drugs (DataFrame): Le DataFrame contenant les données des médicaments.

    Returns:
    - list: Une liste de dictionnaires contenant les mentions de médicaments.
    """
    mentions = []
    for _, drug in drugs.iterrows():
        for _, row in merged_data.iterrows():
            if pd.isna(row['title']):
                continue
            if drug['drug'].upper() in row['title'].upper():
                mentions.append({
                    'drug': drug['drug'],
                    'atccode': drug['atccode'],
                    'journal': row['journal'],
                    'date': row['date']
                })
    return mentions
