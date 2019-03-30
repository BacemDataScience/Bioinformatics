#!/usr/bin/perl

# Clustalw ofor two genes
$IN2=$ARGV[1];

system ("clustalw -infile=$IN1 -align -output=$IN2 -outfile=$IN1.$IN2 2>&1 > /dev/null");

