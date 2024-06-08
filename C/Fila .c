#include <stdio.h>
#include <stdlib.h>

#define tamanho 3

struct tipo_fila{
    int dados[tamanho];
    int ini;
    int fim;
};

struct tipo_fila fila;

void push_back(int elemento){
    if(fila.fim == tamanho){
        printf("Fila cheia.\n");
        system("pause");
    }
    else
    {
        fila.dados[fila.fim] = elemento;
        fila.fim++;
    }
}

int desnfileira(){
    int(fila.fim == fila.ini){
        printf("fila vazia. \n");
        system("pause");
    }
    else
    {
        elemento = fila.dados[fila.ini];
        for(int i=0; i<tamanho; i++)
            fila.dados[i] = fila.dados[i+1];
        fila.dados[fila.fim] = 0;
        fila.fmi--;
        return elemento;
    }
}