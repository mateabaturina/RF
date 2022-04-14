unset multiplot
reset
set encoding utf8

#POSTAVKE GRAFA: DIMENZIJE SLIKE, VELICINA FONTA, IME SLIKE
set term pngcairo background "#ffffff" \
   font "Arial,20pt" \
   size 40.0cm,30.0cm
   set output 'Z3-2.png'

#STILOVI LINIJA: POZIVAMO S ls BROJ
#  POSTAVLJAMO S lw (linewidth), lc (linecolor), dt (dashtype)
set style line  7 lw 1 lc rgb "black"
set style line 11 lw 1 dt '-' lc rgb "blue"
set datafile separator " "

set key top right
set samples 100000


   
   set xlabel "t / od dana 10.03.2021."
   # ZNAK \ NA KRAJU LINIJE OZNACAVA PRELAZAK NAREDBE U NOVI RED
   plot 'S.txt' i 0 u 1:2 w p ti 'S',\
      'I.txt' i 1 u 1:2 w p ti 'I',\
      'R.txt' i 2 u 1:2 w p ti 'R',\
      'JHU-CSSE-CRO.txt' i 3 u 1:2 w p ti 'S(t)',\
      'JHU-CSSE-CRO.txt' i 4 u 1:3 w p ti 'I(t)',\
      'JHU-CSSE-CRO.txt' i 5 u 1:4 w p ti 'R(t)',

unset output
reset
set terminal wxt
