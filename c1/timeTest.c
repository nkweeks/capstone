// calc.c
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

static long get_nanos(void);

int main(void)
{
    long start = get_nanos();
    long end = get_nanos();
    printf("%Lf\n", (((long double)end) - start) / 1000000000);
}


static long get_nanos(void) {
    struct timespec ts;
    timespec_get(&ts, TIME_UTC);
    return (long)ts.tv_sec * 1000000000L + ts.tv_nsec;
}

