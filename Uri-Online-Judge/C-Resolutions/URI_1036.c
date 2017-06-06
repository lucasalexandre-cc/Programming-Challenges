#include <stdio.h>
#include <math.h>

int main() {
 
    double A,B,C;
    scanf("%lf",&A);
    scanf("%lf",&B);
    scanf("%lf",&C);

    double delta = pow(B,2) - 4*A*C;

    if(delta < 0 ||  A == 0){
        printf("Impossivel calcular\n");
    }else{
        printf("R1 = %.5lf\n",(-B + sqrt(delta))/(2*A));
        printf("R2 = %.5lf\n",(-B - sqrt(delta))/(2*A));
    }

 
    return 0;
}