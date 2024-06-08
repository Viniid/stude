#include<stdio.h>
#include<stdlib.h>

int main(){

    int *p;
    p = (int *) malloc(4); // 4 bytes

    if(p == NULL){
        printf("Erro!\n");
    }
    else{
        *p = 10;
        printf("p: %d\n", *p);
        free(p);
        printf("p: %d\n", *p);
    }

}