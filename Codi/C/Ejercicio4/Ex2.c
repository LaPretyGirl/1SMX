#include <stdio.h>

int main() {
    int numero1, numero2;

    printf("Ingrese el primer número entero: ");
    scanf("%d", &numero1);

    if (numero1 == 0) {
        printf("El producto de 0 por cualquier número es 0.\n");
    } else {
        printf("Ingrese el segundo número entero: ");
        scanf("%d", &numero2);
        printf("El producto de %d por %d es %d.\n", numero1, numero2, numero1 * numero2);
    }

    return 0;
}
