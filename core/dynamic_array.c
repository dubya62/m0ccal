
#include <stdio.h>
#include <stdlib.h>

typedef struct DynamicArrayNode{
    size_t size;
    size_t used;
    size_t memberSize;
} DynamicArrayNode;

typedef struct DynamicArray{
    size_t numberOfNodes;
    DynamicArrayNode* nodes;
} DynamicArray;


void DynamicArray_init();
void DynamicArray_uninit();
void DynamicArray_append();
void DynamicArray_getItem();
void DynamicArray_setItem();


