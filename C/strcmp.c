#include<stdio.h>
#include<string.h>
#include<locale.h>

#define N 50 // constante ! facilita a manutenção da variavel!

int main(){
    setlocale(LC_ALL,"Portuguese");

    char hardText[N] = {"/exit"};
    char senha_user[N];

    printf("digite a senha:\n");
    fgets(senha_user,50,stdin);

    char ok = strcmp(hardText, senha_user);
    
    if(ok == 0)
        printf("Textos iguais.\n");
    else
        printf("Texto diferente.\n");


}
