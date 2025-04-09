"""
Break scopes into different blocks
"""

import tokenize

class Block:
    def __init__(self, name:tokenize.Token, args:tokenize.Tokens, content:tokenize.Tokens):
        self.name = name
        self.args = args
        self.content = content
        self.access = tokenize.Token("protected")
        if len(self.args) > 0 and self.args[0] in ["public", "private", "protected"]:
            self.access = self.args[0]
            del self.args[0]
        self.parse_parens()

    def parse_parens(self):
        i = 0
        while i < len(self.args):
            if self.args[i] == "(":
                self.inner_args = self.args.get_match_content(i, ")")[1:-1]
                return self.inner_args
            i += 1
        self.inner_args = None

    def __str__(self):
        return f"#BLOCK"

    def __eq__(self, other):
        return str(self) == str(other)

    def __repr__(self):
        return f"{self.name} BLOCK {self.args}<>{self.inner_args} {self.content} ENDBLOCK {self.name}"


def block(tokens:tokenize.Tokens):
    # handle use statments
    tokens = handle_use(tokens)

    # remove pass statements
    tokens = remove_pass(tokens)

    # find scopes and convert them to blocks
    tokens = convert_to_blocks(tokens)

    # remove documentation blocks
    tokens = remove_documentation_blocks(tokens)

    return tokens


def convert_to_blocks(tokens):
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == "{":
            contents = tokens.get_match_content(i, "}")
            if contents is None:
                tokens[i].fatal_error("Unmatched {")
            line_start = tokens.get_line_start(i-1)

            if tokens[line_start+1] == "C":
                content = tokenize.Tokens(contents[1:-1])
            else:
                content = convert_to_blocks(tokenize.Tokens(contents[1:-1]))

            new_block = Block(tokens[line_start+1], tokenize.Tokens(tokens[line_start+2:i]), content)

            tokens = tokenize.Tokens(tokens[:line_start+1] + tokens[i:])
            i = line_start+1
            tokens.insert(i, new_block)
            n = len(tokens)

        i += 1

    return tokens


def handle_use(tokens):
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == "use":
            # get first part of use statement
            del tokens[i]
            n -= 1

            first = []
            j = i
            while j < n:
                if tokens[j] == "as":
                    break
                first.append(tokens[j])
                del tokens[j]
                n -= 1

            if len(first) == 0:
                tokens[i].fatal_error("First part of use statement is empty")

            if j >= n:
                tokens[i].fatal_error("Expected 'as' in use statement")

            # get the second part now
            del tokens[j]
            n -= 1

            second = []
            while j < n:
                if tokens[j] == ";":
                    break
                second.append(tokens[j])
                del tokens[j]
                n -= 1

            if len(first) == 0:
                tokens[i].fatal_error("Second part of use statement is empty")

            
            # find end of this scope
            last_index = tokens.get_scope_end(j)
            if last_index is None:
                tokens[i].fatal_error("Use statement inside invalid scope")

            # match and make replacement
            m = len(first)
            # a b as c d e
            # [a, b, c, d, e, f, g, }]
            # m = 2
            # [c, d, e, c, d, e, f, g, }]
            while j + m <= last_index:
                x = None
                for x in range(m):
                    if tokens[j+x] != first[x]:
                        x = None
                        break
                if x is not None:
                    tokens.tokens = tokens[:j] + second + tokens[j+m:]
                    j += len(second) - 1
                    n = len(tokens)
                
                j += 1

            n = len(tokens)
            i -= 1

        i += 1
    return tokens


def remove_pass(tokens):
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == "pass":
            del tokens[i]
            n -= 1
            continue
        i += 1
    return tokens



def remove_documentation_blocks(tokens):
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == "#BLOCK":
            if tokens[i].name == "&":
                del tokens[i]
                n -= 1
                i -= 1
            else:
                tokens[i].content = remove_documentation_blocks(tokens[i].content)
        i += 1
    return tokens





