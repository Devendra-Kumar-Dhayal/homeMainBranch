def print_recursive_dictionary(dictionary, indent=0):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print('\t' * indent + str(key) + ':')
            print_recursive_dictionary(value, indent + 1)
        else:
            print('\t' * indent + str(key) + ': ' + str(value))
