
from backend.utils import error

# Converts to integers
def string_to_int(target):
    if type(target) is str:
        try:
            target = int(target)
        except ValueError:
            return None

    elif type(target) is list:
        parsed_target = []

        for item in target:
            try:
                item = int(item)
                parsed_target.append(item)
            except ValueError:
                return None

        target = parsed_target
    
    else:
        return None

    return target


# Converts to float
def string_to_float(target):
    if type(target) is str:
        try:
            target = float(target)
        except ValueError:
            return None

    elif type(target) is list:
        parsed_target = []

        for item in target:
            try:
                item = float(item)
                parsed_target.append(item)
            except ValueError:
                return None

        target = parsed_target
    
    else:
        return None

    return target


# Cleans up trailing spaces
def strip_spaces(target):
    if type(target) is str:
        stripped_target = target.strip(" ")

        target = stripped_target

    elif type(target) is list:
        stripped_target = []
        
        for item in target:
            stripped_target.append(item.strip(" "))

        target = stripped_target
        
    else:
        return None, error.strip_spaces

    return target, None


# Returns dictionary keys
def get_keys(target):
    if type(target) is dict:
        return target.keys(), None

    else:
        return None, error.not_dictionary


# Checks keys against required keys
def has_required_keys(target, requirement):
    if type(target) is dict:
        for key in requirement:
            if key not in target or target.get(key) is None:
                return None, error.missing_field
    else:
        return None, error.not_dictionary

    return target, None

