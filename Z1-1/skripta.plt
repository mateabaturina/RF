unset multiplot
reset
set encoding utf8

#POSTAVKE GRAFA: DIMENZIJE SLIKE, VELICINA FONTA, IME SLIKE
set term pngcairo font "Arial,20" size 1200,800
set output 'Z1-1.png'
set samples 1000


    set xlabel "N"
    set ylabel "greska*sqrt(N)"
    plot [:][:] \
        'Z1-1.txt' u 1:2 w p ti 'podaci'

unset output
set output
set term GNUTERM