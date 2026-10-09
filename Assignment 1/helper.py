
# Converts to integers
def string_to_int(target):
    if type(target) is str:
        try:
            target = int(target)
        except ValueError:
            return False

    elif type(target) is list:
        parsed_target = []

        for item in target:
            try:
                item = int(item)
                parsed_target.append(item)
            except ValueError:
                return False

        target = parsed_target
    
    else:
        return False

    return target


# Converts to float
def string_to_float(target):
    if type(target) is str:
        try:
            target = float(target)
        except ValueError:
            return False

    elif type(target) is list:
        parsed_target = []

        for item in target:
            try:
                item = float(item)
                parsed_target.append(item)
            except ValueError:
                return False

        target = parsed_target
    
    else:
        return False

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
        return False

    return target

