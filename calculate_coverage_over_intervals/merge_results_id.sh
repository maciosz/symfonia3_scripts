cut -f1 H3K4me3_WUM20160909_coverage_on_promoters.tsv > H3K4me3_coverage_on_promoters.tsv

for plik in H3K4me3_*201*on_promoters.tsv
do
    nazwa=$(echo $plik | cut -f2 -d'_')
    echo $nazwa >> H3K4me3_patients.txt
    cut -f2 $plik | paste H3K4me3_coverage_on_promoters.tsv - > tmp
    mv tmp H3K4me3_coverage_on_promoters.tsv
done

echo "ID" > tmp
cat H3K4me3_patients.txt >> tmp
cat tmp | tr '\n' '\t' > tmp1
echo >> tmp1
cat H3K4me3_coverage_on_promoters.tsv >> tmp1
mv tmp1 H3K4me3_coverage_on_promoters.tsv
rm tmp

