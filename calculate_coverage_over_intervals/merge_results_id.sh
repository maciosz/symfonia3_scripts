cut -f1 H3K4me3_DA01_coverage_on_promoters.tsv > H3K4me3_coverage_on_promoters.tsv

for file in H3K4me3_*on_promoters.tsv
do
    name=$(echo $plik | cut -f2 -d'_')
    echo $name >> H3K4me3_patients.txt
    cut -f2 $file | paste H3K4me3_coverage_on_promoters.tsv - > tmp
    mv tmp H3K4me3_coverage_on_promoters.tsv
done

echo "ID" > tmp
cat H3K4me3_patients.txt >> tmp
cat tmp | tr '\n' '\t' > tmp1
echo >> tmp1
cat H3K4me3_coverage_on_promoters.tsv >> tmp1
mv tmp1 H3K4me3_coverage_on_promoters.tsv
rm tmp

