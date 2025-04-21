# How to perform Constraint checking reliably without checking every single value


```
Test public class:
    isprime public function(Int n) -> Bool:
        ~: 
            n = ANY
        if n & 1 == 0:
            ~:
                n & 1 == 0
            return False
        ~:
            n & 1 != 0
        d = 3
        ~:
            n & 1 != 0
            d = 3
        while d * d <= n:
            ~:
                n & 1 != 0
                d = 3 or 5 or 7
            if n % d == 0:
                ~:
                    n % d == 0
                    n & 1 != 0
                    d = 3 or 5 or 7
                    (d == 1) == 0
                return d == 1
            ~:
                n % d != 0
                n & 1 != 0
                d = 3 or 5 or 7
            d= d + 2
            ~:
                n % d != 0
                n & 1 != 0
                d = 5 or 7 or 9
        return n == 1

    getNValue(Int p, Int q) -> Int:
        // require that p and q are prime
        /* This could cause the compiler to perform calculations forever 
            Should terminate after a while and throw a compile time error telling to 
            use an if statement instead of a compile-time constraint for this problem
        *:
            isprime(p)
            isprime(q)
        */
        if isprime(p) and isprime(q):
            // We now know that p and q have passed isprime
            ~:
                isprime(p)
                isprime(q)
            return p * q;

```
`./testProgram 77 19`
* Given that p and q can be any integers, the program needs to know at compile time if it is possible for isprime(p) or isprime(q) to return False
* Look for possible values of p s.t. isprime(p) returns False


* Given a function f(int x) -> Bool
* Given a function g(int x, int y) -> int with constraints: f(x) and f(y) are True
* if x and y are bounded, you could check all possible values
* if x and y are unbounded, you can look for a contradiction and throw error if contradiction found
    * Can run forever if no contradiction exists
    * Need a way to prove that for any value x, f(x) is True to pass the constraint correctly

## Execution
* p and q can be anything
* isprime(p):
    * fails x > 0 because it could be negative
* if isprime(p) returns False for any value that p could be, fail
* if isprime(p) could return False for any value that p could be, fail
        

## What does it mean if no contradiction exists?
* There is an infinite number of possible inputs
* The infinite inputs do not violate the constraints of the function (you cannot tell if they return False after too long of a search)

## But is it possible to get infinite inputs without getting all possible inputs?
* Create a function that generates an infinite number of prime numbers and input the resulting numbers into a function with isprime constraint
* Since we have the prime number generator, as long as it cannot generate a number that returns False, it passes the constraint
* Now we have to prove that the prime generator generates only numbers accepted by the isprime function
    * One way is to assume isprime(result) right before the return in the prime generator

## New idea
* Convert all while and for loops to recursive functions for proofs
* Now the assumptions do not change because there is no backward jump
* Not sure that this actually reduces complexity since the recursive calls will have different assumptions

## Newest Idea
* Try to use several proof solving methods where needed
* If all attempts fail, throw an error telling the user to either make an assumption or replace a constraint with an if statement





