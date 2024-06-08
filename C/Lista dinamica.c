#include<stdio.h>
#include<stdlib.h>

int main(){

    void imprimir (struct NO* ptr){
        system("cls");
        while(ptr != NULL){
            printf("%d ", ptr->dado);
            ptr = ptr->prox;
        }
    }
}