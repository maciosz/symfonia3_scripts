cut -f1-3 DNase_DA01_coverage_on_H3K27ac_peaks.tsv > DNase_coverage_on_H3K27ac_peaks.tsv

for file in DNase_*peaks.tsv
do
    name=$(echo $file | cut -f2 -d'_')
    echo $name >> DNase_patients.txt
    cut -f4 $file | paste DNase_coverage_on_H3K27ac_peaks.tsv - > tmp
    mv tmp DNase_coverage_on_H3K27ac_peaks.tsv
done

echo "chr	start	end" > tmp
cat DNase_patients.txt >> tmp
cat tmp | tr '\n' '\t' > tmp1
echo >> tmp1
cat DNase_coverage_on_H3K27ac_peaks.tsv >> tmp1
mv tmp1 DNase_coverage_on_H3K27ac_peaks.tsv

