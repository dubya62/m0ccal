
import blocker
import tokenize


class ClassBlock(blocker.Block):
    """
    class_name = ""
    extends = []
    is_api = True/False
    access = "public" | "private" | "protected"

    """
    def __init__(self, name, args, content, is_api=False):
        if len(args) == 0:
            name.fatal_error("Expected class name after class")

        self.class_name = args[0]
        del args[0]

        if len(args) > 0:
            if args[0] != "extends":
                args[0].fatal_error("Expected 'extends'")
            else:
                del args[0]

        # TODO: the names of classes that this one extends
        self.extends = []

        blocker.Block.__init__(self, name, args, content)

        # whether or not this class is an api to C code
        self.is_api = is_api

    def __repr__(self):
        return f"{self.name} ({self.args}) {self.content} ENDBLOCK {self.name}"
    


def convert(tokens:tokenize.Tokens):
    # convert classes to special objects
    tokens = convert_classes(tokens)

    # convert functions to special objects
    # convert patterns to special objects
    
    return tokens


def convert_classes(tokens:tokenize.Tokens):
    i = 0
    n = len(tokens)
    while i < n:
        if str(tokens[i]) == "#BLOCK class":
            new_class = ClassBlock(tokens[i].name, tokens[i].args, tokens[i].content)
            tokens[i] = new_class
        elif str(tokens[i]) == "#BLOCK struct":
            new_class = ClassBlock(tokens[i].name, tokens[i].args, tokens[i].content, is_api=True)
            tokens[i] = new_class

        i += 1
    return tokens


