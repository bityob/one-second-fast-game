#include <stdlib.h>

// Number to guess: How many iterations of
// this loop can we go through in a second?

int main(int argc, char **argv) {
    int i;
    long long NUMBER, s;
    char *end;
    NUMBER = strtoll(argv[1], &end, 10);

    for (s = i = 0; i < NUMBER; ++i) {
        s += 1;
    }

    return 0;
}
