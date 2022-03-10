unset multiplot
reset
set term png enhanced \
    font 'Arial,24'\
    size 1000,1000
set output 'r3w.png'

set offsets 0, 0, 0, 0
set lmargin 0
set bmargin 0
set rmargin 0
set tmargin 0

set style line 1  lw 1 lc rgb "blue"
set style line 2  lw 1 lc rgb "cyan"
set style line 3  lw 1 lc rgb "green"
set style line 4  lw 1 lc rgb "orange"
set style line 5  lw 1 lc rgb "red"
set style line 6  lw 1 lc rgb "gray"
set style line 7  lw 1 lc rgb "black"


set multiplot
  set origin 0.13,0.13
  set size 0.84,0.84
    set xlabel 'x / mm'
    set ylabel 'y / mm' offset 1.0, 0

    plot [0:100][0:100] 'primjer1.txt' i 0 u 2:3 w l ls 1 ti '1. čestica', \
                        'primjer1.txt' i 0 u 4:5 w l ls 3 ti '5. čestica', \
                        'primjer1.txt' i 0 u 6:7 w l ls 5 ti '9. čestica' 

unset multiplot
unset output

