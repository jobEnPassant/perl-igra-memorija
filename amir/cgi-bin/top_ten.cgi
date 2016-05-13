#!C:\xampp\perl\bin\perl.exe

# top_ten.cgi - write and disply game scores
#
# Amir Balic
# Comp 225 - final program
# content : memory.cgi, top_trn.cgi, game.cgi, setup.cgi

use strict;
use CGI;
my @lines;
my $message;
my $q = new CGI;
my $init_file = "rangelist.txt"; # file - hold game scores

open(SETUP,"<$init_file") || die;
@lines = <SETUP>;
close (SETUP);

my $filter = ($q->param ( "GameID" ))." end\n";  # disable to enter same result twice

if($lines[10] eq "$filter") {
  $message = "TopTen <br>Pritisni Nova Igra";
} else {
  $message = "Top Ten<br><br>";
$lines[10] = $q->param( "GameScore" )." ".$q->param( "player_name" )."\n";  # append current game score
}

my @sorted_lines = sort { int($b) <=> int($a) } @lines;

print $q->header( -type => "text/html", -target => "top_ten"),
      $q->start_html( -title => "Setup", -bgcolor => "#0033cc", -text => "#FFFF00");
print "<center><b><font face='Comic Sans MS' color='#FFFF00'> $message";
print "<table style='font-family: Comic Sans MS; font-size: 10pt; font-weight: bold'>";

for (my $i=0; $i<10; ++$i) {
  (my $score, my $player) = split(" ", $sorted_lines[$i]);
  print "<tr><td align=\"right\">".($i+1)."-</td> <td>$player</td><td align=\"right\">$score</td></tr>";
}
open(SETUP,">$init_file") || die;
  for (my $i=0; $i<10; ++$i) {
    print SETUP $sorted_lines[$i];
  }
  print SETUP "$filter";        # mark current game in file
close(SETUP);

print "</table></font></b>";
print $q->end_html;
