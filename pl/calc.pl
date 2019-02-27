#!/usr/bin/env perl

# loop.pl

use Time::HiRes;

my $NUM_OF_LOOPS = 1000;

# Gather the start time of the loops
my $start = Time::HiRes::gettimeofday();

# Loop through an empty loop 1 billion times
for (my $i=0; $i < $NUM_OF_LOOPS; $i++) {
    for (my $j=0; $j < $NUM_OF_LOOPS; $j++) {
        for (my $k=0; $k < $NUM_OF_LOOPS; $k++) {}
    }
}
# Gather the end time of the loops
my $end = Time::HiRes::gettimeofday();

# Print the amount of time taken
printf("%.10f\n", $end - $start);
