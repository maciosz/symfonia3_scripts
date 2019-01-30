#!/usr/bin/python
import sys

# Usage:
# bedtools intersect -wao  -a $features -b $coverage > $bedtools_output
# ./calculate_coverage_over_features.py $bedtools_output $output [coordinates/ids] [sum]
#
# coordinates:
#   assumes $features file consists of 3 columns with coordinates,
#   saves the coordinates to the output file
# ids:
#   assumes $features file consists of 6 columns (coords, ID/name, score, strand),
#   saves the ID/name to the output file
# sum:
#   calculates sum of the coverage instead of the (default) mean.


infile = open(sys.argv[1])
output = open(sys.argv[2], 'w')
version = sys.argv[3]
what_to_calculate = "mean"
if len(sys.argv) > 4 and sys.argv[4] == "sum":
    what_to_calculate = "sum"
feature = {'name':False, 'coords':False, 'value':0}

for line in infile:
    line = line.strip().split()
    if version == 'coordinates':
        if len(line) != 8:
            sys.exit("Are you sure your bed was formatted correctly?"
                    " I assume 3 columns: chr, start, end."
                    " Anyway, sth went wrong while reading.")
        chromosome, feature_start, feature_end,  _, start, end, value, number_of_bases = line
    elif version == 'ids':
        if len(line) != 11:
            sys.exit("Are you sure your bed was formatted correctly?"
                    " I assume 6 columns: chr, start, end, ID, score, strand."
                    " Anyway, sth went wrong while reading.")
        chromosome, feature_start, feature_end, feature_name, score, strand,  _, start, end, value, number_of_bases = line
    else:
        sys.exit("Available options: ids coordinates; argument " + version + " not recognised")
    if number_of_bases == '0':
        summaric_value = 0
    else:
        summaric_value = float(value) * int(number_of_bases)
    if version == 'coordinates':
        condition = ([chromosome, feature_start, feature_end] != feature['coords'])
    elif version == 'ids':
        condition = (feature_name != feature['name'])
    if condition:
        if feature['name'] or feature['coords']:
            if what_to_calculate == "sum":
                value_to_write = int(feature['value'])
            elif what_to_calculate == "mean":
                feature_length = int(feature['coords'][2]) - int(feature['coords'][1])
                value_to_write = feature['value'] / feature_length
            if version == 'coordinates':
                to_write = feature['coords'] + [str(value_to_write)]
            elif version == 'ids':
                to_write = [feature['name'], str(value_to_write)]
            output.write('\t'.join(to_write))
            output.write('\n')
        feature['value'] = 0
        feature['coords'] = [chromosome, feature_start, feature_end]
        if version == 'ids':
            feature['name'] = feature_name
    feature['value'] += summaric_value

if what_to_calculate == "sum":
    value_to_write = int(feature['value'])
elif what_to_calculate == "mean":
    feature_length = int(feature['coords'][2]) - int(feature['coords'][1])
    average_value = feature['value'] / feature_length
if version == 'coordinates':
    to_write = feature['coords'] + [str(value_to_write)]
elif version == 'ids':
    to_write = [feature['name'], str(value_to_write)]
output.write('\t'.join(to_write))
output.write('\n')
  

"""
example input for coordinates mode:
chr1	19482	22400	chr1	19482	19490	0.562250441863	8
chr1	19482	22400	chr1	19490	19492	0.977285323141	2
chr1	19482	22400	chr1	19492	19506	0.562250441863	14
chr1	19482	22400	chr1	19506	19513	0.977285323141	7
chr1	19482	22400	chr1	19513	19528	0.562250441863	15
chr1	19482	22400	chr1	19528	19539	0.977285323141	11
chr1	19482	22400	chr1	19539	19547	0.562250441863	8
chr1	19482	22400	chr1	19547	19563	-0.0227225308891	16
chr1	19482	22400	chr1	19563	19585	-1.02272253089	22
chr1	19482	22400	chr1	19635	19654	-1.02272253089	19
input for ids mode:
chr1	28214	30117	MACS_peak_1	1032.05	+	chr1	28252	28312	0.0	60
chr1	28214	30117	MACS_peak_1	1032.05	+	chr1	28343	28392	0.0	49
chr1	28214	30117	MACS_peak_1	1032.05	+	chr1	28392	28403	1.0	11
chr1	28214	30117	MACS_peak_1	1032.05	+	chr1	28403	28432	0.0	29
chr1	28214	30117	MACS_peak_1	1032.05	+	chr1	28432	28452	1.0	20
chr1	28214	30117	MACS_peak_1	1032.05	+	chr1	28452	28465	0.0	13
chr1	28214	30117	MACS_peak_1	1032.05	+	chr1	28465	28492	1.0	27
chr1	28214	30117	MACS_peak_1	1032.05	+	chr1	28492	28522	0.0	30
chr1	28214	30117	MACS_peak_1	1032.05	+	chr1	28522	28525	1.0	3
chr1	28214	30117	MACS_peak_1	1032.05	+	chr1	28525	28582	0.0	57
"""
