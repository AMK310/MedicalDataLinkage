import json

def create_graph(mentions):
    """
    Crée un graphe de liaison entre les médicaments et leurs mentions dans les journaux.

    Args:
    - mentions (list): Une liste de dictionnaires représentant les mentions de médicaments.

    Returns:
    - dict: Un dictionnaire représentant le graphe de liaison entre les médicaments et leurs mentions.
    """
    graph = {}
    for mention in mentions:
        drug = mention['drug']
        journal = mention['journal']
        date = mention['date']

        if drug not in graph:
            graph[drug] = []

        graph[drug].append({
            'journal': journal,
            'date': date
        })

    return graph

def export_to_json(data, filepath):
    """
    Exporte les données au format JSON dans un fichier.

    Args:
    - data (dict): Les données à exporter.
    - filepath (str): Le chemin du fichier JSON de sortie.
    """
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)
