#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return None
    if sentence:
        length = len(sentence)
    else:
        length = 0
    return (length, sentence if not sentence else sentence[0:1])
