c

#define tamanho 3 //constante

struct tpilha{
    int dados[tamanho];
    int ini;
    int topo;
};
struct tipo_pilha pilha;

void push(int elemento){
    if(pilha.topo == tamanho){
        printf("Fila cheia. \n");
            //system("pause");
    }
    else
    {
        pilha.dados[pilha.topo] = elemento;
        pilha.topo++;
    }
        //printf("%d\n", pilha);
}
int desempilha(){
    int elemento;
    if(pilha.topo == pilha.ini){
        printf("Fila vazia.\n");
        system("pause");
    }
    else
    {
        pilha.topo--;
        elemento = pilha.dados[pilha.topo];
        return elemento;
    }
}