
import json
import csv

from backend.utils import error

# JSON reader
def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as target_json:
            target = json.load(target_json)
    
    except FileNotFoundError:
        return None, error.open_file
    except json.JSONDecodeError:
        return None, error.file_format

    return target, None

# CSV reader
def load_csv(path):
    try:
        with open(path, "r", encoding="utf-8") as target_csv:
            target = list(csv.DictReader(target_csv))

    except FileNotFoundError:
        return None, error.open_file

    except (UnicodeDecodeError, csv.Error):
        return None, error.file_format

    return target, None

