//CODIGO DE ALGORITMO CONCURRENTE
#include <iostream>

int main() {
    
    // Itera sobre los n�meros entre 50000 y 100000
    for (int i = 50000; i <= 100000; i++) {
        // Verifica si el n�mero es par
        if (i % 2 == 0) {
            // Imprime el n�mero si es par
            std::cout << i << " ";
        }
    
	}	
    return 0;
}
