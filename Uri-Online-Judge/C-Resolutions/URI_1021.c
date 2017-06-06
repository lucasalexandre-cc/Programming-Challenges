#include <stdio.h>
 
int main() {
 
    double valor;
    int notas[6] = {100,50,20,10,5,2};
    scanf("%lf",&valor);
    printf("NOTAS:\n");

    int i,x;
    for(i = 0; i<6;i++){
        x = valor/notas[i];
        printf("%i nota(s) de R$ %i.00\n",x,notas[i]);
        valor -= x*notas[i];
    }

    printf("MOEDAS:\n");
    valor *= 100;
    notas[2] = 25;
    notas[5] = 1;
    for(i = 0; i<6;i++){
        x = (int)(valor)/notas[i];
        printf("%i moeda(s) de R$ %.2lf\n",x,notas[i]/100.00);
        valor -= x*notas[i];
    }
    return 0;
    
}