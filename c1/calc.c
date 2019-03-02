// calc.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define NUM_OF_LOOPS 100

// Function prototypes
static long get_nanos(void);
int mypow(int x, int y);

int main(void)
{
    long start = get_nanos();
    for (int i = 1; i <= NUM_OF_LOOPS; i++) {
        // Save the counter to a variable that can be used
        int x = i;

        // Raise the counter to the power of itself
        x = mypow(i, i);
        printf("%d ** %d = %d\n", i, i, x); 
        // Multiply
        x = x * x;
        // Divide
        x = x / x;
        // Add
        x = x + x;
        // Subtract
        x = x - x;
    }
    long end = get_nanos();
    printf("%Lf\n", (((long double)end) - start) / 1000000000);
}


int mypow(int x, int y) 
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

