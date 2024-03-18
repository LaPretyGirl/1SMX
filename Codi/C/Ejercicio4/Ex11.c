#include <stdio.h>

int main() {
    int numeroSecreto = 42;  
    int intentos = 5;  
    int intento;
    int acertado = 0;

    printf("Bienvenido al juego de adivinanza!\n");
    printf("Tienes 5 intentos para adivinar un número del 1 al 100.\n");

    while (intentos > 0) {
        printf("Intento %d: ", 6 - intentos);
        scanf("%d", &intento);

        if (intento == numeroSecreto) {
            acertado = 1;
            break;
        } else if (intento < numeroSecreto) {
            printf("El número secreto es mayor.\n");
        } else {
            printf("El número secreto es menor.\n");
        }

        intentos--;
    }

    if (acertado) {
        printf("¡Felicitaciones! Has adivinado el número secreto %d.\n", numeroSecreto);
    } else {
        printf("¡Agotaste tus intentos! El número secreto era %d.\n", numeroSecreto);
    }

    return 0;
}
