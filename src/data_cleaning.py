import pandas as pd

def clean_data(df):
    """
    Nettoie les données en supprimant les doublons, les valeurs manquantes et en normalisant les formats de date.

    Args:
    - df (DataFrame): Le DataFrame contenant les données à nettoyer.

    Returns:
    - DataFrame: Le DataFrame nettoyé.
    """
    # Suppression des doublons
    df = df.drop_duplicates()
    # Traitement des valeurs manquantes
    df = df.dropna(subset=['id', 'title', 'journal'])
    # Normalisation des formats de date
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['date'] = df['date'].dt.strftime('%d/%m/%Y')
    return df

def fix_date_format(pubmed_df):
    """
    Corrige le format de la date dans un DataFrame PubMed.

    Args:
    - pubmed_df (DataFrame): Le DataFrame PubMed.

    Returns:
    - DataFrame: Le DataFrame avec le format de date corrigé.
    """
    # Vérifier la ligne avec l'id "6"
    row_to_fix = pubmed_df.loc[pubmed_df['id'] == 6]

    # Vérifier si la ligne existe
    if not row_to_fix.empty:
        # Convertir la date au format attendu
        pubmed_df.loc[pubmed_df['id'] == 6, 'date'] = pd.to_datetime(row_to_fix['date'], format='%Y-%m-%d').dt.strftime('%d/%m/%Y')

    return pubmed_df

def clean_clinical_trials(clinical_trials_df):
    """
    Nettoie les données des essais cliniques en supprimant les lignes avec un ID vide, en assignant une valeur à la date mal formatée
    et en normalisant le format de date.

    Args:
    - clinical_trials_df (DataFrame): Le DataFrame des essais cliniques.

    Returns:
    - DataFrame: Le DataFrame nettoyé des essais cliniques.
    """
    # Supprimer la ligne dupliquée avec l'id vide 
    clinical_trials_df = clinical_trials_df.dropna(subset=["id"])
    # Assigner une valeur pour la date mal formatée
    clinical_trials_df.at[5, 'journal'] = "Journal of emergency nursing"
    clinical_trials_df.at[5, 'date'] = "25 May 2020"

    # Convertir la colonne 'date' en datetime
    clinical_trials_df['date'] = pd.to_datetime(clinical_trials_df['date'], errors='coerce')
    clinical_trials_df['date'] = clinical_trials_df['date'].dt.strftime('%d/%m/%Y')
    # Remplacer les valeurs de journal anormales
    clinical_trials_df.at[7, 'journal'] = "Journal of emergency nursing"

    return clinical_trials_df

def assign_missing_id(pubmed_json):
    """
    Assigner des valeurs aux IDs manquants dans un DataFrame PubMed JSON.

    Args:
    - pubmed_json (DataFrame): Le DataFrame PubMed JSON.

    Returns:
    - DataFrame: Le DataFrame avec les IDs manquants assignés.
    """
    # Identifier les lignes avec l'id manquant
    pubmed_json.loc[pubmed_json['id'] == '', 'id'] = '13'
    return pubmed_json


def fix_trailing_comma_in_json(file_path):
    """
    Enlève la virgule après le dernier élément dans un fichier JSON.

    Args:
        file_path (str): Le chemin vers le fichier JSON à corriger.

    Returns:
        None
    """
    with open(file_path, 'r') as file:
        content = file.read()
    
    # Trouver la dernière fermeture de crochet "}" avant la fermeture de tableau "]"
    last_brace_index = content.rfind('}')
    last_square_bracket_index = content.rfind(']')

    # Vérifier si la virgule suit le dernier "}"
    if last_brace_index != -1 and last_square_bracket_index != -1:
        comma_index = content.rfind(',', last_brace_index, last_square_bracket_index)
        if comma_index != -1:
            # Enlever la virgule après le dernier élément
            content = content[:comma_index] + content[comma_index + 1:]

    # Réécrire le fichier corrigé
    with open(file_path, 'w') as file:
        file.write(content)


fix_trailing_comma_in_json('data/pubmed.json')