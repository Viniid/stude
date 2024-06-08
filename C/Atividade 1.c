#include<stdio.h>
//#include<windows.h> // delay na execução do programa usando win conta 1 milisegundo 1 seg é igual á 1000 milisegundo
#include<unistd.h> // delay na execução do programa usando linux e mac conta 1 segundo

int main(){

//1. Defina uma variável x, do tipo inteiro, e uma variável y, do tipo ponteiro de inteiro.
   printf("bem vindo ao passe de magica do ponteiro !\n");
   sleep(2);

    int x; 
    int *y;

//2. Usuário deverá informar o valor 25 à variável x.
   
    printf("Atribua o numero 25 para x!\n"); 
    sleep(2);
    printf("insira o numero:");
    scanf("%d", &x);


//3. Faça o ponteiro y apontar para o mesmo endereço da variável x.
   
    y = &x;

//4. Altere o valor armazenado no endereço de y para 12.
   
    *y = 12;  

//5. Execute a operação y = y + 1.
   
    y = y + 1;

//6. Some 5 ao valor armazenado no endereço de y.
  
    *y = *y + 5;

//7. Imprimir na tela: qual é o valor de x?

    printf("O valor de x é: %d.\n", x);
    sleep(2);
    printf("Essa magica é incrivel ");
    

}
