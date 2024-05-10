//CODIGO DE ALGORITMO PARALELO 
#include <iostream>
#include <omp.h>

int main() {
    
    #pragma omp parallel for
    for (int i = 50000; i <= 100000; i++) {
        // Verifica si el n�mero es par
        if (i % 2 == 0) {
            // Imprime el n�mero si es par
            std::cout << i << " ";
        }
    }

    return 0;
}
