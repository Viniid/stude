#include<stdio.h>


int main(){

    char s[10];

    printf("Digite algo (scanf convencional):\n");
    scanf("%s", s);
    getchar ();  // fflush(stdin); do linux

    printf("Resultado: %s\n\n", s);

    printf("Digite Algo (scnaf aprimorado):\n");
    scanf("%10[^\n]s", s);
    getchar (); // fflush(stdin); do linux

    printf("Resultado: %s\n\n", s);

}
