#include<stdio.h>

int main(){

    int i;

    for(i=1; i<=10; i++){
        printf("%d ", i);
        if(i == 5){
            break; // encerra o processo de repetição independente de onde esteja !
        }
    }
 

    int j;

    for(j=1; j<=10; j++){
        
        if(j == 5){
            continue;
        }

        printf("\n %d \n", j);
    }
}