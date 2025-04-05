# Easy Programming Language (EPL)
* A compiled programming language that should be geared towards very quick development
* It's syntax should be even easier to understand than python

## Features
* It should compile files to "object" files so that compilation goes faster by just linking
* Object files should still hold relevant documentation so that you can easily use libraries
* There should be built-in live debugging
* By default, it should be able to use dynamic primitives and data structures
* You should be able to easily define several test cases for a function that make testing significantly faster
    * Make a mode for the compiler that simply runs the test cases every time one of the files changes
    * Having this open in another window would make development much faster
* Allow very strong pattern matching switch-case statements
    * Should be able to do something like sml functions here
    * Pattern matching across several variables
* Should have a very good preprocessor that allows modifying aspects of the language itself

## Modularity
* EPL should make modularity extremely easy
* EPL will allow object oriented code

## Syntax
* EPL's syntax should be even more human readable than python's
* Require strong typing, but allow infering types if not stated
```
let x: int = 2
```
* Allow kwargs
* Allow ints, strings, floats, dynamic arrays, dictionaries, sets, stacks, queues
* Allow overloading functions based on arg types
* Allow calling functions above where they are defined
* Allow built-in test cases and documentation
* You can define operators just like functions. 
    * reversible binary operator precendence +(int first, int second)
    * You can define if it is reversible or not
    * Allow unary or binary keyword
    * reversible unary operator 1 - (int first)
* Like javascript, you can pass functions around like objects or add a function to an instance of an object
* Allow for-loops by reference
* Allow function call by reference (refof)
* There should be a way that defines how the code will be translated to C
    * This would allow the language to do basically anything
    * This would allow platform independence
    * This would move a lot of functionality from the compiler directly into the standard libraries

## Keywords
```
class, extends
public, private, protected
reversible, unary, binary
refof
let
return

```

## Syntax Rules
* To define a class, use 'class' followed by a unique name. The name must start with an uppercase letter
    * The class name can be followed by 'extends'
    * If using 'extends', expect one or more class names separated by ','
    * Now expect ':' to end the line
    * Everything within the indention level/braces of the class is now a member of that class
* To define a function, start with the function's name, followed by (in order):
    * optional access specifier 'public', 'private', or 'protected'
    * required parenthesis containing args
    * optional ->
        * if present, require the return type after
        * if not present, the return type is assumed Null
* To define an operator, start with the operator's name, followed by (in order):
    * optional access specifier 'public', 'private', or 'protected'
    * optional 'reversible'
        * if not present, is not reversible
    * optional 'unary' or 'binary'
        * if not present, assume binary
    * required 'operator'
    * required precedence value
    * required parenthesis with args inside
        * Exaclty 0 args if unary
        * Exactly 1 arg is binary
* C block 'C{}'
    * 'C' keyword followed by
    * braces with C code inside
* Comments:
    * // for single line comment
    * `/* */` for multi-line comment
* Api to C code
    * function name
    * optional access specifier 'public', 'private', or 'protected'
    * 'api' keyword
    * args inside parenthesis
    * optional -> and return value
* Test cases |:
    * start with required pipe '|' 
    * optional test name
    * optional arrow
    * optional passed text or underscore
    * optional failed text or underscore
    * required ':'
    * last line of the test will evaluate to either true or false to pass/fail the test
* Allow adding functions to be called once a function is over
    * updateDisplay.addCallback(self.onUpdate)
    * `updateDisplay => self.onUpdate`
* Allow exposing private/protected functions easily
    * expose private (via) getters/setters to public
    * expose private (via) getters/setters to protected
* Allow trusting another class with access to a private/protected variable/function
* @F() converts to a call to the function you are currently in
* &: starts a documentation block
* \*: constraint (throws compile-time error if violated)
* ~: compiler should assume the following (possible values for result)
* @F converts to the name of the function you are currently in
* @C converts to the name of the class you are currently in
* @A converts to the absolute filepath you are at
* @R converts to the relative filepath you are at
* @1, @2, ..., @-1, @n convert to that argument of the function you are currently in
* @# converts to the number of arguments to this function
* @? converts to a random number [0, 1)
* @S Starts a timer (accessed with @E)
* @E returns the amount of time since the last @S was encountered
* @V converts to a Dictionary of all variables in available in this scope
* @T time since this function started
* @M returns the members of this object as a Dictionary
* @^ converts to the args of the function you are currently in as a List
* @< converts to the args of the function you are currently in as a Dictionary
* @> converts to the return type of the function you are currently in
* @L converts to the current line number
* @G converts to True if in the global scope or false otherwise
* @Z converts to True if this is the file the compiler was called on
* !: Debug print level 1
* !!: Debug print level 2
* !!!: Debug print level 3
* !!!!: Debug print level 4
* !!!!!: Debug print level 5
* init and uninit are understood as functions when in class
    * can just use init or uninit with parenthesis (or without if no args)

* B, D, H, I, J, K, N, O, P, Q, U, W, X, Y
* A, C, F, R, S, E, V, T, M, L, G, Z


## Preprocessor
* Allow strong definition stuff like C does


## Idea
* Make the language extremely simple
* The complexity should be defined explicitly in the standard libraries


## Process
* Perform Lexing
* Remove comments
* Preprocess
* Convert indention to braces
* Convert Blocks to objects
* Perform constraint checking
* Convert Classes to Structs
* Convert Methods to functions that operate on structs



