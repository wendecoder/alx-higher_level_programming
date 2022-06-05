#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence[0] = None
        tuple_a = len(sentence), sentence[0]
        return tuple_a
    else:
        tuple_a = len(sentence), sentence[0]
        return tuple_a
    
