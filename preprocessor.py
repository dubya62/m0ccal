
import tokenize
import os

import lexer
import normalizer
import blocker


# TODO: make imports create sorrounding classes


def preprocess(tokens:tokenize.Tokens, start_path, already_included=set()):
    # handle directives
    tokens = handle_directives(tokens, start_path, already_included)
    return tokens


def handle_directives(tokens:tokenize.Tokens, start_path, already_included):
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == "#BLOCK":
            tokens[i].content = handle_directives(tokens[i].content, start_path, already_included)
        elif tokens[i] == ";" and i + 1 < n and tokens[i+1] == "#":
            # this is a directive.
            # pull the entire line and handle it 
            handle_directive(tokens, i+1, start_path, already_included)
            i += len(tokens) - n
            n = len(tokens)
        i += 1
    return tokens
    

def handle_directive(tokens:tokenize.Tokens, index:int, start_path, already_included):
    # index = location of #

    line_end = tokens.get_line_end(index)
    if line_end is None:
        tokens[index].fatal_error("Expected a preprocessor directive")

    statement = tokenize.Tokens(tokens[index:line_end])

    # handle import statements
    result = handle_import(statement, start_path, already_included)

    tokens.tokens = tokens[:index] + result.tokens + tokens[line_end:]

    return tokens


def handle_import(tokens:tokenize.Tokens, start_path, already_included):
    """
    Handle import syntax and return handled tokens from those files
    """
    EXTENSION = ".ccal"

    if len(tokens) < 3:
        tokens[0].fatal_error("Expected file in import")

    if tokens[0] != "#" or tokens[1] != "import":
        tokens[0].fatal_error("Invalid import directive")

    filename = tokens[2:]
    
    # go up parent directories for each .
    filepath = os.path.dirname(start_path)
    filepath = os.path.abspath(filepath)
    while len(filename) > 0:
        if filename[0] == ".":
            filepath = os.path.dirname(filepath)
        else:
            break
        del filename[0]
    

    # iterate through the modules
    filepaths = None
    while len(filename) > 0:
        if filename[0] == "*":
            # * must be the last thing
            if len(filename) != 1:
                filename[0].fatal_error("* must be last name in import path")
            # recursively search
            dirs = [filepath]
            files = []
            while len(dirs) > 0:
                print(files, dirs)
                current = os.listdir(dirs[0])
                print(current)
                for x in current:
                    current_path = os.path.join(dirs[0], x)
                    print(current_path)
                    if os.path.isfile(current_path) and current_path[-5:] == ".ccal":
                        files.append(current_path)
                    elif os.path.isdir(current_path):
                        dirs.append(current_path)
                del dirs[0]
            filepaths = files
            
        else:
            filepath = os.path.join(filepath, filename[0].token)

        del filename[0]


    if filepaths is None:
        filepath = filepath + EXTENSION
        result = get_file_contents(filepath, already_included)
    else:
        result = tokenize.Tokens([])
        for x in filepaths:
            if os.path.isfile(x):
                result.tokens += get_file_contents(x, already_included).tokens
            
    return result


def get_file_contents(filepath, already_included):
    print(f"Importing: {filepath}")
    if not os.path.isfile(filepath):
        print(f"File: {filepath} does not exist...")
        exit(0)

    if filepath in already_included:
        print(f"Circular import of {filepath} detected.")
        exit(0)

    result = lexer.lex(filepath)
    result = normalizer.normalize(result, filepath)
    result = blocker.block(result)

    child_included = set(already_included)
    child_included.add(filepath)

    result = preprocess(result, filepath, child_included)

    return result


