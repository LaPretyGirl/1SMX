#include <stdio.h>
#include <string.h>

int main() {
    char palabra[100];
    int longitud, i;
    int contadorVocales = 0;

    printf("Ingrese una palabra: ");
    scanf("%s", palabra);

    longitud = strlen(palabra);

    for (i = 0; i < longitud; i++) {
        if (palabra[i] == 'a' || palabra[i] == 'e' || palabra[i] == 'i' || palabra[i] == 'o' || palabra[i] == 'u' ||
            palabra[i] == 'A' || palabra[i] == 'E' || palabra[i] == 'I' || palabra[i] == 'O' || palabra[i] == 'U') {
            contadorVocales++;
        }
    }

    printf("El número de vocales en la palabra es: %d\n", contadorVocales);

    return 0;
}
