import os
import utils

download_data_cmd =
"""
G1K="../data"
BRCA_RESOURCES=$G1K
mkdir $G1K

echo extract BRCA gene region from chr13 and chr17
tabix -h $G1K/ALL.chr13.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz 13:32889080-32973809 > $G1K/chr13_brca2_1000g_GRCh37.vcf
tabix -h $G1K/ALL.chr17.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz 17:41191488-41322420 > $G1K/chr17_brca1_1000g_GRCh37.vcf
vcf-concat $G1K/chr13_brca2_1000g_GRCh37.vcf $G1K/chr17_brca1_1000g_GRCh37.vcf  > $G1K/brca12_1000g_GRCh37.vcf
CrossMap.py vcf $BRCA_RESOURCES/hg19ToHg38.over.chain.gz  $G1K/brca12_1000g_GRCh37.vcf $BRCA_RESOURCES/hg38.fa  $G1K/1000G_brca.hg38.vcf
vcf-sort $G1K/1000G_brca.hg38.vcf > $G1K/1000G_brca.sorted.hg38.vcf

echo Done!
"""

extract_high_af_cmd = 
"""
vcftools --vcf """ +
exon_fn + " --maf " + str(0.01) + """
"""

# File names
start_fn = """1000G_brca.hg38.vcf"""
exon_fn = """1000G_brca.hg38_exon.vcf"""
af_fn = """1000G_brca.hg38_exon_high_af.vcf"""

# Download data files
os.system(download_data_cmd)

# Extract exons
utils.extract_exon(start_fn, exon_fn)

# Extract high allele frequencies
os.system(extract_high_af_cmd)
