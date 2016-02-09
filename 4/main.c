/* Project Euler Problem #4 */

#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char
palindrome(char *str) {
    int len = strlen(str);
    if (len%2 != 0)
        return 0;
    int i;
    for (i=0; i<len/2; i++) {
        if (str[i] != str[len-i-1]) {
            return 0;
        }
    }
    return 1;
}

int
main()
{
    int n = 1000;
    int prod;
    char str[100];
    int pal = 1;

    int i, j;
    for (i=1; i<n; i++) {
    for (j=i; j<n; j++) {
        prod = i*j;
        sprintf(str, "%d", prod);
        if (palindrome(str)) {
            if (prod > pal)
                pal = prod;
        }
    }
    }

    // display result
    printf("%d\n", pal);

    return 0;
}
