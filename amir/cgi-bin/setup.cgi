#!C:\xampp\perl\bin\perl.exe

# setup.cgi - manage game options
#
# Amir Balic
# Comp 225 - final program
# content : memory.cgi, top_trn.cgi, game.cgi, setup.cgi

use strict;
use CGI;

my $q = new CGI;

print $q->header( -type => "text/html", -target => "setup"),
      $q->start_html( -title => "Setup", -bgcolor => "#0033cc", -text => "#FFFF00"),
      $q->br,
      $q->p( "<center><b><font face='Comic Sans MS' color='#FFFF00'>",
             "Postavke",
             "<hr width='94%' color='#FFFF00'>" ),
      $q->start_form( -method => "post", -target => "game", -action => "game.cgi" ),
      $q->radio_group(                 # pick picture set
         -name    => "Pic_set",
         -values  => [ "0", "10", "100", "1000" ],
         -default => "0",
         -labels  => {   0 => "..............Brojevi",
                        10 => "..............Simboli",
                       100 => ".................Boje",
                      1000 => ".................Pipe" }
      ),
      $q->p( "<hr width='94%' color='#FFFF00'>" ),
      $q->submit( -value => "Pogledaj", -name => "See" ),   # preview game choice
      $q->submit( -value => "Nova Igra", -name => "Start" ), # start new game
      $q->end_form,
      $q->p( "</font></b>"),
      "<img border='0' src='http://$ENV{SERVER_NAME}/perl/amir/r.gif' align='right'>",
      $q->end_html;
