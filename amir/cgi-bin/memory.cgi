#!C:\xampp\perl\bin\perl.exe

# memory.cgi - frame window for game scripts
#
# Amir Balic
# Comp 225 - final program
# content : memory.cgi, top_trn.cgi, game.cgi, setup.cgi

print "Content-type: text/html\n\n";

print <<TO_END;
<head>
<title>Memory</title>
</head>
<body>
<table width="640" cellspacing="0" cellpadding="0" >
   <tr>
     <th bgcolor="#345678">&nbsp;</th>
     <th bgcolor="#45678A">&nbsp;</th>
     <th bgcolor="#5678AB">&nbsp;</th>
     <th bgcolor="#678ABC">
      <p align="left">&nbsp;</p>
     </th>
     <th bgcolor="#78ABCD">&nbsp;</th>
     <th bgcolor="#8ABCDE">&nbsp;</th>
     <th bgcolor="#ABCDEF">&nbsp;</th>
     <th bgcolor="#BCDEF0" width="30%">
       <font color="#0000FF" size="+2">Memorija</font>
     </th>
     <th bgcolor="#ABCDEF">&nbsp;</th>
     <th bgcolor="#8ABCDE">&nbsp;</th>
     <th bgcolor="#78ABCD">&nbsp;</th>
     <th bgcolor="#678ABC">&nbsp;</th>
     <th bgcolor="#5678AB">&nbsp;</th>
     <th bgcolor="#45678A">&nbsp;</th>
     <th bgcolor="#345678">&nbsp;</th>
   </tr>
  </table>
<IFRAME SRC="top_ten.cgi" NAME="top_ten" FRAMEBORDER=0 style="float: left" width=200 height=370>
</IFRAME>
<IFRAME SRC="game.cgi" NAME="game" FRAMEBORDER=0 style="float: left" width=240 height=370>
</IFRAME>
<IFRAME SRC="setup.cgi" NAME="setup" FRAMEBORDER=0 style="float: left" width=200 height=370>
</IFRAME>
</body>
</html>
TO_END
