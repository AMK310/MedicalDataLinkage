import pandas as pd

def clean_data(df):
    # Suppression des doublons
    df = df.drop_duplicates()
    # Traitement des valeurs manquantes
    df = df.dropna(subset=['id', 'title', 'journal'])
    # Normalisation des formats de date
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['date'] = df['date'].dt.strftime('%d/%m/%Y')
    return df

def fix_date_format(pubmed_df):
    # Vérifier la ligne avec l'id "6"
    row_to_fix = pubmed_df.loc[pubmed_df['id'] == 6]

    # Vérifier si la ligne existe
    if not row_to_fix.empty:
        # Convertir la date au format attendu
        pubmed_df.loc[pubmed_df['id'] == 6, 'date'] = pd.to_datetime(row_to_fix['date'], format='%Y-%m-%d').dt.strftime('%d/%m/%Y')

    return pubmed_df

def clean_clinical_trials(clinical_trials_df):
    # Supprimer la ligne dupliquer avec l'id vide 
    clinical_trials_df = clinical_trials_df.dropna(subset=["id"])
    # Assigner la valeur manquante
    clinical_trials_df.at[5,'journal'] = "Journal of emergency nursing"

    # Assigner une valeur manquante pour la date mal formatée
    clinical_trials_df.at[5, 'date'] = "25 May 2020"

    # Convertir la colonne 'date' en datetime
    clinical_trials_df['date'] = pd.to_datetime(clinical_trials_df['date'], errors='coerce')
    clinical_trials_df['date'] = clinical_trials_df['date'].dt.strftime('%d/%m/%Y')
    # Remplacer les valeurs de journal anormales
    clinical_trials_df.at[7, 'journal'] = "Journal of emergency nursing"

    return clinical_trials_df
