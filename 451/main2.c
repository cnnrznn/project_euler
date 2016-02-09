/* Project Euler Problem 451 */

#include <mpi.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int *factors;
int *possible;

int solve(int n) {
    // prime factorization of n
    int index = 0;
    int i = 2, j;
    int t = n;
    while (i<=t) {
        while (t % i == 0) {
            t /= i;
            if (factors[index] == 0) {
                factors[index] = i;
                index++;
            }
        }
        i++;
    }
    /*
    for (i=0; i<index; i++) {
        printf("%d, ", factors[i]);
    } printf("\n");
    */
    // create a list of elements numbered 0->n/2
    possible = calloc(n/2+1, sizeof(int));
    for (i=0; i<n/2+1; i++) {
        possible[i] = i;
    }
    // sieve out multiples of factors of n
    for (i=0; i<index; i++) {
        for (j=factors[i]; j<n/2+1; j+=factors[i]) {
            possible[i] = -1;
        }
    }
    // test remaining numbers
    for (i=2; i<n/2+1; i++) {
        if (possible[i] > -1) {
            if ((possible[i]*possible[i]) % n == 1) {
                free(possible);
                return n-possible[i];
            }
        }
    }

    free(possible);
    return 1;
}

int main(int argc, char **argv)
{
    MPI_Init(NULL, NULL);

    int size, rank;

    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

    // allocate space for factors
    factors = calloc(atoi(argv[1]), sizeof(int));

    long lsum=0, sum=0;

    int i;
    for (i=3+rank; i<=atoi(argv[1]); i+=size)
        lsum += solve(i);

    MPI_Reduce(&lsum, &sum, 1, MPI_LONG, MPI_SUM, 0, MPI_COMM_WORLD);

    if (rank==0)
        printf("%ld\n", sum);

    MPI_Finalize();
    return 0;
}
