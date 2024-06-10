import json
from collections import Counter

def journal_with_most_mentions(json_file):
    """
    Trouve le journal qui mentionne le plus de médicaments différents.

    Args:
    - json_file (str): Le chemin du fichier JSON contenant les données.

    Returns:
    - str: Le nom du journal ayant le plus de mentions de médicaments.
    """
    with open(json_file, 'r') as file:
        data = json.load(file)

    journal_mentions = Counter()
    for entry in data:
        journal = entry['journal']
        drugs_mentioned = entry['mentions']
        journal_mentions[journal] += len(drugs_mentioned)

    most_mentioned_journal = journal_mentions.most_common(1)[0][0]
    return most_mentioned_journal

def related_drugs_for_journal(json_file, journal, given_drug):
    """
    Trouve les médicaments mentionnés par un journal mais pas dans les essais cliniques.

    Args:
    - json_file (str): Le chemin du fichier JSON contenant les données.
    - journal (str): Le nom du journal pour lequel rechercher les médicaments associés.
    - given_drug (str): Le médicament de référence.

    Returns:
    - set: Un ensemble de médicaments mentionnés par le journal mais pas dans les essais cliniques.
    """
    related_drugs = set()
    with open(json_file, 'r') as file:
        data = json.load(file)

    for entry in data:
        if entry['journal'] == journal and given_drug in entry['mentions']:
            related_drugs.update(entry['mentions'])

    related_drugs.remove(given_drug)
    return related_drugs
