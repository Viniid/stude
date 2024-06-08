#include<stdio.h>
#include<string.h>
#include<locale.h>

#define TAM 50 //constante

struct tipo_pessoa{
    int idade;
    float peso;
    char nome[TAM];
};

typedef struct tipo_pessoa tipo_pessoa;

int main(){

    setlocale(LC_ALL, "Portuguese");

    tipo_pessoa pes = {0, 0.0, "Teste"};

    printf("Inicio:\n");
    printf("pes.idade: %d\n", pes.idade);
    printf("pes.peso: %.2f\n", pes.peso);
    printf("pes.nome: %s\n", pes.nome);

    pes.idade = 32;
    pes.peso = 81.70;
    strcpy(pes.nome, "Texto Teste");
    
    printf("IAlterando os dados via codigo:\n");
    printf("pes.idade: %d\n", pes.idade);
    printf("pes.peso: %.2f\n", pes.peso);
    printf("pes.nome: %s\n", pes.nome);

    printf("Interação como usuario!\n");

    printf("\nInsira a idade:\n");
    scanf("%d", &pes.idade);
    printf("\nInsira o Peso\n");
    scanf("%.2f", &pes.peso);
    getchar();
    printf("\nInsira o Nome\n");
    scanf("%[^\n]s", &pes.nome);

    printf("\nDados alterados pelo usuário:\n");
    printf("pes.idade: %d\n", pes.idade);
    printf("pes.peso: %f\n", pes.peso);
    printf("pes.nome: %s\n\n", pes.nome);

}