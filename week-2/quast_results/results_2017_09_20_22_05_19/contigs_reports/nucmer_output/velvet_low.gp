set terminal canvas jsdir ""
set output "/Users/cmdb/qbb2017-answers/week-2/quast_results/results_2017_09_20_22_05_19/contigs_reports/nucmer_output/velvet_low.html"
set ytics ( \
 "0" 0, \
 "900" 900, \
 "1800" 1800, \
 "2700" 2700, \
 "3600" 3600, \
 "4500" 4500, \
 "5400" 5400, \
 "6300" 6300, \
 "7200" 7200, \
 "" 7243 \
)
set size 1,1
set grid
set key outside bottom right
set border 0
set tics scale 0
set xlabel "Reference" noenhanced
set ylabel "Assembly" noenhanced
set format "%.0f"
set xrange [1:*]
set yrange [1:7243]
set linestyle 1  lt 1 lc rgb "red" lw 3 pt 7 ps 0.5
set linestyle 2  lt 3 lc rgb "blue" lw 3 pt 7 ps 0.5
set linestyle 3  lt 2 lc rgb "yellow" lw 3 pt 7 ps 0.5
plot \
 "/Users/cmdb/qbb2017-answers/week-2/quast_results/results_2017_09_20_22_05_19/contigs_reports/nucmer_output/velvet_low.fplot" title "FWD" w lp ls 1, \
 "/Users/cmdb/qbb2017-answers/week-2/quast_results/results_2017_09_20_22_05_19/contigs_reports/nucmer_output/velvet_low.rplot" title "REV" w lp ls 2
