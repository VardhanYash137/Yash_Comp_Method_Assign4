#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

// Function to generate a random number from an exponential distribution
double generate_exponential(double lambda) {
    double u = (double) rand() / RAND_MAX;  // Generate a uniform random number between 0 and 1
    return -log(1 - u) / lambda;            // Apply the inverse CDF
}

int main() {
    int num_samples = 10000;    // Number of random samples to generate
    double lambda = 2;        // Parameter of the exponential distribution
    double *samples = (double *) malloc(num_samples * sizeof(double));
    
    if (samples == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    // Seed the random number generator
    srand(time(NULL));

    // Generate random samples
    for (int i = 0; i < num_samples; i++) {
        samples[i] = generate_exponential(lambda);
    }

    // Print a few samples as a demonstration
    for (int i = 0; i < num_samples; i++) {
        printf("%f\n", samples[i]);
    }

    // Clean up
    free(samples);

    return 0;
}

