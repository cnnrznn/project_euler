/* Project Euler Problem #3 */

#include <stdio.h>

int
main()
{
    // number to be factored
    long n = 600851475143;
    long d = 2;

    // prime factorization
    while (n > 1) {
        if (n%d == 0) {
            while (n%d == 0) {
                n /= d;
            }
            printf("%ld\n", d);
        }
        d = d+1;
    }

    return 0;
}
