import pandas as pd
import json 

def load_csv(file_path):
    """
    Charge un fichier CSV dans un DataFrame.

    Args:
    - file_path (str): Le chemin du fichier CSV.

    Returns:
    - pandas.DataFrame: Le DataFrame contenant les données du fichier CSV.
    """
    df = pd.read_csv(file_path)
    return df

def load_json(file_path):
    """
    Charge un fichier JSON dans un DataFrame.

    Args:
    - file_path (str): Le chemin du fichier JSON.

    Returns:
    - pandas.DataFrame: Le DataFrame contenant les données du fichier JSON.
    """
    with open(file_path, 'r') as file:
        data = json.load(file)
        return pd.DataFrame(data)
