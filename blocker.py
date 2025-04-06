"""
Break scopes into different blocks
"""

import tokenize

class Block:
    def __init__(self, name:tokenize.Token, args:tokenize.Tokens, content:tokenize.Tokens):
        self.name = name
        self.args = args
        self.content = content

    def __str__(self):
        return f"#BLOCK {self.name}"

    def __repr__(self):
        return f"{self.name} BLOCK ({self.args}) {self.content} ENDBLOCK {self.name}"


def block(tokens:tokenize.Tokens):
    # find scopes and convert them to blocks
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == "{":
            contents = tokens.get_match_content(i, "}")
            if contents is None:
                tokens[i].fatal_error("Unmatched {")
            line_start = tokens.get_line_start(i-1)

            new_block = Block(tokens[line_start+1], tokens[line_start+2:i], block(tokenize.Tokens(contents[1:-1])))

            tokens = tokenize.Tokens(tokens[:line_start+1] + tokens[i:])
            i = line_start+1
            tokens.insert(i, new_block)
            n = len(tokens)

        i += 1

    return tokens



