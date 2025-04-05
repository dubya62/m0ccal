
/*
This will serve as an example of resulting code
*/

/*
Allocate a large region of memory at compile time.
This memory will be used to store variables
*/
#define STARTING_MEMORY 4194304
char MEMSPACE[STARTING_MEMORY];

/*
class Test

classes should be defined as structs with a hashmap to represent their state/methods

Lists, Dictionaries, Ints, Strings, and Floats should be built on top of Dynamic Arrays

Dynamic Arrays should be built to allow easy doubling:
*/
typedef struct DynamicArrayHead{
    int length;
    int used;
    int startSize;
    void* arrayPointers[10]; // keeps track of all of the Dynamic Arrays held
} DynamicArrayHead;

typedef struct DynamicArray{
    int length;
    DynamicArrayHead* Head; // each node of the dynamic array has access to every node
    int headIndex; // this array's index in the head
    void* content;
} DynamicArray;
/*
Dynamic Array Memory Management
MEMSPACE
[DynamicArrayHead, Int, Float, Int, FirstBlock(256bytes), Int, Float, SecondBlock(256bytes), ThirdBlock(512bytes), Int, Float]
*/

/*
Be smart with memory management. Return values of functions are written in a place where they are safe from stack frame deallocation

If something cannot be saved from stack frame deallocation, copy it to a safe spot

Figure out the maximum amount of memory something may take and allow allocations after that if needed
*/

int main(int argc, char** argv){
}


