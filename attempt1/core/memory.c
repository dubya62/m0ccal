// Task: Create a memory management system that is as efficient as possible
//
// Use bit hacking to make management take as few cycles as possible
// arbitrary precision/length objects will use doubling
//
//
// Things to allow:
//      allocate memory
//      free memory
//      double allocation size
//      use arenas for speed
//
// Use size_t to hold allocation information
//      00001111
//      11111111
//      00001111
//      11111111
//      00001111
//      11111111
//      00001111
//      11111111
//      
// Give allocated pointers a deallocation mask to &= with the allocation information
//      11111101
//      10111011
//      11111111
//      11111110
//      11111111
//      11111101
//      11111111
//      11111101
//
// 
//

// best way to efficiently allocate memory
// Use arenas to hold multiple variables and use bumping
// Can easily extend the size of the arena
// Just wait until everything in the arena is guaranteed to be deallocated before deallocating the arena
// Design the size_t just right so that each one holds a certain number of arenas. Give arenas a max size that is larger than any system should be able to achieve in the wild (4 TB of memory is probably enough right?)

// Arena sizes
// 1. 2 K
// 2. 4 K
// 3. 8 K
// 4. 16 K
// 5. 32 K
// 6. 64 K
// 7. 128 K
// 8. 256 K
// 9. 512 K
// 10. 1 M
// 11. 2 M
// 12. 4 M
// 13. 8 M
// 14. 16 M
// 15. 32 M
// 16. 64 M
// 17. 128 M
// 18. 256 M
// 19. 512 M
// 20. 1 G
// 21. 2 G
// 22. 4 G
// 23. 8 G
// 24. 16 G
// 25. 32 G
// 26. 64 G
// 27. 128 G
// 28. 256 G
// 29. 512 G
// 30. 1 T
// 31. 2 T
// 32. 4 T

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// if there is not a memory issue, just be extremely aggressive and put everything in the same arena - never free anything
// if there is a memory constraint, just allocate in separate arenas and destroy them when it is safe to do so


// create arenas to hold different scopes
// to deallocate the arena, simply mark its sections as free memory
// to allocate within the arena, use a bump allocator

// need a way to handle arenas whose maximum size is unknown at compile time

// how to divy up memory so that arena size can grow without preallocating all of that memory?


// At compile time, create the correct number of arenas to make the program efficient
// Make the arena sufficiently large enough to hold all of the data

typedef struct MemoryBlock{
    size_t allocated;
    void* data;
} MemoryBlock;


typedef struct MemoryManager{
    MemoryBlock blocks[5];
} MemoryManager;


MemoryManager manager;

void initManager(){
    size_t blockSize = 32 * sizeof(size_t) * 8;
    printf("Block Size: %lu\n", blockSize);
    for (int i=0; i<5; i++){
        manager.blocks[i].allocated = 0;
        manager.blocks[i].data = malloc(blockSize);
    }
}

void* evil_malloc(size_t bytes){
    manager.blocks[0].allocated |= (1LU << (sizeof(size_t) * 8 - 1));
    printf("Allocated: %lu\n", manager.blocks[0].allocated);
    return manager.blocks[0].data;
}

void evil_free(void* ptr){
    manager.blocks[0].allocated = 0;
    printf("Allocated: %lu\n", manager.blocks[0].allocated);
}


int main(int argc, char** argv){
    printf("++++++++++++++++++++++++++++++\n");
    printf("Allocating 25 bytes...\n");

    initManager();

    char* testString = evil_malloc(25);
    for (int i=0; i<24; i++){
        testString[i] = 'a';
    }
    testString[24] = '\0';

    printf("%s\n", testString);

    evil_free(testString);

    return 0;
}


