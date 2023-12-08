<<<<<<< HEAD
#!/usr/bin/python3
def best_score(a_dictionary):
=======
t_score(a_dictionary):
>>>>>>> c065d8bd456b6475a876a0882686e02710b80099
    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    max_score = float('-inf')
    best_key = None

    for key, value in a_dictionary.items():
        if isinstance(value, int) and value > max_score:
            max_score = value
            best_key = key

    return best_key
