"""
Reorganize a ccal file into the actual order of execution, getting rid 
of extra class/function definitions
"""

import tokenize

def reorder(tokens:tokenize.Tokens):
    # remove the order from definitions by putting all of the function/class/operator/api definitions unordered at the top of the scope
    return tokens
