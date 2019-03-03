#!/usr/bin/env perl
# branch.pl

use Time::HiRes;

my $NUM_OF_LOOPS = 1000000;

# Gather the start time of the loops
my $start = Time::HiRes::gettimeofday();

# Loop through an empty loop 1 billion times
for (my $i=0; $i < $NUM_OF_LOOPS; $i++) {
    if ($i == 1) {}
    if ($i == 2) {}
    if ($i == 3) {}
    if ($i == 4) {}
    if ($i == 5) {}
    if ($i == 6) {}
    if ($i == 7) {}
    if ($i == 8) {}
    if ($i == 9) {}
    if ($i == 10) {}
}
# Gather the end time of the loops
my $end = Time::HiRes::gettimeofday();

# Print the amount of time taken
printf("%.10f\n", $end - $start);
