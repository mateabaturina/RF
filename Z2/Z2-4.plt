unset multiplot
reset
set encoding utf8

#POSTAVKE GRAFA: DIMENZIJE SLIKE, VELICINA FONTA, IME SLIKE
set term pngcairo font "Arial,20" size 1200,800
set output 'Z2-4.png'
set samples 1000

    set xlabel "x"
    set ylabel "f(x)"

    D = 1.51018
    f(x) = 2.0*D*x

    plot [:][:] \
        'Z2-3.txt' u 2 w p ti 'datoteka', f(x) 

unset output
set output
set term GNUTERM
