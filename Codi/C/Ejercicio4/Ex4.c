#include <stdio.h>
#include <math.h>

int main() {
    double numero;
    printf("Ingrese un número: ");
    scanf("%lf", &numero);

    double raizCuadrada = sqrt(numero);
    double seno = sin(numero);
    double coseno = cos(numero);
    double potencia = pow(numero, 3);

    printf("Número ingresado: %.2lf\n", numero);
    printf("Raíz cuadrada: %.2lf\n", raizCuadrada);
    printf("Seno: %.2lf\n", seno);
    printf("Coseno: %.2lf\n", coseno);
    printf("Potencia (elevado al cubo): %.2lf\n", potencia);

    return 0;
}
