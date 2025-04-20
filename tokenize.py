

class Token:
    def __init__(self, token):
        self.token = token
        self.filename = ""
        self.line_number = 0

    def fatal_error(self, message):
        print(f"FATAL ERROR at {self.filename}:{self.line_number}")
        print(f"\t{message}")
        exit(1)

    def is_int_literal(self):
        try:
            x = int(self.token)
            return str(x) == self.token
        except:
            pass
        return False

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
        return self.token == str(other)
    def __contains__(self, item):
        return item in self.token
    def __ne__(self, other):
        return self.token != str(other)



class Tokens:
    def __init__(self, tokens:list[Token]=[]):
        self.tokens = tokens

    def get_match_index(self, start_index, closer:str) -> int:
        opened = 0
        i = start_index
        while i < len(self.tokens):
            if self.tokens[i] == self.tokens[start_index]:
                opened += 1
            elif self.tokens[i] == closer:
                opened -= 1
                if opened == 0:
                    return i
            i += 1


    def get_match_content(self, start_index:int, closer:str) -> 'Tokens':
        end_index = self.get_match_index(start_index, closer)
        if end_index is None:
            return None

        result = Tokens(self.tokens[start_index:end_index+1])
        self.tokens = self.tokens[:start_index] + self.tokens[end_index+1:]

        return result


    def get_line_start(self, index):
        while index > 0:
            if self.tokens[index] == ";":
                return index
            index -= 1
        return index
    

    def get_line_end(self, index):
        while index < len(self.tokens):
            if self.tokens[index] == ";":
                return index
            index += 1
        return index

    def get_scope_end(self, index):
        stack = 0
        while index < len(self.tokens):
            if self.tokens[index] == "{":
                stack += 1
            elif self.tokens[index] == "}":
                if stack == 0:
                    return index
                stack -= 1
            index += 1
        return len(self.tokens) - 1


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

