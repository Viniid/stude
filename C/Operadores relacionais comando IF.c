#include<stdio.h>

// Conjunção "&&"
// Disjunção "||"
// Inversão "!"

int main(){

    float m;

    printf("Insira a nota: \n");
    scanf("%f", &m);

    if(m >= 4.0 && m < 6.0){
        printf("Tem direito a exame!\n");
    }

  //  else{
   //     printf("Foi reprovado !\n");
    //}
    printf("Foi Aprovado!\n");
}
