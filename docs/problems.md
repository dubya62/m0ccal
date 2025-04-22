# Problems

## Things the transpiler should handle
* Checking syntax and access specifiers
* Keeping track of possible values of variables and verifying guarantees
* Making the unordered program use C's ordering requirements
* Managing memory
    * The compiler should figure out the last possible place an object can be referenced
    * Use this information to efficiently handle dynamic memory allocations
    * Use bump allocation and arenas?
    * Since everything is handled at compile time, try to perform some memoization?
    * Probably a problem for later.
* Handling naming collisions and overloading
    * Do not allow $ in function names in m0ccal
    * When converting to C, use $ where needed so that naming collisions are impossible
* Throw meaningful error messages
* Performing a basically 1:1 mapping to C and calling the correct C compiler(s)



