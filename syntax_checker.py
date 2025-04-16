
from converter import ClassBlock, FunctionBlock
import blocker
from tokenize import Token, Tokens

def check_syntax(tokens:Tokens):
    # Make sure that each scope only has 1 definition of classes
    tokens = ensure_class_singularity(tokens)

    # For each class, figure out what all static and instance variables need to be allocated
    find_class_variables(tokens[1])

    # Make sure that each scope only has 1 definition of functions with the same number and types of args
    ensure_function_singularity(tokens)

    # TODO RN: Make all references to objects, functions, and states point to their definition
    

    # TODO RN: Make calls to class names reference the init function instead

    # TODO RN: Make sure that all accesses follow access specifiers

    # TODO RN: Remove all access specifiers


    # TODO RN: Disambiguate function calls based on input arg types

    return tokens


def ensure_class_singularity(tokens:Tokens):
    class_names = set()
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == "#BLOCK":
            tokens[i].content = ensure_class_singularity(tokens[i].content)
        if issubclass(type(tokens[i]), ClassBlock):
            if tokens[i].name in class_names:
                tokens[i].fatal_error(f"Class {tokens[i].name} is defined multiple times in this scope")
            class_names.add(tokens[i].name)
        i += 1

    return tokens


def find_class_variables(the_block:blocker.Block, parent_block=None):
    i = 0
    n = len(the_block.content)
    while i < n:
        if the_block.content[i] == "#BLOCK":
            find_class_variables(the_block.content[i], the_block)
        if the_block.content[i] == "let":
            # This is the declaration of a local variable
            if i + 1 >= n:
                the_block.content[i].fatal_error("Expected variable name after let")

            the_name = the_block.content[i+1]

            if the_name == "this":
                # throw an error if this is not the init block
                # if it is in the init block, add it to the parent class' instance variables
                if the_block.name != "init" or not issubclass(type(the_block), FunctionBlock):
                    the_block.content[i+1].fatal_error("Cannot declare an instance variable outside of the init function")
                if i + 3 >= n or the_block.content[i+2] != ".":
                    the_block.content[i+1].fatal_error("Expected valid variable name for instance variable")
                the_name = the_block.content[i+3]
                if parent_block is None or not issubclass(type(parent_block), ClassBlock):
                    the_block.content[i+3].fatal_error("Cannot declare instance variable when init function is not directly inside a class")
                parent_block.instance_vars.append(the_name)
                print(f"Instance var: {the_name}")
            else:
                the_block.variables.append(the_name)
        i += 1
    print(f"{the_block.name}: {the_block.variables}")


def ensure_function_singularity(tokens:Tokens):
    # make sure that each scope only has unique function name-type pairs
    found_funcs = set()

    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == "#BLOCK":
            ensure_function_singularity(tokens[i].content)
        if issubclass(type(tokens[i]), FunctionBlock):
            arg_id = "$".join(["".join([y.token for y in x[:-1]]) for x in tokens[i].args])
            func_id = f"{tokens[i].name}-{arg_id}"
            print("FUNCID")
            print(func_id)

            if func_id in found_funcs:
                tokens[i].name.fatal_error(f"Function {tokens[i].name} with args {tokens[i].args} was already defined in this scope")

            found_funcs.add(func_id)
        i += 1

