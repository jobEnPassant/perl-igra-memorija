#!C:\xampp\perl\bin\perl.exe

use strict;
use CGI;

my $q = new CGI;

print $q->header( "text/html" );

print $q->start_html( "Welcome" );
print $q->p( "These are the HTTP environment variables I received:" );

foreach ( $q->http ) {
   print "$_:";
   print "    ", $q->http( $_  ), "\n";
   print "<br>";
}

print $q->end_html;