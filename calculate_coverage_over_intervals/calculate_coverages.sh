bed=$1
coverage=$2
output_suffix=$3
option=$4
sum=$5

nazwa=$(basename -s .bedgraph $coverage | cut -f1,2 -d'_')
echo $nazwa
bedtools_output=${nazwa}"_tmp_bedtools_output_"${output_suffix}
echo $bedtools_output
bedtools intersect -wao  -a $bed -b $coverage > $bedtools_output
output=${nazwa}"_coverage_${output_suffix}.tsv"
/home/maciosz/coverage_manipulation/calculate_coverage_over_intervals/calculate_coverage_over_features.py $bedtools_output $output $option $sum
rm $bedtools_output
