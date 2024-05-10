//CODIGO DE ALGORITMO CONCURRENTE
#include <iostream>

int main() {
    
    // Itera sobre los números entre 50000 y 100000
    for (int i = 50000; i <= 100000; i++) {
        // Verifica si el número es par
        if (i % 2 == 0) {
            // Imprime el número si es par
            std::cout << i << " ";
        }
    
	}	
    return 0;
}
