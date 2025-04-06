
import tokenize

def preprocess(tokens:tokenize.Tokens):
    # handle directives
    tokens = handle_directives(tokens)
    return tokens


def handle_directives(tokens:tokenize.Tokens):
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == ";" and i + 1 < n and tokens[i+1] == "#":
            # this is a directive.
            # pull the entire line and handle it 
            pass
        i += 1
    return tokens
    

def handle_directive(tokens:tokenize.Tokens):

    # handle import statements
    # handle define
    # handle macro
    # handle undef
    # handle ifdef
    # handle ifndef
    # handle if
    # handle elif
    # handle else
    # handle endif
    # handle error
    # handle warn
    return tokens
