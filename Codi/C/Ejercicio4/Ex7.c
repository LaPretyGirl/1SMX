#include <stdio.h>

int main() {
    int contador = 0;
    int numero;
    int sumaPares = 0;

    printf("Ingrese cinco números enteros:\n");

    while (contador < 5) {
        printf("Número %d: ", contador + 1);
        scanf("%d", &numero);

        if (numero % 2 == 0) {
            sumaPares += numero;
        } else {
            printf("No se suma: %d es un número impar.\n", numero);
        }

        contador++;
    }

    printf("La suma de los números pares ingresados es: %d\n", sumaPares);

    return 0;
}
