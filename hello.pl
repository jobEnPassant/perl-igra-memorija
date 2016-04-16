#!C:\xampp\perl\bin\perl.exe

print "Content-type: text/html \n\n";
print "<HTML><HEAD><TITLE>Hello World</TITLE></HEAD>";
print "<BODY><h2>Hello Loyola</h2></BODY></HTML>";

print "<BODY><h2>Hello World</h2>";
print "<br> server name <br>";
print $ENV{SERVER_NAME};
print "<br> server + perl<br>" ;
print $ENV{SERVER_NAME}."/perl/amir/";
print "<br> isto<br>";
print "$ENV{SERVER_NAME}/perl/amir/";
print "<br> isto + http<br>";
print "http://$ENV{SERVER_NAME}/perl/amir/";

print "<br> http refer<br>";
print $ENV{HTTP_REFERER};

print "</BODY></HTML>";
