#include <stdio.h>

int main() {
    int numero;

    printf("Ingrese un número entero: ");
    scanf("%d", &numero);

    if (numero % 2 == 0) {
        printf("%d es un número par.\n", numero);
    } else {
        printf("%d no es un número par.\n", numero);
    }

    return 0;
}
