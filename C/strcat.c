#include<stdio.h>
#include<string.h>
#include<locale.h>

#define N 20 // constante ! facilita a manutenção da variavel!

int main(){
    setlocale(LC_ALL,"Portuguese");

    char s1[N] = {"Logica de "};
    char s2[N] = {"Programação!"};

    printf("antes do strcat:\n");
    printf("str1: %s\n", s1);
    printf("str2: %s\n", s2);

    strcat(s1,s2);

    printf("Depois do strcat: \n");
    puts(s1);
    //puts(s2);

}