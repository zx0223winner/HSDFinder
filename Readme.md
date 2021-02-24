ReadMe.md

## HSDFinder (http://hsdfinder.com)
HSDFinder - an integrated tool to predict highly similar duplicates (HSDs) in eukaryotic genomes.
HSDFinder aims to become a useful platform for the identification and analysis of HSDs in the eukaryotic genomes, which deepen our insights into the gene duplication mechanisms driving the genome adaptation.

### What's new
Aug. 5th, 2020: Updated to version 1.5.
The result of the predicted HSDs is displayed in a spreadsheet, which offers an alternative way to browse the result in graphical and tabular form. The software presented here is the primary selection of HSDs, the manually curation should be done to filter the partial and pseudogenes.

Aug. 1st, 2020: Updated to version 1.0.
The web server is able to analyze the unannotated genome sequences by integrating the results from InterProScan (e.g., Pfam) and KEGG.

### INSTALLATION
Download the package and run
tar -xzvf HSDFinder_v1.0.tar.gz 
Make sure the three python scripts (HSDFinder.py, operation.py, pfam.py) are under the same dirctory. 

### USAGE

Must Use python3 HSDFinder.py to run HSDFinder
Or
Use python HSDFinder.py in Python2 environment
```
HSDFinder.py -i <inputfile> -p <percentage identity> -l <length> -f <pfam file> -t <type> -o <output file>
or 
use HSDFinder.py --input_file=<input file> --percentage_identity=<percentage identity> --length=<length> --file=<pfam file> --type=<type> --output_file=<output file>
```
```
See argument details by python/python3 HSDFinder.py -h
Options:
-i or --input_file	your fasta file
-p or --percentage_identity	identity percent e.g. For 90%, input 90.0
-l or --length	length e.g. 10
-f or --file	the file contain pfam
-t or --type	type e.g. Pfam
-o or --output_file	output file name

Run examples:

python3 HSDFinder.py -i '/.../.../##.BLAST.tabular' -p 90.0 -l 10 -f '/.../.../##.INTERPROSCAN.tsv' -t Pfam -o ##.species.txt
```
### OUTPUT
HSDFinder generates one output files: 8-column spreadsheet integrating with the information of HSD identifier, gene copies number and Pfam domain.

Example of the 8-column spreadsheet:
g735.t1 	g735.t1; g741.t1; g8053.t1 	744; 744; 747 	Pfam PF11999; PF11999; PF11999 	Protein of unknown function (DUF3494); Protein of unknown function (DUF3494); Protein of unknown function (DUF3494) 	2.2E-47; 7.8E-47; 2.5E-47 	IPR021884; IPR021884; IPR021884 	Ice-binding protein-like ; Ice-binding protein-like ; Ice-binding protein-like 

Column explanation:
Highly Similar Duplicates (HSDs) identifiers: The first gene model of the duplicate gene copies is used as the HSD identifers in default.
Duplicate gene copies (within 10 amino acids, ≥90% pairwise identities):g735.t1; g741.t1; g8053.t1
Amino acid length of duplicate gene copies (aa):744; 744; 747
Pfam identifier:PF11999; PF11999; PF11999
Pfam Description: Protein of unknown function (DUF3494); Protein of unknown function (DUF3494); Protein of unknown function (DUF3494)
InterPro Entry Identifier: IPR021884; IPR021884; IPR021884
InterPro Entry Description: Ice-binding protein-like ; Ice-binding protein-like ; Ice-binding protein-like
```
Usage: python HSD_to_KEGG.py -h
 HSD_to_KEGG.py -i <HSD file> -k <Gene list file with KO annotation> -n <species name> -o <output file name>

e.g., python HSD_to_KEGG.py -i '/.../.../##.species.txt' -k '/.../.../##.species_ko.txt' -n ##.species -o ##.species.out.txt
```
### What's NoBadWordsCombiner?
Unlike the NCBI-NR or UniProtKB/Swiss-Prot, although they provide valuable function description of the interested genes; however, many hypothetical proteins or ‘bad name’ proteins are also included in the respective database, which will mess up the interpretation of HSDs results. Although it is not the focus of this article, we have developed another software can integrate the gene function information together without ‘bad words’ including Nr-NCBI, UniProtKB/Swiss-Prot, KEGG, Pfam and GO etc..
```
Environmental Requirement: Pandas
To collect pandas packages : sudo pip install pandas

python NoBadWordsCombiner.py -h

Combiner.py -n <NCBI file> -s <Swiss file> -g <Gene list file> -k <Gene list file with KO annotation> -p <pfam file> -t <type> -o <output file name>
Or use Combiner.py --ncbi_file=<NCBI file> --swiss_file=<Swiss file> --gene_file=<Gene list file> --ko_file=<Gene list file with KO annotation> --pfam_file=<pfam file> --type=<type> -output_file=<output file name>
```
### How to acquire the length of the gene models?
In some situations, if running errors occur with missing the gene length information. You can follow the sulution below.
For the genome with amino acid sequences, simply copy and paste the code below to create length of amino acid, make sure the gene identifier is consistent with the ones used as input files.
```
awk '/^>/{if (l!="") print l; print; l=0; next}{l+=length($0)}END{print l}' '/.../.../protein.fa' |paste - - |sed 's/>//g'|awk -F'\t' '{print $1"\t"$1"\t"100"\t"$2}' >##.protein.length.aa
```
This output file "##.protein.length.aa" can simply paste into the "##.BLAST.tabular" to run as the input file.

### Common questions (FAQ):
*How to prepare the input files?
First, before running HSDFinder to acquire the HSDs of your interest genome, there are two spreadsheets in tab-separated values (tsv) format shall be prepared as input files. File examples are provided to guide the appropriate input files. A protein BLAST search of the genome models against themselves (E-value cut-off 10-5, BLASTp output format 6) will yield the first input file. The BLAST results should be 12-column spreadsheets including the key information from query name to percentage identity etc. The second spreadsheet is acquired from InterProScan which is an automatically software providing the protein signatures such as Pfam domain. The output file of InterProsScan is tab-separated values (tsv) format in default. 

*How to run HSDFinder?
Then, the two spreadsheets can be safely submitted to HSDFinder with some personalized options. The HSDFinder is set default to filter those with near-identical protein lengths (within 10 amino acids) and >90% pairwise identities. The users always have an option to try different parameters from 50% to 100% identity or from within 0 aa to 100 aa variances to acquire the duplicates they like. The output of this step will be an 8-column spreadsheet integrating with the information of HSD identifier, gene copies number and Pfam domain. Additionally, the user can conveniently set different values to create a trendline graph of the gene copies numbers under different criteria.

*How to visualize the HSDs across species? 
To comparative analyse the HSDs across different species, we developed an online heatmap plotting option to visualize the HSDs results in different KEGG pathway category. Firstly, the user will need to acqurie the HSDs outputs ("##.species.txt") from the former step, it is depending on how many species you are willing to compare with. But the default for plotting the heatmap is at least two species. There will be two files needed to plot the heatmap. Examples are given to guide the appropriate input files (Figure #). First input file is the outputs of your interest species after running the HSDFinder, the second file is retrieved from the KEGG database documented the correlation of KO accession with each gene model identifier. Since the species usually have unique gene model identifier, we recommend the user to submit the second KEGG pathway files corresponding to each species. Once the input files have been submitted, the HSDs numbers for each species will be displayed in a heatmap under different KEGG function category. On the left side, the color bar indicates a broad category of HSDs who have pathway function matches, such as carbohydrate metabolism, energy metabolism, translation etc. The color for the matrix indicates the number of HSDs across species. 

### Help 
The distribution version of HSDFinder is also available.
 Current version: v1 (5 August 2020) [download]. https://github.com/zx0223winner/HSDFinder
 
 Links to the InterProScan and KEGG
 InterProscan: https://github.com/ebi-pf-team/interproscan
 KEGG : https://www.kegg.jp/kegg/

### Contact
For comments and questions, send a message to Xi Zhang (xzha25@uwo.ca).
Usage of this site follows AWS’s Privacy Policy. In accordance with that policy, we use Matomo to collect anonymised data on visits to, downloads from, and searches of this site.
© Copyright (C) 2021
https://github.com/zx0223winner/HSDFinder.git

### Reference
X. Zhang, Yining. Hu, D. Smith (2020). HSDFinder- an integrated tool to predict highly similar duplicates in eukaryotic genomes. doi: XX.XX

