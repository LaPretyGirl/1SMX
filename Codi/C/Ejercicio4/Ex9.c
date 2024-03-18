#include <stdio.h>
#include <string.h>

int main() {
    char cadena1[100];
    char cadena2[100];
    char cadenaConcatenada[200];

    printf("Ingrese la primera cadena: ");
    scanf("%s", cadena1);

    printf("Ingrese la segunda cadena: ");
    scanf("%s", cadena2);

    strcpy(cadenaConcatenada, cadena1);
    strcat(cadenaConcatenada, cadena2);

    printf("Cadena resultante: %s\n", cadenaConcatenada);

    return 0;
}
