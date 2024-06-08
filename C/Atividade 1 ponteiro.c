#include<stdio.h>

int main(){

//1. Defina uma variável x, do tipo inteiro, e uma variável y, do tipo ponteiro de inteiro.
   
    int x; 
    int *y;

//2. Usuário deverá informar o valor 25 à variável x.
   
    printf("Insira o numero 25.\n");
    scanf("%d", &x);

//3. Faça o ponteiro y apontar para o mesmo endereço da variável x.
   
    y = &x;

//4. Altere o valor armazenado no endereço de y para 12.
   
    *y = 12;  //quando se trata de um endereço é necessario acrescentar "*"

//5. Execute a operação y = y + 1.
   
    y = y + 1;

//6. Some 5 ao valor armazenado no endereço de y.
  
    *y = *y + 5;

//7. Imprimir na tela: qual é o valor de x?

    printf("O valor de x é: %d.\n", x);

}
