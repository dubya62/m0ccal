#include <stdio.h>
#include <stdlib.h>

typedef struct File{
    FILE* fp;
} File;

typedef char* String;

File* open(String filename, String mode){
    FILE* fp = fopen(filename, mode);
    File* result = malloc(sizeof(File));
    result->fp = fp;
    return result;
}

void close(File* instance){
    fclose(instance->fp);
}

String read(File* instance, size_t bytes){
    char* result = malloc(sizeof(char) * bytes + 1);
    fread(result, sizeof(char), bytes, instance->fp);
    result[sizeof(char) * bytes] = '\0';
    return result;
}

void write();
void truncate();


int main(int argc, char** argv){
    File* test = open("compiler.ccal", "r");

    printf("%p\n", test->fp);

    String result = read(test, 100);
    printf("%s\n", result);

    close(test);

    return 0;
}

