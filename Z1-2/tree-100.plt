# RESET POSTAVKI
unset multiplot
reset
set encoding utf8

# TERMINAL ZA NIZANJE CRTEZA U gif-DATOTEKU 
set term gif enhanced background "white" \
    animate delay 1 loop 1 \
    font 'Times-New-Roman' 18\
    size 1000,1200
set output "tree-100.gif"

# UKLANJANJE MARGINA
set samples 100000
set bmargin 0.
set lmargin 0.
set rmargin 0.
set tmargin 0.

set size ratio -1

# ITERATIVNO DODAVANJE VISE GRUPA BLOKOVA NA CRTEZ 
n = 100 # ukupno koraka (blokova polozaja)
j = 1 # dodaj vise novih blokova
k = 0 # 0-ti korak (pocetni polozaj)
# za svaki k=OD:DO:KORAK
while (k <= n) {
	set multiplot
	set origin 0.08,0.08
	set size 0.90,0.90
		set xlabel  "x"
		set ylabel  "y"
		set xrange [-0.6:0.9]
		set yrange [0:2]
		plot 'tree-100.txt' i 0:k:1 u 2:3 w l lw 2 lc rgb "blue" ti sprintf("%i koraka", k)
	unset multiplot
	k = k + j;
}

# RESET POSTAVKI
reset
unset output
set terminal GNUTERM
