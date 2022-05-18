# RESET POSTAVKI
unset multiplot
reset
set encoding utf8

# ODABIR gif-TERMINALA ZA SLAGANJE NIZA SLIKA
set term gif animate  \
    font "Arial,18pt" \
    size 1000,1000
set output "solar_system.gif"

nk=50000 # ukupan broj koraka (slika)
dk=100  # duljina koraka pi šetanju po blokovima
k=0   # početni korak (blok podataka)

set xlabel 'x / m'
set ylabel 'y / m' 

# CRTANJE NIZA SLIKA
while (k <= nk) {
    plot [-950000000000:900000000000][-900000000000:900000000000] 'Z4.txt' i k u 2:3 w p pt 7 ps 5 lc rgb "yellow" ti 'Sun', \
                        'Z4.txt' i k u 4:5 w p pt 7 ps 5 lc rgb "blue" ti 'Earth', \
                        'Z4.txt' i k u 6:7 w p pt 7 ps 5 lc rgb "orange" ti 'Jupiter'
    k = k + dk  
}

# RESET POSTAVKI
unset output
set terminal GNUTERM
