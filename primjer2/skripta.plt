unset multiplot
reset
set encoding utf8

#POSTAVKE GRAFA: DIMENZIJE SLIKE, VELICINA FONTA, IME SLIKE
set term pngcairo background "#ffffff" \
   font "Arial,20pt" \
   size 40.0cm,30.0cm
   set output 'primjer2.png'

#STILOVI LINIJA: POZIVAMO S ls BROJ
#  POSTAVLJAMO S lw (linewidth), lc (linecolor), dt (dashtype)
set style line  7 lw 1 lc rgb "black"



set key top right
set samples 100000
set grid


   #set xrange [3:12.0]
   #set yrange [0.415:0.417]
   set xlabel "x"
   set ylabel "rho(x,t)"
   # ZNAK \ NA KRAJU LINIJE OZNACAVA PRELAZAK NAREDBE U NOVI RED
   plot 0 w l ls 7 ti '',\
      'primjer2.txt' i 0 u 2:3 w lp ti 't=0',\
      '' i 1 u 2:3 w lp ti 't=50',\
      '' i 2 u 2:3 w lp ti 't=100',\
      '' i 3 u 2:3 w lp ti 't=150',\
      '' i 4 u 2:3 w lp ti 't=200'

unset output
reset
set term GNUTERM
