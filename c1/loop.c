// loop.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_OF_LOOPS 1000

static long get_nanos(void);

int main(void)
{
    // Gather the start time of the program
    long start = get_nanos();

    // Loop 1 billion times
    for (int i = 0; i < NUM_OF_LOOPS; i++) {
        for (int j = 0; j < NUM_OF_LOOPS; j++) {
            for (int k = 0; k < NUM_OF_LOOPS; k++){}
        }
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

