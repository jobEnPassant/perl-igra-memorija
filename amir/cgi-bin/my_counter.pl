#!C:\xampp\perl\bin\perl.exe
print "Content-type: application/x-javascript\n\n"; 

print "r=new Array(";

$countfile = "counter.no";
$logfile = "log.txt";
$ipadress = $ENV{REMOTE_ADDR};
$username = $ENV{HTTP_USER_AGENT};

open(COUNT,"$countfile");
$count = <COUNT>;
close(COUNT);

$count++;
print "\"",$count,"\"";
print ",";
print "\"",$ipadress,"\"";
print ")\n";

open(COUNT,">$countfile");
print COUNT "$count";
close(COUNT);

use POSIX qw(strftime);
$now_string = strftime "%a %b %e %H:%M:%S %Y", localtime;

open(LOG,">>$logfile");
print LOG "|",$now_string,"|","$ENV{REMOTE_ADDR}","|","$ENV{HTTP_USER_AGENT}","|","\n";
close(LOG);

