#!/usr/bin/env perl

use Time::HiRes;

# This tests the time of a function
my $start = Time::HiRes::gettimeofday();
for (my $i=0; $i < 1000; $i++) {
    for (my $j=0; $j < 1000; $j++) {
        for (my $k=0; $k < 1000; $k++) {}
    }
}
my $end = Time::HiRes::gettimeofday();

printf("%.10f\n", $end - $start);
