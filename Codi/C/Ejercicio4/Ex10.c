#include <stdio.h>
#include <stdlib.h>

int main() {
    printf("Contenido del directorio actual:\n");
    system("ls -l");

    printf("\nFecha y hora actual:\n");
    system("date");

    printf("\nDirectorio de trabajo actual:\n");
    system("pwd");

    printf("\nEjecutando Firefox...\n");
    system("firefox");

    return 0;
}
