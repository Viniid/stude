#include<stdio.h>

// Conjunção "&&"
// Disjunção "||"
// Inversão "!"

int main(){

    float m;

    printf("Insira a nota: \n");
    scanf("%f", &m);

    if(m > 7.0 ){
        printf("Aprovado!\n");
    }

    else{
        printf("Foi reprovado !\n");
    }
    
}