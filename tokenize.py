

class Token:
    def __init__(self, token):
        self.token = token
        self.filename = ""
        self.line_number = 0

    def __hash__(self):
        return self.token.__hash__()
    def __getitem__(self, index):
        return self.token[index]
    def __repr__(self):
        return str(self.token)
    def __str__(self):
        return str(self.token)
    def __len__(self):
        return len(self.token)
    def __eq__(self, other):
        return self.token == other
    def __contains__(self, item):
        return item in self.token
    def __ne__(self, other):
        return self.token != other



class Tokens:
    def __init__(self, tokens:list[Token]=[]):
        self.tokens = tokens

    def __getitem__(self, index):
        return self.tokens[index]
    def __str__(self):
        return str(self.tokens)
    def __len__(self):
        return len(self.tokens)
    def __setitem__(self, index, value):
        self.tokens[index] = value
    def __contains__(self, item):
        return item in self.tokens
    def __delitem__(self, index):
        del self.tokens[index]
    def append(self, item):
        self.tokens.append(item)
    def extend(self, iterable):
        self.tokens.extend(iterable)
    def insert(self, index, item):
        self.tokens.insert(index, item)
    def remove(self, item):
        self.tokens.remove(item)
    def pop(self, index=-1):
        self.tokens.pop(index)
    def clear(self):
        self.tokens.clear()

