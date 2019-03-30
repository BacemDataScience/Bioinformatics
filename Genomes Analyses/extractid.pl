#!/usr/bin/perl
# extract id of genes represented in Fasta file

open (IN, "GSACE.pep");

while (<IN>)
{
    if (m/^>/) {

	s/>//g;
	
	@tab=split(/\s+/ ,$_);

	

print "$tab[0]\n";
	


} #if
    
} # while
