set terminal canvas jsdir ""
set output "/Users/cmdb/qbb2017-answers/week-2/quast_results/results_2017_09_20_22_05_19/contigs_reports/nucmer_output/spades_nanopore_contigs.html"
set ytics ( \
 "0" 0, \
 "7000" 7000, \
 "14000" 14000, \
 "21000" 21000, \
 "28000" 28000, \
 "35000" 35000, \
 "42000" 42000, \
 "49000" 49000, \
 "56000" 56000, \
 "" 61012 \
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
set yrange [1:61012]
set linestyle 1  lt 1 lc rgb "red" lw 3 pt 7 ps 0.5
set linestyle 2  lt 3 lc rgb "blue" lw 3 pt 7 ps 0.5
set linestyle 3  lt 2 lc rgb "yellow" lw 3 pt 7 ps 0.5
plot \
 "/Users/cmdb/qbb2017-answers/week-2/quast_results/results_2017_09_20_22_05_19/contigs_reports/nucmer_output/spades_nanopore_contigs.fplot" title "FWD" w lp ls 1, \
 "/Users/cmdb/qbb2017-answers/week-2/quast_results/results_2017_09_20_22_05_19/contigs_reports/nucmer_output/spades_nanopore_contigs.rplot" title "REV" w lp ls 2
