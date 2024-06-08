#include<stdio.h>

int main(){

    int idade = 0;
    int ano = 0;
    float peso = 0.0;

    printf("Valor inicial da idade, ano e peso: %d. %d. %.1f. \n", idade, ano, peso);

    printf("Digite uma idade e o ano:\n");
    scanf("%d %d", &idade, &ano);

    printf("Digite o peso:\n");
    scanf("%f", &peso);

    printf("Idade informada: %d. \n", idade);
    printf("Ano informado: %d. \n", ano);
    printf("Peso informado; %.1f. \n", peso);

}