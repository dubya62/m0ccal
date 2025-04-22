# Specs

## Implementation
* As the name suggests, m0ccal will be implemented simply as a higher-level abstraction of C.
    * This should preserve C's efficiency while allowing better abstraction and modularity
* To achieve this, the current plan is to design a transpiler that simply converts m0ccal directly to an efficient C implementation after ensuring the program respects syntax, access specifiers, and guarantees.

## Paradigm
* m0ccal will be a mostly object oriented language where functions are not first-class citizens
* It will be very similar to Java but with slightly less verbose syntax, no generics in the traditional sense, the ability to write statements outside of classes, and not having to put all files in the same directory and name them the same as classes.

## Basic Syntax
* Allow unordered programming (can call/access before declared/defined)
* Built-in garbage collection
* Allow public, private, and protected
* Assume static or non static from whether or not a function uses *this*
    * Can only access instance variables using *this*, but *this* is never an argument in function headers
* Strong, inferred typing using *let*
* Multiple inheritance without generics
    * Everything inherits from Object 
        * even Integer, Float, and String
    * Functions accept their arg types and anything that inherits from their arg types:
```
class List:
    function append(Object obj){
        /*
            accepts an object of any type since
            everything inherits from Object
        */
    }

    function append(Int int){
        /*
            Whichever parent class is the closest to the
            passed object will be used
        */
    }
```

## Basis
* m0ccal will be based on blocking constructs:
```
// pythonic class
class Test:
    pass
     pass
    pass
```
and
```
// Javic class
class Test2 {}
```
should both be valid blocks in m0ccal.

* You should be able to switch between pythonic and Javic syntax
    * Notice that pythonic syntax does not care about indentation changes within a block as long as the indention level of a statement does not fall below the indention level of the first statement in that block

## Valid Blocks
* class block
    * `class Test{}`
* function block
    * `function Test{}`
* C block
    * `C {}`
        * Directly inline C code
        * Most of the language's complexity is in libraries rather than in the compiler
        * It is up to library writers to ensure safety, speed, and platform independence in the core libraries
* struct block
    * `struct Test{}`
        * A class block that does not get translated. Instead assumes that a C block already implements the class using the correct naming standard.
        * Allows the compiler to integrate C and m0ccal code seamlessly
* api block
    * `api testFunc{}`
        * A function block that does not get translated. Instead assumes that a C block already implements the function using the correct naming standard.
        * Allows the compiler to integrate C and m0ccal code seamlessly
        * Should probably design this to where it can have guarantees and assumptions in it
* testcase block
    * `|{}`
* debug block
    * `!{}` (LVL 1 debug) 
    * `!!{}` (LVL 2 debug)
    * `!!!{}` (LVL 3 debug)
    * `!!!!{}` (LVL 4 debug)
    * `!!!!!{}` (LVL 5 debug)
* guarantee block
    * `*{}` (moment guarantee)
        * If it is possible for any statement within to evaluate false, throw a compiler error
    * `**{}` (scope guarantee)
        * For the rest of this scope, if it is possible for any statement within to evaluate false, throw a compiler error
    * `***{}` (forever guarantee)
        * For the rest of the program, if it is possible for any statement within to evaluate false, throw a compiler error
* assumption block
    * `~{}` (moment assumption)
        * Assume that everything inside this block evaluates to true
    * `~~{}` (scope assumption)
        * For the rest of this scope, assume that everything inside this block evaluates to true
    * `~~~{}` (forever assumption)
        * For the rest of the program, assume that everything inside this block evaluates to true
    * `&{}` (documentation block)
        * Not sure I actually like this idea since there are already comments. Could be documentation that survives being converted to linkable object file or something.
    * pattern/match
        * An SML-like pattern matching block (match multiple variables at once)


## Guarantee motivating example
```
class BankAccount:
    let this.balance = 0.0

    // guarantee that there is no way 
    // for anything to cause the balance to
    // go negative

    ***:
        this.balance >= 0.0
```
* This syntax is subject to change since one might need to guarantee something about certain indices in an array
* In theory, this makes it impossible to ship out an executable with a bug that allows a negative balance

## Problem with guarantee
* If given some functions f(), g(x), and h(x) s.t. g(x) needs the guarantee that h(x) == True, then for the code segment:
```
// requires that h(f()) cannot be false
let result = g(f())
```
* The compiler must be able to prove that f() can only generate output s.t. h(f()) is true
* This is obviously going to be difficult (but not impossible) to write even a decent mathematical proving system just for this feature.
    * In some cases, might run into the halting problem trying to prove by counterexample
* Just throw an error if whatever proof system is in place cannot verify the guarantee
* Suggest editing the code to look like this:
```
function f(){
    ...
    // Assume that the result satisfies h(result) == true
    ~:
        h(result)
}
function g(Object x){
    *:
        h(x)
    ...
}
function h(Object x){
    ...
}
```
or offload the work to runtime like this:
```
function f(){
    ...
}
function g(Object x){
    if h(x):
        ...
    else:
        // put code here to handle when constraint fails
}
function h(Object x){
    ...
}
```
* The assumption block defeats the purpose of the guarantee block in cases where the proof system cannot prove the guarantee stands implicitly (hurts the safety of the program)
* As a best practice, you should only make assumptions when you are absolutely certain it is true 
    * For example: f = generate prime from sieve, h = isprime, and g is a function that requires a prime number. It is safe to assume that f() will only generate numbers x such that isprime(x) == true



