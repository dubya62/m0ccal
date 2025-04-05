
# Memory Management
* MemoryManager contains functionality for allocation/deallocation
    * allocate(bytes)
    * free(ptr)

## Lexer example
```
[Lexer Object, Lexer State Dictionary, init function, lex function, openFile function, breakIntoTokens function, String filename]

init can be directly given the reference to String filename
filename can be directly added to the state dictionary
String filename can be given directly to lex instead of copied
String filename can be given directly to openFile instead of copied

```

## Process
* Find last possible place that a memory region can be referenced from
* After that point, it is fine to write over it
* Design an object code format that uses abstract memory accesses
    * When the object files are "linked", handle whether or not memory should be allocated statically or dynamically


