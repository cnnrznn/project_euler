/* Project Euler Problem #2 */

#include <stdio.h>

int 
nextFib(int a, int b)
{
    return a + b;
}

int main()
{
    // upper-bound inclusive
    int n = 4000000;

    // previous fib number buffers
    int fibn1=1, fibn2=1;

    // sum
    long sum = 0;

    // main loop
    int currFib = 2;
    while (currFib <= n) {
        if (currFib%2 == 0) {
            sum += currFib;
        }
        fibn2 = fibn1;
        fibn1 = currFib;
        currFib = nextFib(fibn2, fibn1);
    }

    // display result
    printf("The sum of even fibonacci numbers below %d is %ld.\n", n, sum);

    return 0;
}
