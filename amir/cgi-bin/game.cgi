#!C:\xampp\perl\bin\perl.exe

# game.cgi - main program
#
# Amir Balic
# Comp 225 - final program
# content : memory.cgi, top_trn.cgi, game.cgi, setup.cgi

use strict;
use CGI;

my $q = new CGI;                   # CGI object

my $img_str ="";
my $slv_str ="";
my $scr_str ="";

&new_game() if ($q->param( "Start" ) eq "Nova Igra");
my $mark_end = 1;
&preview_game () if ($q->param( "See" ) eq "Pogledaj" || !$q->param( "pc" ));

my @images = split (" ", $q->param ( "pc" ));  # array pictures
my @sloved = split (" ", $q->param ( "pr" ));  # pair flags - 1/0 sloved/no
my @scores = split (" ", $q->param ( "pt" ));  # score holder

my $part ="http://$ENV{SERVER_NAME}/perl/amir/";       # pictures location 
#my $part ="http://100.64.94.245/perl/amir/";
my $extension =".gif";                         # pictures exstension

my $value;                                     # table position of clicked picture
for (my $x=1; $x<17; $x++) {                   # determine vhich picture submit values (is clicked)
  $value = $x if($q->param ( "p".$x.".x" ) || $q->param ( "p".$x ));  # graphich or text
}

print $q->header( -type => "text/html", -target => "game" ).
      $q->start_html( -title => "Memory", -bgcolor => "#0033CC"),
      "<center>";
&slove_table();
FINISH:                                        # to display table once more after is sloved
&display_table();

###  subroutines ###
sub display_table {                            # setup and display game field
print $q->start_form( -method => "post", -target => "game", -action => $q->script_name ),
      $q->hidden( -value => $img_str , -name => "pc"),
      $q->hidden( -value => $slv_str , -name => "pr"),
      $q->hidden( -value => $scr_str , -name => "pt"),
      "<table border=0 bgcolor=\"#33CCFF\">",
      "<th colspan=\"4\" bgcolor=\"#0033CC\"><font face=\"Comic Sans MS\" color=\"#FFFF00\">",
      "Rezultat :$scores[2]</font></th>";
  for (my $i=0; $i<=12; $i+=4) {
    print "<tr>";
    for (my $j=1; $j<=4; ++$j) {
      my $index = $j+$i;                       # pisture index-table position=picture array index=sloved flag index
      my $adress = $part.$images[$index*$sloved[$index]].$extension;
      my $picture = "<img src=\"$adress\" width=\"50\" height=\"50\"border=\"0\">";
      if($sloved[$index] eq "0") {             # display image button
        print "<td><input type=\"image\" name=\"p".$index."\" value=\"".$index."\" "."src=\"$adress\">";
      }else {
        print "<td>$picture</a></td>";         # or display sloved picture
      }
    }
    print "</tr>";
  }
  print "</table></form></body></html>";
}

sub slove_table {
  if($sloved[0] eq "0"){                               # first click
    if($images[$images[17]] ne $images[$sloved[17]]){  # if no picture pair
      $sloved[$images[17]] = "0";                      # reset picture flags
      $sloved[$sloved[17]] = "0";
    }
    else {                                             # if pair - calculate score - 100 minus secund to pair
      $scores[0]++;
      my $earnings = 100 - (time()%100000 - $scores[1]);
      $scores[2] += $earnings if($earnings>0);
      $scores[1] = time()%100000;
    }
    $sloved[$value] = "1";                     # setup picture flag
    $images[17] = $value;                      # store clicked picture position (first click)
    $sloved[0] = "1";                          # set flag for second click
  }
  elsif($sloved[0] eq "1"){                    # second click
    $sloved[$value] = "1";                     # setup picture flag
    $sloved[17] = $value;                      # store clicked picture position (second click)
    $sloved[0] = "0";                          # set flag for first click
  }
  $q->param( pc => "@images" );                # update submit parameters
  $q->param( pr => "@sloved" );
  $q->param( pt => "@scores" );
  foreach ( @images ) { $img_str .= $_." "; }
  foreach ( @sloved ) { $slv_str .= $_." "; }
  foreach ( @scores ) { $scr_str .= $_." "; }
  for (my $e=1; $e<17; $e++) { $mark_end *= $sloved[$e]; } # proces pair flags
  $mark_end > 0 ? &end_game() : print "<br><br>";          # all 1 - game over / any 0 continue
}

sub new_game {                                # setup base state for game
  my @start_scores = qw( 0 0 0 );
  $start_scores[1] = time()%100000;           # setup start time
  my $inc = $q->param( "Pic_set" );                         # picture set coiser submited by setup
  my @img_start = qw (0 1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8 9); # base picture set
  for(my $i=1; $i<17; $i++) {$img_start[$i] += $inc;}       # calculate picture names
  for(my $i=1; $i<17; $i++) {                               # mix pictures
    my $temp_i = $img_start[$i];
    my $ix = int(rand(8)) + 1;
    $img_start[$i] = $img_start[$ix];
    $img_start[$ix] = $temp_i;
  }
  $q->param( pc => "@img_start" );            # simulate script call with parameters
  $q->param( pr => "1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0");
  $q->param( pt => "@start_scores" );
}

sub preview_game {                            # setup base state for preview
  $mark_end = 0;
  my $img_start = "0 ";
  my $inc = $q->param( "Pic_set" ) ;          # picture set coiser submited by setup
  for(my $i=1+$inc; $i<9+$inc; $i++) {$img_start .= ($i)." ".($i)." ";}
  $q->param( pc => $img_start );              # simulate script call with parameters
  $q->param( pr => "1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1");
  $q->param( pt => "0 0 Pogled");
}

sub end_game {                                # final proces
  $scores[0]++;
  my $earnings = 100 - (time()%100000 - $scores[1]);  # score for last pair
  $scores[2] += $earnings;
  $scores[1] = time()%100000;
  # pick user name and pass it by parameter to top_ten.cgi script (score and game ident too)
  print $q->start_form( -method => "post", -target => "top_ten", -action => "top_ten.cgi"),
        $q->submit( -value => "Unesi Ime", -name => "GameOver" ),
        $q->textfield( -name => "player_name", -default => "inkognito", -size => "12" ),
        $q->hidden( -value => ($scores[2]) , -name => "GameScore"),
        $q->hidden( -value => ($scores[1])*(-1) , -name => "GameID"),
        $q->end_form;
  $mark_end = 0;
  goto FINISH;                               # disply final form and game field
}
