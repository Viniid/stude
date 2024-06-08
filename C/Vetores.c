#include<stdio.h>

int main(){

    int v [5];                                           // Vetor

    float m;
    
    v[0] = 50;
    v[1] = 40;
    v[2] = 30;
    v[3] = 20;
    v[4] = 10;

    m = (v[0] + v[1] + v[2] + v[3] + v[4]) /5;

    printf("Resultado; %f\n", m);

    
    // ou


    int k[5] = {10, 20, 30, 40, 50}; // lista
    int j; // indice
    float s = 0;

    for(j=0; j<5; j++){       // adicona o indice
        s += k[j];
    }

    printf("Resultado> %f\n", s/5);
}