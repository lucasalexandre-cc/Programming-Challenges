#include <stdio.h>
int main(void)
{
    char string[1000];
    while(scanf("%s",string) != EOF) {
        int i;
        int cont = 0;
        for (i = 0; string[i] != '\0'; i++) {
            if (string[i] == '(') cont++;
            else if (string[i] == ')') cont--;
            if (cont < 0) {
                break;
            }
        }
        if (cont == 0) printf("correct\n");
        else printf("incorrect\n");
    }
    return 0;
}