#!/usr/bin/perl

$IN=@ARGV[0];  # sequence name to look for in the folder
$DB=@ARGV[1];  # folder name

# extract a sequence from list of sequences

$SEQ=">"."$IN";
$db=$DB;

$db =~ s/.*\.p/p/g;
$db =~ s/.*\.d/d/g;
$db =~ s/.*\.s/s/g;

$ext=$db;

if ($ext eq "pep" ) { $ext = "prt"; }

$OUT=" $SEQ".".$ext";

open (OUT,"$OUT");

$found=$iflag=0;
open(DB,"$DB") || die "can't open $DB";
while(<DB> )
{

    @tab=split(/\s+/,$_);

    if ( m />/ && $found == 1 ) { exit; }

    if ( $tab[0] eq $SEQ ) { $iflag=1; }
    if ( $iflag == 1 )
  {
      print OUT $_;
      $found=1;
  }

}

if ($found == 0 ) { print "$IN not found in $DB\n"; }
