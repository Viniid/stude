#include<stdio.h>
#include<string.h>
#include<locale.h>

#define N 20 // constante ! facilita a manutenção da variavel!

int main(){
    setlocale(LC_ALL,"Portuguese");

    char s[N];
    int i;

    printf("Digite um texto:\n");
    fgets(s,20,stdin); // no linux este codigo não é permitido pois o gets não está na biblioteca
    i = strlen(s);
    printf("\nTamanho do texto: %d\n\n", i);


    //printf("Impressão de posição a posição:\n");
    //for(i=0; i <= strlen(s); i++){
        //printf("%c", s[i]);
    //}
    puts(s);
}