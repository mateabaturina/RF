unset multiplot
reset
set encoding utf8

#POSTAVKE GRAFA: DIMENZIJE SLIKE, VELICINA FONTA, IME SLIKE
set term pngcairo background "#ffffff" \
   font "Arial,20pt" \
   size 40.0cm,30.0cm
   set output 'Z2-6_usporedba.png'

#STILOVI LINIJA: POZIVAMO S ls BROJ
#  POSTAVLJAMO S lw (linewidth), lc (linecolor), dt (dashtype)
set style line  7 lw 1 lc rgb "black"
set style line 11 lw 1 dt '-' lc rgb "blue"


set key top right
set samples 100000
set grid


   #set xrange [-100:100.0]
   #set yrange [0.0:60000]
   set xlabel "x/cm"
   set ylabel "rho(x,t)"
   # ZNAK \ NA KRAJU LINIJE OZNACAVA PRELAZAK NAREDBE U NOVI RED
   plot 0 w l ls 7 ti '',\
      'Z2-6_dif.txt' i 1 u 2:3 w lp ti 't=50',\
      'Z2-6_dif.txt' i 2 u 2:3 w lp ti 't=100',\
      'Z2-6_dif.txt' i 3 u 2:3 w lp ti 't=150',\
      'Z2-6_dif.txt' i 4 u 2:3 w lp ti 't=200',\
      'Z2-6_hod.txt' i 0 u 1:2 w lp ti 'P(x) t=50',\
      'Z2-6_hod.txt' i 1 u 1:2 w lp ti 'P(x) t=100',\
      'Z2-6_hod.txt' i 2 u 1:2 w lp ti 'P(x) t=150',\
      'Z2-6_hod.txt' i 3 u 1:2 w lp ti 'P(x) t=200'

unset output
reset
set terminal wxt
