/* Project Euler Problem #5 */

#include <stdlib.h>
#include <stdio.h>
#include <math.h>

int numPrimes = -1;

int *
prime_nums_below(int n)
{
    int i, j, ct = 0, flag;
    for (i=2; i<=n; i++) {
        flag = 0;
        for (j=2; j<=i/2; j++) {
            if (i%j == 0) {
                flag = 1;
                break;
            }
        }
        if (!flag) {
            ct++;
        }
    }

    numPrimes = ct;

    int *res = malloc(ct * sizeof(int));

    int index = 0;

    for (i=2; i<=n; i++) {
        flag = 0;
        for (j=2; j<=i/2; j++) {
            if (i%j == 0) {
                flag = 1;
                break;
            }
        }
        if (!flag) {
            res[index] = i;
            index++;
        }
    }

    return res;
}

int
main()
{
    int n = 20;
    int res = 1;

    int *numbers = prime_nums_below(n);

    int i;
    for (i=0; i<numPrimes; i++) {
        int tmp = numbers[i];
        int power = 0;
        while (tmp < n) {
            tmp *= numbers[i];
            power++;
        }
        res *= pow(numbers[i], power);
    }

    printf("%d\n", res);

    return 0;
}
