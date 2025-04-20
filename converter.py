
import blocker
from tokenize import Token, Tokens


class ClassBlock(blocker.Block):
    """
    class_name = ""
    extends = []
    is_api = True/False
    access = "public" | "private" | "protected"

    """
    def __init__(self, name, args, content, is_api=False, extends=[], access="protected"):
        self.name = name
        self.args = args
        self.content = content
        self.is_api = is_api
        self.extends = extends
        self.access = access

        self.variables = []
        self.instance_vars = []
        self.operators = []

    def __repr__(self):
        return f"{self.access} class {self.name} extends {self.extends}: {self.content} ENDBLOCK {self.name}"



class FunctionBlock(blocker.Block):
    """
    name = ""
    args = []
    content = []
    access = "public" | "private" | "protected"
    return_type = ""
    is_api = False

    """
    def __init__(self, name, args, content, is_api=False, return_type="Void", access="protected"):
        self.name = name
        self.args = args
        self.content = content
        self.is_api = is_api
        self.return_type = return_type
        self.access = access
        self.variables = []

    def __repr__(self):
        return f"{self.access} function {self.name} ({self.args}) -> {self.return_type}: {self.content} ENDBLOCK {self.name}"




def convert(tokens:Tokens):
    # create a new global scope class
    global_block = blocker.Block("$_GLOBAL", Tokens([Token("class")]), tokens.tokens)
    tokens.tokens = [Token(";"), global_block, Token(";")]

    # convert classes to special objects
    tokens = convert_classes(tokens)

    # convert functions to special objects
    tokens = convert_functions(tokens)

    # convert operator usage to function calls
    tokens = convert_operators(tokens)

    # TODO: convert patterns to special objects

    return tokens



def convert_classes(tokens:Tokens):
    # look for a class block
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == "#BLOCK":
            block = tokens[i]

            block.content = convert_classes(block.content)

            is_api = False

            if len(block.args) > 0:
                if block.args[0] != "class":
                    if block.args[0] == "struct":
                        is_api = True
                    else:
                        i += 1
                        continue
            else:
                i += 1
                continue
            
            del block.args[0]
            extensions = []

            # instead of expecting exactly one token, get everything between commas
            if len(block.args) > 0:
                if block.args[0] != "extends":
                    block.args[0].fatal_error("Expected extends or :")
                if len(block.args) == 1:
                    block.args[0].fatal_error("Expected type(s) after extends")
                del block.args[0]

                current_type = []
                while len(block.args) > 0:
                    if block.args[0] == ",":
                        extensions.append(current_type)
                        current_type = []
                    else:
                        current_type.append(block.args[0])
                    del block.args[0]

                if len(current_type) == 0:
                    block.name.fatal_error("Invalid extensions to class")
                extensions.append(current_type)

            # convert to special Block
            new_block = ClassBlock(block.name, block.args, block.content, is_api, extensions, block.access)
            tokens[i] = new_block
        i += 1

    return tokens



def convert_functions(tokens:Tokens):
    # look for a function block
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == "#BLOCK":
            if issubclass(type(tokens[i]), ClassBlock):
                tokens[i].content = convert_functions(tokens[i].content)
                i += 1
                continue

            block = tokens[i]
            is_api = False

            if len(block.args) == 0 and block.name not in ["init", "uninit"]:
                i += 1
                continue
            if block.name not in ["init", "uninit"] and block.args[0] not in ["function", "api"]:
                i += 1
                continue

            if len(block.args) > 0:
                if block.args[0] == "api":
                    is_api = True
                del block.args[0]
            
            # convert the function to a special block
            func_args:list[tokenize.Tokens] = []
            return_type:Token = Token("Void")

            # get the return type from the args
            if len(block.args) > 0:
                if len(block.args) != 3 or block.args[0] != "-" or block.args[1] != ">":
                    block.name.fatal_error("Bad return type")
                return_type = block.args[2]
            block.args.tokens = []

            # get the args in a way that does not throw an error with multi-token types
            argname = None
            argtype = []
            while block.inner_args is not None and len(block.inner_args) > 0:
                if len(block.inner_args) == 1 or block.inner_args[1] == ",":
                    argname = block.inner_args[0]
                elif block.inner_args[0] == ",":
                    if argname is None or len(argtype) == 0:
                        block.name.fatal_error("Function has Invalid args")
                    func_args.append(argtype + [argname])
                    argname = None
                    argtype = []
                else:
                    argtype.append(block.inner_args[0])

                del block.inner_args[0]

            if argname is not None:
                if len(argtype) == 0:
                    block.name.fatal_error("Function has Invalid args")
                func_args.append(argtype + [argname])
            else:
                if len(argtype) != 0:
                    block.name.fatal_error("Function has Invalid args")

            new_block = FunctionBlock(block.name, func_args, block.content, is_api, return_type, block.access)

            tokens[i] = new_block


        i += 1

    return tokens


def convert_operators(tokens:Tokens):
    """
    + __add__
    - __sub__
    / __div__
    * __mul__
    ** __pow__
    __log__ (for !, &&, and ||)
    % __mod__
    & __and__
    | __or__
    ~ __not__
    ^ __xor__
    () __call__
    [] __getitem__
    [] __setitem__
    == __eq__
    != __ne__
    < __lt__
    <= __le__
    > __gt__
    >= __ge__
    ++ __inc__
    -- __dec__
    """
    # convert operators to function calls
    return tokens




