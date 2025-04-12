
from converter import ClassBlock
from tokenize import Token, Tokens

def check_syntax(tokens:Tokens):
    # Make sure that each scope only has 1 definition of classes
    tokens = ensure_class_singularity(tokens)

    # TODO: For each class, figure out what all static and instance variables need to be allocated
    tokens = find_class_variables(tokens)

    # TODO: Make sure that each scope only has 1 definition of functions with the same number and types of args

    # TODO: Make sure that all accesses follow access specifiers
    # TODO: Remove all access specifiers
    # TODO: Make all references to objects, functions, and states point to their definition

    # TODO: Disambiguate function calls based on input arg types

    return tokens


def ensure_class_singularity(tokens:Tokens):
    class_names = set()
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == "#BLOCK":
            tokens[i].content = ensure_class_singularity(tokens[i].content)
        if issubclass(type(tokens[i]), ClassBlock):
            if tokens[i].name in class_names:
                tokens[i].fatal_error(f"Class {tokens[i].name} is defined multiple times in this scope")
            class_names.add(tokens[i].name)
        i += 1

    return tokens


def find_class_variables(tokens:Tokens):
    return tokens


