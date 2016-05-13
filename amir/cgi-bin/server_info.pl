#!C:\xampp\perl\bin\perl.exe

use strict;

print "Content-type: text/html\n\n";

print "<html>";

my $var_name;
foreach  $var_name (sort keys %ENV ) {
   print "<P><B>$var_name</B><BR>";
   print $ENV{$var_name};
}   
print"</html>";
