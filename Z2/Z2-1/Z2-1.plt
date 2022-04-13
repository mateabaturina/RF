unset multiplot
reset

# KORACI
  Nk = 200 # ukupno
  pk = 10   # pohranjen svaki pk-ti
  sk = 10   # slikaj    svaki sk-ti

# BLOKOVI u primjer2.txt
  Nb = Nk/pk # ukupno
  db = sk/pk # slikj svaki db-ti
   b = 0     # početni blok

# SKUPLJANJE SLIKA ZA ANIMACIJU 
set term gif animate \
    font 'Arial,24' \
    size 1000,1000
    animacija = sprintf("Z2-1.gif", b, sk, Nk)
    set output animacija

    set xlabel 'x / mm'
    set ylabel 'y / mm' offset 1.0, 0

    # SLIKAJ
      load "rNw_slikaj.gnu"

set output
unset output
reset
set term GNUTERM