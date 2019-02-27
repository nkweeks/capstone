// calc.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_OF_LOOPS 5

// Function prototypes
static long get_nanos(void);
long pow(long x, long y);

int main(void)
{
    long start = get_nanos();
    for (int i = 1; i <= NUM_OF_LOOPS; i++) {
        // Exponent
        i = pow(i, i);
        printf("%ld\n", i);
    }
    long end = get_nanos();
    printf("%Lf\n", (((long double)end) - start) / 1000000000);
}


long pow(long x, long y) 
{
    if (y <= 1) {
        return x;
    } else {
        return pow(x, y-1) * pow(x, y-2);
    }
}

static long get_nanos(void) {
    struct timespec ts;
    timespec_get(&ts, TIME_UTC);
    return (long)ts.tv_sec * 1000000000L + ts.tv_nsec;
}

