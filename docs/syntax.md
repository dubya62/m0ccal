# Syntax

## Primitives
* **EVERYTHING** (including primitives) is an object
    * Float
    * Int
    * String

## Lines
* Semicolons are optional
    * Required to separate multiple statements on the same line
* Within pythonic blocks, the scope ends when the indention level falls below the indention level of the first statement
* Extra whitespace does not matter (in most cases)

## Preprocessor Directives
```
// requires ./test.ccal
#import test
// requires ../../testing.ccal
#import ..testing

// something like this for archive/object files
#link test
```
* Only import once to prevent circular imports
* Use imports as if they are classes
    * `let result = ..testing.Test();`
* There is no *from* or *as* for imports
    * There are *use as* statments to replace this
* Other directives can be added later if needed

## Use-as
```
// assume test.ccal has a class named TestClass with function testFunc
#import test

use tc as test.TestClass.testFunc;

tc();
```
* Basically an alias that is scope aware (happens after preprocessing)

## C blocks
* Literally just inline C code.
* Needs to be ignored by most of the compilation process and just inserted into the resulting C code.

## Classes
```
protected class Test extends Test1, Test2:
    pass
```
* Pretty standard

## Functions
```
protected function testFunc(Int input1, String input2) -> ReturnType:
    return ReturnType()
```
* Also pretty standard
* The arrow syntax might need to change
* Also might want to assume the function keyword for less verbosity


# ADITIONAL SYNTAX COMING SOON


