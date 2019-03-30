#!/usr/bin/perl

# split a whole genome to a list of genes
$IN=@ARGV[0]; 

if ($IN eq "") {print "usage: splitfasta.pl dbprotfile.fasta\n"; exit}

open (IN, "$IN");

while (<IN>)
{
    # print $_;
	
    if (m/^>/)
        {
	close (OUT);
	@tab=split(/\s+/, $_);
        $idseq=$tab[0];
        open (OUT, "$idseq.prt");
        
         } #if
  
    print OUT $_;

} #while
