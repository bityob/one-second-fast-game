#include <stdlib.h>
#include <stdio.h>

// Number to guess: How many iterations of
// this loop can we go through in a second?

int main(int argc, char **argv) {
    unsigned int NUMBER, i, s;
    NUMBER = atoi(argv[1]);

    for (s = i = 0; i < NUMBER; ++i) {
        s += i;
    }
    printf("%u\n", s);

    return 0;
}