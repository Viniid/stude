#include<stdlib.h>
#include<stdio.h>
#include<locale.h>
#include<string.h>

#define TAM 3

struct tipo_pessoa{
    int idade;
    float peso;
    char nome[50];
};

typedef struct tipo_pessoa tipo_pessoa;

int main(){

    setlocale(LC_ALL, "Portuguese");

    tipo_pessoa lista[TAM];
    int i;

    for(i=0; i<TAM; i++){

        printf("Insira os dados (%d):\n", i+1);
        puts("Nome: ");
        scanf("%50[^\n]s", &lista[i].nome);
        getchar();

        puts("Idade: ");
        scanf("%d", &lista[i].idade);
        getchar();

        puts("Peso: ");
        scanf("%f", &lista[i].peso);
        getchar();

    }
    system("cls");

    puts("Seus dados:\n");
    for(i=0; i<TAM; i++){
        printf("--------------------------- Pessoa %d ---------------------------\n", i+1);
        printf("\tNome: %s\n", lista[i].nome);
        printf("\tIdade: %d\n", lista[i].idade);
        printf("\tPeso: %.2f\n", lista[i].peso);
    }
    printf("---------------------------------------------------------------------\n");
}