
from converter import ClassBlock, FunctionBlock
import blocker
from tokenize import Token, Tokens
from grapher import Graph


def check_syntax(tokens:Tokens):
    # Make sure that each scope only has 1 definition of classes
    tokens = ensure_class_singularity(tokens)

    # For each class, figure out what all static and instance variables need to be allocated
    find_class_variables(tokens[1])

    # Make sure that each scope only has 1 definition of functions with the same number and types of args
    ensure_function_singularity(tokens)

    # fix the . class to be a special $ class
    fix_dot_classes(tokens)

    # TODO: if the class was imported, it cannot access stuff from the global scope

    # TODO RN: Make all references to objects, functions, and states point to their definition
    parent_node = Graph(None, None)
    create_graph(tokens, parent_node)
    point_references(tokens, parent_node)

    def pgraph(graph:Graph):
        print(graph.data)
        print(graph.children)
        [pgraph(x) for x in graph.children.values()]
    #pgraph(parent_node)

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
            else:
                the_block.variables.append(the_name)
        i += 1


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

            if func_id in found_funcs:
                tokens[i].name.fatal_error(f"Function {tokens[i].name} with args {tokens[i].args} was already defined in this scope")

            found_funcs.add(func_id)
        i += 1


def fix_dot_classes(tokens:Tokens):
    """
    let x = ..Test2()
    =>
    let x = $DOT_CLASS.$DOT_CLASS.Test2()

    if token before is an operator or the start of the line, insert a $DOT_CLASS
    """
    operators = set([
        "+", "-", ":", "=", "<", ",", ">", ";", "/", "?", "!", "and", "or", "not", "^", "%", "&", "|", "*", "(", "["
        ])
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == "#BLOCK":
            fix_dot_classes(tokens[i].content)
        elif tokens[i] == "." and i > 0 and tokens[i-1] in operators:
            tokens.insert(i, Token("$DOT_CLASS"))
            i += 1
            n += 1
        i += 1


def create_graph(tokens:Tokens, graph:Graph):
    # Make all references to variables/types/functions point to their declaration
    # create the graph
    i = 0
    n = len(tokens)
    while i < n:
        if tokens[i] == "#BLOCK" or (i > 0 and tokens[i-1] == "let" and tokens[i] != "this"):
            the_name = tokens[i]
            if tokens[i] == "#BLOCK":
                the_name = tokens[i].name

            new_graph = Graph(tokens[i], graph)
            graph.children[the_name] = new_graph

            # if this is a function, add the args as children
            if issubclass(type(tokens[i]), FunctionBlock):
                for arg in tokens[i].args:
                    graph.children[arg[-1]] = Graph(arg[-1], new_graph)

            if tokens[i] == "#BLOCK":
                create_graph(tokens[i].content, new_graph)
        i += 1


def point_references(tokens:Tokens, graph:Graph):
    print(f"Pointing references {graph.data}")
    if graph.data == "#BLOCK":
        # point references in the content
        the_block = graph.data
        i = 0
        n = len(the_block.content)
        while i < n:
            # TODO: somehow find all identifiers for linking
            i += 1

    # point references in all children
    for x in graph.children.values():
        point_references(tokens, x)


