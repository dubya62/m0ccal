"""
The purpose of this program is to allow lexing of m0ccal files
Given a filename, it should break the file up into tokens
"""

def lex(filename):
    data = open_file(filename)
    tokens = break_into_tokens(data)
    return tokens


def open_file(filename):
    try:
        with open(filename, 'r') as f:
            data = f.read()
    except:
        print(f"Unable to open file {filename}")
    return data


def break_into_tokens(data:str) -> list[str]:
    break_chars = set([
        "~", "!", "@", "#", "%", "^", "$", "^", "&", "*", "(", ")", "-", "+", "=", "[", "]", "{", "}", "|", "<", ">", ",", ".", "/", "?", ":", " ", "\n", "\t", "'", '"', ";", "\\"
        ])

    i = 0
    n = len(data)
    current = ""
    result = []
    while i < n:
        if data[i] in break_chars:
            if len(current) > 0:
                result.append(current)
            current = ""
            result.append(data[i])
        else:
            current += data[i]
        i += 1

    if len(current) > 0:
        result.append(current)

    return result
