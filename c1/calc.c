// calc.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_OF_LOOPS 1000

// Function prototypes
static long get_nanos(void);
long mypow(long x, int y);

int main(void)
{
    long start = get_nanos();
    // Restart calculations 100 times
    for (int j = 0; j < 100; j++) {
        // Loop through 1000 sets of calculations
        for (int i = 1; i <= NUM_OF_LOOPS; i++) {
            // Raise the counter to the power of itself
            long x = mypow(i, 3);
            // Multiply
            x = x * 3;
            // Divide
            x = x / i;
            // Add
            x = x + i;
            // Subtract
            x = x - i;
        }
    }
    long end = get_nanos();
    printf("%Lf\n", (((long double)end) - start) / 1000000000);
}


long mypow(long x, int y) 
{
    if (y <= 1) {
        return x;
    } else {
        return x * mypow(x, y-1);
    }
}

static long get_nanos(void) {
    struct timespec ts;
    timespec_get(&ts, TIME_UTC);
    return (long)ts.tv_sec * 1000000000L + ts.tv_nsec;
}

