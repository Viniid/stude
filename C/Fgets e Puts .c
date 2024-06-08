#include<stdio.h>

int main(){

    char s[10];

    printf("Digite algo (leitura pelo fgets):\n");
    fgets(s,10,stdin);
    getchar();

    puts("Resultados:");
    puts(s);
    puts("");
}