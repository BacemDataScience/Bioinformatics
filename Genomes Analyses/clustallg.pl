#!/usr/bin/perl

# clustall.pl for a list of sequences
$OF=@ARGV[0]; #output format
@LIST=`ls *.pep`;
while ($P=shift(@LIST))
{
    chomp $P;
    system ("clustg.pl $P $OF");
}
