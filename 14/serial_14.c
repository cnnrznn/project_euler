#include <stdio.h>

#define LIMIT 1000000

int collatz(long n) {
    int count = 0;
    while (n != 1) {
        count++;
        if (n%2 == 0)
            n = n/2;
        else
            n = 3*n + 1;
    }

    return count;
}

int main()
{
    int maxi = 0;
    int maxval = 0;
    int tval;
    long i;
    for (i=1; i<LIMIT; i++) {   
        tval = collatz(i);
        if (tval > maxval) {
            maxval = tval;
            maxi = i;
        }
    }

    printf("%d, %d\n", maxi, maxval);

    return 0;
}
