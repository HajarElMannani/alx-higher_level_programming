#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        score = 0
        for x, y in a_dictionary.items():
            if y > score:
                score = y
                name = x
        return name
