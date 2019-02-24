#!/usr/bin/env perl

use Time::HiRes;

# This tests the time of a function
my $start = Time::HiRes::gettimeofday();
printf("%s\n", "hello");
my $end = Time::HiRes::gettimeofday();

printf("%.10f\n", $end - $start);
