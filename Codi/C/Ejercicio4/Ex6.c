#include <stdio.h>

int main() {
    int numero;

    for (numero = 1; numero <= 10; numero++) {
        printf("%d ", numero);

        if (numero == 8) {
            break;
        }
    }

    return 0;
}
