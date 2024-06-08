#include<stdio.h>
#include<string.h>
#include<locale.h>

#define N 20 // constante ! facilita a manutenção da variavel!

int main(){
    setlocale(LC_ALL,"Portuguese");

    char origem[N] = {"Olá, mundo!"};
    char destino[N] = {"-"};

    printf("antes do strcpy:\n");
    puts(origem);
    puts(destino);

    strcpy(destino,origem);

    printf("Depois do strcpy: \n");
    puts(origem);
    puts(destino);

}


