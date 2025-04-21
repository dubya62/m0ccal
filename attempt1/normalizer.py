
import tokenize


class Indention:
    def __init__(self, number_of_spaces):
        self.number_of_spaces = number_of_spaces
    def __repr__(self):
        return f"Indention({self.number_of_spaces})"
    def __eq__(self, other):
        return other == "#INDENTION"


def normalize(tokens:list[str], filename:str):
    # remove comments
    tokens = remove_comments(tokens)

    # TODO: combine @directives

    # convert tabs to spaces
    tokens = convert_tabs(tokens)

    # convert newlines to line indents
    tokens = convert_newlines(tokens)

    # remove extra indents (indents with nothing on the line)
    tokens = remove_extra_indents(tokens)

    # convert indention syntax to braces
    tokens = convert_indention_syntax(tokens)

    # Add semicolons to the end of lines
    tokens = add_semicolons(tokens)

    # convert to Token objects
    tokens = convert_to_tokens(tokens, filename)

    # combine Float literals into single tokens
    tokens = combine_float_literals(tokens)

    # remove whitespace
    tokens = remove_whitespace(tokens)


    # put semicolons around all statements
    tokens = normalize_semicolons(tokens)


    return tokens



def remove_comments(tokens:list[str]):

    comment = False
    multiline = False

    i = 0
    n = len(tokens)
    escapable = set([
        "n",
        "t",
        "\\",
        "'",
        '"',
        "r",
        "b",
        "f",
        "v",
        ])
    while i < n:

        if tokens[i] == "/" and i + 1 < n :
            if tokens[i+1] == "/" and not comment:
                comment = True
                multiline = False
            elif tokens[i+1] == "*" and not comment:
                comment = True
                multiline = True

        elif tokens[i] == "*" and i + 1 < n:
            if tokens[i+1] == "/" and comment and multiline:
                del tokens[i]
                del tokens[i]
                n -= 2
                comment = False
                multiline = False
                continue

        if tokens[i] == "'" or tokens[i] == '"' and not comment:
            # combine into a single string
            starter = tokens[i]
            done = False
            backslashes = 0
            while i + 1 < n and not done:
                if tokens[i+1] == "\\":
                    backslashes ^= 1

                if not backslashes or tokens[i+1]:
                    tokens[i] += tokens[i+1]
                elif tokens[i+1] in escapable:
                    tokens[i] += "\\" + tokens[i+1]

                if tokens[i+1] == starter and not backslashes:
                    done = True

                if tokens[i+1] != "\\":
                    backslashes = 0

                del tokens[i+1]
                n -= 1

        if tokens[i] == "\n":
            if comment and not multiline:
                comment = False

        if comment:
            del tokens[i]
            n -= 1
            continue


        i += 1

    return tokens


def convert_tabs(tokens:list[str]):
    # any time there is \t, convert to 4 spaces
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == "\t":
            tokens[i] = " "
            tokens.insert(i, " ")
            tokens.insert(i, " ")
            tokens.insert(i, " ")
            n += 3
            i += 3
        i += 1
    return tokens


def convert_newlines(tokens:list[str]):
    # any time there is \n followed by 0 or more spaces,
    # convert to Indention object with that number of spaces
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == "\n":

            # remove whitespace before \n to make \ work at end of line
            while i > 0 and tokens[i-1] == " ":
                del tokens[i-1]
                i -= 1
                n -= 1

            tokens[i] = Indention(0)
            while i + 1 < n and tokens[i+1] == " ":
                tokens[i].number_of_spaces += 1
                del tokens[i+1]
                n -= 1
            if i > 0 and tokens[i-1] == "\\":
                del tokens[i-1]
                del tokens[i-1]
                i -= 2
                n -= 2

        i += 1

    return tokens


def remove_extra_indents(tokens:list[str]):
    i = 0
    n = len(tokens)
    while i + 1 < n:
        if tokens[i] == "#INDENTION" and tokens[i+1] == "#INDENTION":
            del tokens[i]
            n -= 1
            continue
        i += 1
    return tokens



def convert_indention_syntax(tokens:list[str]):
    # any time there is : followed by an indention,
    # anything else at that same indention level is 
    # encapsulated with {}
    i = 0
    n = len(tokens)
    print(tokens)
    while i < n:
        if tokens[i] == ":":
            while i + 1 < n and tokens[i+1] == " ":
                del tokens[i+1]
                n -= 1
            if i + 1 < n and tokens[i+1] == "#INDENTION":
                j = i
                my_indent = Indention(0)
                while j >= 0:
                    if tokens[j] == "#INDENTION":
                        my_indent = tokens[j]
                        break
                    j -= 1

                indent_level = tokens[i+1].number_of_spaces
                
                if my_indent.number_of_spaces >= indent_level:
                    # TODO: make this error message more helpful
                    print(f"Expected indented block: {my_indent.number_of_spaces}, {indent_level}")
                    exit(1)


                # remove : and replace INDENTION with {
                del tokens[i]
                tokens[i] = "{"
                n -= 1

                j = i + 1
                while j < n:
                    # if a shorter nonzero indent is found, end the braces
                    if tokens[j] == "#INDENTION":
                        if tokens[j].number_of_spaces < indent_level and not (j + 1 < n and tokens[j+1] == "#INDENTION"):

                            break
                    j += 1
                tokens.insert(j, "}")
                n += 1
        i += 1

    return tokens


def add_semicolons(tokens:list[str]):
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == "#INDENTION":
            tokens.insert(i, ";")
            n += 1
            i += 1
        i += 1
    return tokens


def remove_whitespace(tokens:tokenize.Tokens):
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == "#INDENTION" or tokens[i] in [" ", "\t"]:
            del tokens[i]
            i -= 1
            n -= 1
        i += 1
            


    return tokens



def convert_to_tokens(tokens:list[str], filename:str):
    token_version = [tokenize.Token(x) for x in tokens]
    line_number = 1
    for x in token_version:
        x.line_number = line_number
        x.filename = filename
        if x == "#INDENTION":
            line_number += 1

    result = tokenize.Tokens(token_version)
    return result


def normalize_semicolons(tokens:tokenize.Tokens):
    # require semicolons before and after {, }
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] in ["{", "}"]:
            tokens.insert(i+1, tokenize.Token(";"))
            n += 1
            if tokens[i] == "}":
                tokens.insert(i, tokenize.Token(";"))
                i += 1
                n += 1
        i += 1

    # and after ;
    i = 0
    while i < n:
        if tokens[i] == ";":
            while i + 1 < n and tokens[i+1] == ";":
                del tokens[i+1]
                n -= 1 
        i += 1

    return tokens


def combine_float_literals(tokens:tokenize.Tokens):
    i = 0
    n = len(tokens)
    while i + 2 < n:
        if tokens[i].is_int_literal() and tokens[i+1] == "." and tokens[i+2].is_int_literal():
            tokens[i].token += tokens[i+1].token + tokens[i+2].token
            del tokens[i+1]
            del tokens[i+1]
            n -= 2
        i += 1
    return tokens

