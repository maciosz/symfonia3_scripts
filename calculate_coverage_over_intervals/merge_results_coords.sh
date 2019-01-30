cut -f1-3 DNase_WUM20160909_coverage_normalised_on_H3K27ac_peaks_outside_promoters.tsv > DNase_coverage_normalised_on_H3K27ac_peaks_outside_promoters.tsv

for plik in DNase_*201*outside_promoters.tsv
do
    nazwa=$(echo $plik | cut -f2 -d'_')
    echo $nazwa >> DNase_patients.txt
    cut -f4 $plik | paste DNase_coverage_normalised_on_H3K27ac_peaks_outside_promoters.tsv - > tmp
    mv tmp DNase_coverage_normalised_on_H3K27ac_peaks_outside_promoters.tsv
done

echo "chr	start	end" > tmp
cat DNase_patients.txt >> tmp
cat tmp | tr '\n' '\t' > tmp1
echo >> tmp1
cat DNase_coverage_normalised_on_H3K27ac_peaks_outside_promoters.tsv >> tmp1
mv tmp1 DNase_coverage_normalised_on_H3K27ac_peaks_outside_promoters.tsv

