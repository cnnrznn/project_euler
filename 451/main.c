/* Project Euler Problem 451 */

#include <mpi.h>
#include <stdio.h>

int solve(int n) {
    int i;
    for (i=n-2; i>=n/2; i--)
        if ((i*i)%n == 1)
            return i;
    return 1;
}

int main(int argc, char **argv)
{
    MPI_Init(NULL, NULL);

    int size, rank;

    MPI_Comm_size(MPI_COMM_WORLD, &size);
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);

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
