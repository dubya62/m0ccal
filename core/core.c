/**
 * The core of m0ccal.
 *
 * Definitions for everything that is required at the beginning of every converted m0ccal file
 *
 */

/*
Important functionality:
    Memory Manager
        Handle the memory space
    Dynamic Arrays
        Allow appending more items
        Only allow a single type of item
    Classes/Objects
    Int, Float, String, and Dictionary
*/

#include <stdio.h>
#include <stdlib.h>

typedef struct $_MemoryBlock{
    size_t size;
    size_t used;
    size_t remaining;
    size_t users; // the number of allocations made that have not been given back
    char* contents;
} $_MemoryBlock;

typedef struct $_MemoryManager{
    size_t numberOfBlocks;
    $_MemoryBlock* memoryBlocks;
} $_MemoryManager;

#define $_STARTMEMORY 4194304LLU

char $_MEMSPACE[$_STARTMEMORY];
$_MemoryManager $_MANAGER;


// Memory Manager methods

void $_INIT_MEMORY_HANDLING(){
    $_MANAGER.numberOfBlocks = 1;
    $_MANAGER.memoryBlocks = ($_MemoryBlock*) malloc(sizeof($_MemoryBlock));
    $_MANAGER.memoryBlocks[0].size = $_STARTMEMORY;
    $_MANAGER.memoryBlocks[0].contents = $_MEMSPACE;
    $_MANAGER.memoryBlocks[0].used = 0;
    $_MANAGER.memoryBlocks[0].remaining = $_STARTMEMORY;
}


void $_MemoryManager_newBlock($_MemoryManager* instance){
    /*
    Allocate a new memory block and add it to the collection
    */
    instance->memoryBlocks = realloc(instance->memoryBlocks, sizeof($_MemoryBlock) * instance->numberOfBlocks);

    instance->memoryBlocks[instance->numberOfBlocks-1].size = sizeof(char) * $_STARTMEMORY << (instance->numberOfBlocks-1);

    instance->memoryBlocks[instance->numberOfBlocks-1].contents = (char*) malloc(instance->memoryBlocks[instance->numberOfBlocks-1].size);
    instance->memoryBlocks[instance->numberOfBlocks-1].used = 0;
    instance->memoryBlocks[instance->numberOfBlocks-1].remaining = instance->memoryBlocks[instance->numberOfBlocks-1].size;
    instance->numberOfBlocks++;
}


void* $_MemoryManager_requestBlock($_MemoryManager* instance, size_t** memoryReturn, size_t bytes){
    /*
    Fill out a request for a memory block. If a large enough
    block does not exist, add a new block
    */
    $_MemoryBlock* theBlock = instance->memoryBlocks + (instance->numberOfBlocks-1);

    size_t remaining = theBlock->remaining;
    while (bytes > remaining){
        $_MemoryManager_newBlock(instance);
        theBlock = instance->memoryBlocks + (instance->numberOfBlocks-1);
        remaining = theBlock->remaining;
    }

    void* result = theBlock->contents + theBlock->used;
    theBlock->used += bytes;
    theBlock->remaining -= bytes;

    theBlock->users++;
    *memoryReturn = &(theBlock->users);

    return result;
}

void* $_MemoryManager_requestFakeBlock($_MemoryManager* instance, size_t realBytes, size_t fakeBytes){
    /*
    Give out region of memory large enough to perform calculations
    using fakeBytes, but once those calculations are over, leave 
    realBytes allocated
    */

    return NULL;
}




// TEST CODE 
int main(int argc, char** argv){
    $_INIT_MEMORY_HANDLING();

    size_t* memoryReturn;
    char* test = $_MemoryManager_requestBlock(&$_MANAGER, &memoryReturn, 10);

    test[0] = 'h';
    test[1] = 'i';
    test[2] = '\n';
    test[3] = '\0';

    (*memoryReturn)--;

    printf("%s", test);

    return 0;
}



