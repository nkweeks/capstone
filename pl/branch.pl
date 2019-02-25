#!/usr/bin/env perl

# branch.pl

use Time::HiRes;

my $NUM_OF_LOOPS = 1000000000;

# Gather the start time of the loops
my $start = Time::HiRes::gettimeofday();

# Loop through an empty loop 1 billion times
for (my $i=0; $i < $NUM_OF_LOOPS; $i++) {
    if ($i % 1 == 0) {}
    if ($i % 2 == 0) {}
    if ($i % 3 == 0) {}
    if ($i % 4 == 0) {}
    if ($i % 5 == 0) {}
    if ($i % 6 == 0) {}
    if ($i % 7 == 0) {}
    if ($i % 8 == 0) {}
    if ($i % 9 == 0) {}
    if ($i % 10 == 0) {}
}
# Gather the end time of the loops
my $end = Time::HiRes::gettimeofday();

# Print the amount of time taken
printf("%.10f\n", $end - $start);
