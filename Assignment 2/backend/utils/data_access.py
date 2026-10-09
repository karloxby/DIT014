
import json

# JSON reader
def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as target_json:
            target = json.load(target_json)
    
    except FileNotFoundError:
        return None, "Error - Unable to open file."
    except json.JSONDecodeError:
        return None, "Error - Unable to validate file format."

    return target, None

