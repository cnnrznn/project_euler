/* Project Euler Problem #1 */

#include <stdio.h>

int main()
{
    long n = 1000;
    long tmp;
    long sum = 0;

    // sum 3's
    tmp = n-1;
    while (tmp%3 != 0) { tmp--; }
    sum += ((tmp+3) * (tmp/3)) / 2;

    // sum 5's
    tmp = n-1;
    while (tmp%5 != 0) { tmp--; }
    sum += ((tmp+5) * (tmp/5)) / 2;

    // subtract double-counted 3*5's
    tmp = n-1;
    while (tmp%15 != 0) { tmp--; }
    sum -= ((tmp+15) * (tmp/15)) / 2;

    // display result
    printf("The sum of numbers divisible by 3 or 5 below %ld is %ld.\n", n, sum);

    return 0;
}
