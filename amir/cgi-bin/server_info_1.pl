#!C:\xampp\perl\bin\perl.exe

print <<END_OF_HTML;
Content-type: text/html

<HTML>
<HEAD>
    <TITLE>About this server</TITLE>
</HEAD>
<BODY>
<H1>About this server</H1>
<HR>
<PRE>
   Server Name:         $ENV{SERVER_NAME}
   Listening on Port:   $ENV{SERVER_PORT}
   Server Software:     $ENV{SERVER_SOFTWARE}
   Server Protocol:     $ENV{SERVER_PROTOCOL}
   CGI Version:         $ENV{GATEWAY_INTERFACE}
</PRE>
<HR>
</BODY>
</HTML>
END_OF_HTML

