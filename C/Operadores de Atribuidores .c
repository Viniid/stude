#include<stdio.h>

int main(){

    int dado = 10;
    printf("Dados antes do incremento: %d.\n", dado);

    dado ++;
    printf("Dados depois do incremento: ++ %d.\n", dado);

    dado --;
    printf("Dados depois do decremento: -- %d.\n", dado);

    dado += 5;
    printf("Dados depois do incremento generico: += 5 = %d.\n", dado);

    dado -= 3;
    printf("Dados depois do decremento generico: -= 3 = %d.\n", dado);

    dado *= 2;
    printf("Dados depois do Atribuição com multiplicação: *= 2 = %d.\n", dado);

    dado /= 2;
    printf("Dados depois do Atribuição com divisão: /= 2 = %d.\n", dado);

}


