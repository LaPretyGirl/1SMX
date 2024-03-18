#include <stdio.h>

#define PULGADAS_POR_METRO 39.37

int main() {
    float metros, pulgadas;

    printf("Ingrese la medida en metros: ");
    scanf("%f", &metros);

    pulgadas = metros * PULGADAS_POR_METRO;

    printf("La medida en pulgadas es: %.2f\n", pulgadas);

    return 0;
}
