    plot [-100:100][-100:100] 'primjer2.txt' i b u 1:2 w p pt 6 ps 0.5 lc rgb "blue" title sprintf("t = %i Δt", b*pk)
    b = b + db
    if (b <= Nb) reread