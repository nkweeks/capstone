#!/usr/bin/env perl
# calc.pl

use Time::HiRes;

my $NUM_OF_LOOPS = 1000;

# Gather the start time of the loops
my $start = Time::HiRes::gettimeofday();

for (my $j=0; $j < 100; $j++) {
    for (my $i=1; $i <= $NUM_OF_LOOPS; $i++) {
        # Raise the counter to the power of itself
        my $x = pow($i, 3);
        # Multiply
        $x = $x * 3;
        # Divide
        $x = $x / $i;
        # Add
        $x = $x + $i;
        # Subtract
        $x = $x - $i;
    }
}
# Gather the end time of the loops
my $end = Time::HiRes::gettimeofday();

# Print the amount of time taken
printf("%.10f\n", $end - $start);

sub pow {
    # Get argument
    my $x = @_[0];
    my $y = @_[1];
    if ($y <= 1) {
        return $x;
    } else {
        return $x * pow($x, $y-1);
    }
}
