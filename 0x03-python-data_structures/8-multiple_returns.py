#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        return 0, None
    w = len(sentence)
    x = sentence[:1]
    return w, x
