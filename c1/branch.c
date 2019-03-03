// branch.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_OF_LOOPS 1000000

static long get_nanos(void);

int main(void)
{
    // Gather the start time of the program
    long start = get_nanos();

    // Loop 1 billion times
    for (int i = 0; i < NUM_OF_LOOPS; i++) {
        if (i == 1) {}
        if (i == 2) {}
        if (i == 3) {}
        if (i == 4) {}
        if (i == 5) {}
        if (i == 6) {}
        if (i == 7) {}
        if (i == 8) {}
        if (i == 9) {}
        if (i == 10) {}
    }

    // Gather the end time
    long end = get_nanos();

    // Print out the elapsed time
    printf("%Lf\n", (((long double)end) - start) / 1000000000);
}


static long get_nanos(void) {
    struct timespec ts;
    timespec_get(&ts, TIME_UTC);
    return (long)ts.tv_sec * 1000000000L + ts.tv_nsec;
}

