#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *archivo;
    char frase[100];

    archivo = fopen("frases.txt", "a");

    if (archivo == NULL) {
        printf("No se pudo crear el archivo.\n");
        return 1;
    }

    printf("Ingrese frases (presione Enter sin ingresar nada para terminar):\n");

    while (1) {
        fgets(frase, sizeof(frase), stdin);

        if (frase[0] == '\n') {
            break;
        }

        fputs(frase, archivo);
    }

    fclose(archivo);

    printf("Contenido del archivo \"frases.txt\":\n");

    archivo = fopen("frases.txt", "r");

    if (archivo == NULL) {
        printf("No se pudo abrir el archivo.\n");
        return 1;
    }

    char caracter;
    while ((caracter = fgetc(archivo)) != EOF) {
        printf("%c", caracter);
    }

    fclose(archivo);

    return 0;
}
