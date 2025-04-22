# Welcome to m0ccal
* Modular 0-Cost C Abstraction Language

## Motivation
* C is my favorite language for its speed, pointer magic, and (relative) simplicity.
* C is also my least favorite language for its runtime errors, having a single namespace, and terrible support for libraries.
* I think there is some room for improvement by creating a programming language with these [specs](specs.md).
* The first version of the transpiler should be somewhat simple with potential to make more [complex features](problems.md) while the language's complexity remains the same.

## Desired Final Result
* A language with C's speed and control without its difficulty
* A language with extremely simple syntax
    * Only the bare essential syntax is allowed
    * Anyone that is a week into learning programming should be able to look at an arbitrary program and know what it does (given the author used good naming conventions)
    * The complexity that is required to solve hard problems should be implemented in the standard/user libraries as classes and functions
* A language that has a (pretty much) 0% chance to encounter runtime errors
    * Anything that could possibly throw an error should throw its error at compile time
        * If it is possible for the program to access an index outside of an array, throw an error
        * This will require a complex guarantee/assumption/proof system in the compiler
        * This should also make the programming language extremely safe and fast
    * The compiler should have an option (undecided if opt-in or opt-out yet) that gives extremely verbose error messages
* A language that is platform independent
* A language that integrates efficient testing and documentation constructs
* A language designed for modularity and a strong package ecosystem
* A language that works with the programmer to modularize and test things 
    * probably should be implemented in IDEs or interactive compiler/debugger

## Good and Bad features to include/exclude from other languages
### Good
* Python
    * Magic methods for operators (allowing overloading)
    * Arbitrary length Arrays and Strings and arbitrary precision Integers and Floats
        * Inefficient, but really help in some real-world problems
    * Multiple inheritance
    * Class and Function nesting
* C
    * Speed
    * Manual memory management 
        * m0ccal compiler will handle this via GC
    * Good support for bit hacking algos
    * Preprocessor directives
* Java
    * Designed for modularity
    * Ability to easily modify code that is already compiled 
        * allow calling m0ccal code like an api while respecting access specifiers
    * Allows method overloading based on arg types (I think)
* SML
    * Pattern matching

### Bad
* Python
    * dynamic typing
* C
    * Syntax can be hard to read
    * Runtime errors
* Java
    * Slightly too verbose
    * Import system and generics seem trash
    * I have to have 4 different versions to run 4 different programs





