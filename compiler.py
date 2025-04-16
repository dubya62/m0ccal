
import sys

import lexer
import normalizer
import blocker
import preprocessor
import converter
import syntax_checker
import constrainer

if __name__ == "__main__":
    FILENAME = sys.argv[1]

    # Break the file into tokens
    print("++++++++++++++++++++++++++++++")
    print("Lexing...")
    tokens = lexer.lex(FILENAME)
    print(tokens)

    # Remove comments, handle indentions, combine strings, and add semicolons
    print("++++++++++++++++++++++++++++++")
    print("Normalizing...")
    tokens = normalizer.normalize(tokens, FILENAME)
    print(tokens)

    # convert scopes into block
    print("++++++++++++++++++++++++++++++")
    print("Blocking...")
    tokens = blocker.block(tokens)
    print(tokens)

    # handle preprocessor directives
    print("++++++++++++++++++++++++++++++")
    print("Preprocessing...")
    tokens = preprocessor.preprocess(tokens, FILENAME)
    print(tokens)

    # Convert operator definitions and usages to function calls
    # Handle APIs to C code
    # Handle Functions
    print("++++++++++++++++++++++++++++++")
    print("Converting...")
    tokens = converter.convert(tokens)
    print(tokens)

    # Handle access specifiers and syntax errors
    print("++++++++++++++++++++++++++++++")
    print("Checking syntax...")
    tokens = syntax_checker.check_syntax(tokens)
    print(tokens)

    # Run through the program and find all possible values of variables at each location in the program (handle constraints and assumes)
    """
    print("++++++++++++++++++++++++++++++")
    print("Checking constraints...")
    tokens = constrainer.constrain(tokens)
    print(tokens)
    """
    
    # TODO RN: Rearrange the program to be in the correct order

    # TODO RN: Convert the program to C






