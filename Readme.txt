ReadMe.txt

1. HSDFinder
HSDFinder - an integrated tool to predict highly similar duplicates (HSDs) in eukaryotic genomes.
HSDFinder aims to become a useful platform for the identification and analysis of HSDs in the eukaryotic genomes, which deepen our insights into the gene duplication mechanisms driving the genome adaptation.

2.What's new
Aug. 5th, 2020: Updated to version 1.5.
The result of the predicted HSDs is displayed in a spreadsheet, which offers an alternative way to browse the result in graphical and tabular form. The software presented here is the primary selection of HSDs, the manually curation should be done to filter the partial and pseudogenes.

Aug. 1st, 2020: Updated to version 1.0.
The web server is able to analyze the unannotated genome sequences by integrating the results from InterProScan (e.g., Pfam) and KEGG.

3.INSTALLATION
Download the package and run

tar -xzvf gce.tar.gz 
make (to build the executable file "gce")

in the compiled version, you can use the gce directly.

4. USAGE


Use python3 HSDFinder.py to run HSDFinder
Or
Use python HSDFinder.py in Python2 environment

See argument details by python/python3 HSDFinder.py -h

gce -f test.freq -g total_kmer_num

Options:
-f      depth frequency file, is a list file containing at least two lines, the first line
	is depth and the second line is frequency(not the ratio) of the depth, other
	line is not recognized in the program. 
-g 	total kmer number counted from the reads. It is suggested to set this
	value for accurate estimation. If not, the total kmer number will be calculated using data in
	kmer_depth_file, which often missing data and cause error in estimation
-c	unqiue coverage depth. It is suggested to be set when there is no
	clear peak or there is clear un-unique peaks, especially when the
	heterozygous ratio is high.
-H	when the heterozygous caused peak is clear, it is suggested to use
	hybrid mode.
-b	when there is sequencing bias, you need to set the value.

-m	estiation mode, there are standard discrete model(default) and continuous model. You can
	set 1 to use continuous model, but its stability is not well.
-M      max depth value, information for larger depth will be ignored; If you increase this value,
	the estimation accuaray will be higher, but the run speed will be slower. 

-D	set the raw distance for continuous model, which decide the peak
	number.
	
-h: display help information.


Run examples:

First use a kmer counting tool to calculate kmer frequency for the sequencing data, get result file AF.kmer.freq.stat
	kmerfreq -k 17 -t 10 -p AF  ./raw_reads.lib

Then get the total kmer number for gce option "-g", and the depth frequency file for gce option "-f":
	less AF.kmer.freq.stat | grep "#Kmer indivdual number" 
	less AF.kmer.freq.stat | perl -ne 'next if(/^#/ || /^\s/); print; ' | awk '{print $1"\t"$2}' > AF.kmer.freq.stat.2colum 

Run gce in homozygous mode, suitable for homozygous and near-homozygous genome (-g and -f must be set at the same time) 
        ./gce -g 173854609857 -f AF.freq.stat.2colum >gce.table 2>gce.log

Run gce in heterzygous mode, siutable for heterozgyous genome (-H and -c must be set at the same time) 
        ./gce -g 173854609857 -f AF.freq.stat.2colum -c 75 -H 1 >gce2.table 2>gce2.log


5.OUTPUT
GCE generates two output files: gce.table and gce.log

The most valuable estimation results can be found at the end of gce.log file:

Final estimation table:
raw_peak        effective_kmer_species  effective_kmer_individuals      coverage_depth  genome_size     a[1]    b[1]
75      742400596       168346645871    75.8021 2.22087e+09     0.663012        0.271515

Column explanation:
raw_peak: the major peak on the kmer species curve, corresponding to the non-repeatitive and non-heterozygous genomic regions
effective_kmer_species: total number of genuine kmer species (without low-frequency kmers caused by sequencing errors)
effective_kmer_individuals: total number of genuine kmer individuals (without low-frequency kmers caused by sequencing errors)      
coverage_depth: estimated coverage depth of genuine kmers
genome_size: estimated genome size (genome_size = effective_kmer_individuals / coverage_depth)
a[1]: the ratio of unique kmers in all the kmer species in the genome
b[1]: the ratio of unique kmers in all the kmer individuals in the genome


6. Reference
X. Zhang, Yining. Hu, D. Smith (2020). HSDFinder- an integrated tool to predict highly similar duplicates in eukaryotic genomes. Genome Research, doi: XX.XX

7.Help 
The distribution version of HSDFinder is also available.
 Current version: v1 (5 August 2020) [download]. https://github.com/zx0223winner/HSDFinder

Links to the InterProScan and KEGG
 InterProscan: https://github.com/ebi-pf-team/interproscan
 KEGG : https://www.kegg.jp/kegg/

8. Contact
For comments and questions, send a message to Xi Zhang (xzha25@uwo.ca).
Usage of this site follows AWS’s Privacy Policy. In accordance with that policy, we use Matomo to collect anonymised data on visits to, downloads from, and searches of this site.
