[![License](https://img.shields.io/badge/licence-GPLv2-blue)](https://www.gnu.org/licenses/old-licenses/gpl-2.0)


<font size=40>__HSDFinder Manual__</font>

1. [About HSDFinder](#sec1) </br>
        1.1 [What's NEW](#sec1.1) </br>
        1.2 [INSTALLATION](#sec1.2) </br>
2. [INPUT](#sec2) </br>
3. [Running HSDFinder](#sec3) </br>
4. [OUTPUT](#sec4) </br>
5. [Creating Heatmap](#sec5) </br>
        5.1 [INPUT](#sec5.1) </br>
        5.2 [RUNNING](#sec5.2) </br>
        5.3 [OUTPUT (.tsv and .eps)](#sec5.3) </br>
6. [Common questions (FAQ):](#sec6) </br>
        6.1 [How to prepare the input files?](#sec6.1) </br>
        6.2 [How to run HSDFinder?](#sec6.2) </br>
        6.3 [How to visualize the HSDs across species?](#sec6.3) </br>
        6.4 [How to acquire the length of the gene models?](#sec6.4) </br>
        6.5 [What's NoBadWordsCombiner?](#sec6.5) </br>
7. [Help](#sec7) </br>
8. [Contact](#sec8) </br>
9. [Reference](#sec9) </br>

<a name="sec1"></a>
## HSDFinder (http://hsdfinder.com)
HSDFinder - an integrated tool to predict highly similar duplicates (HSDs) in eukaryotic genomes.
HSDFinder aims to become a useful platform for the identification and analysis of HSDs in the eukaryotic genomes, which deepen our insights into the gene duplication mechanisms driving the genome adaptation.
<a name="sec1.1"></a>
### What's new 
Jan. 16th, 2021: HSDFinder and HSDatabase were cited by the Cell Press Journal iScience with the aticle name "Draft genome sequence of the Antarctic green alga _Chlamydomonas_ sp. UWO241" DOI:https://doi.org/10.1016/j.isci.2021.102084

Aug. 5th, 2020: Updated to version 1.5.
The result of the predicted HSDs is displayed in a spreadsheet, which offers an alternative way to browse the result in graphical and tabular form. The software presented here is the primary selection of HSDs, the manually curation should be done to filter the partial and pseudogenes.

Aug. 1st, 2020: Updated to version 1.0.
The web server is able to analyze the unannotated genome sequences by integrating the results from InterProScan (e.g., Pfam) and KEGG.
<a name="sec1.2"></a>
### 1. INSTALLATION
Download the package and run
```tar -xzvf HSDFinder_v1.0.tar.gz```
Make sure the three python scripts (HSDFinder.py, operation.py, pfam.py) are under the same dirctory. 

HSDFinder is developed to run on Linux. There are no versions planned for Windows or Apple (MAC OS X) operating systems. A minimum specification requirement is a machine with 2 cores and 4 GB of RAM, which will allow the analysis of a small number of sequences at a time. However the more resources the faster the analysis/more sequences can be analysed at a time.

Software requirements:<br />
64-bit Linux <br />
Python 3 <br />
<a name="sec2"></a>
### 2. INPUT
Input File 1: BLAST all-against-all using protein sequence in FASTA format

*Example of the 12-column input file 1:*
```
g735.t1	g735.t1	100.000	744	0	0	1	744	1	744	0.0	1375
g735.t1	g741.t1	96.237	744	28	0	1	744	1	744	0.0	1219
g735.t1	g8053.t1	90.196	51	3	2	6	55	3	52	7.50e-13	65.8
g735.t1	g7171.t1	77.632	608	121	13	144	740	147	750	3.98e-100	355
g735.t1	g11305.t1	97.500	40	1	0	17	56	14	53	5.80e-14	69.4
g741.t1	g741.t1	100.000	744	0	0	1	744	1	744	0.0	1375
g8053.t1	g8053.t1	100.000	747	0	0	1	747	1	747	0.0	1380
g7171.t1	g7171.t1	100.000	750	0	0	1	750	1	750	0.0	1386
g11305.t1	g11305.t1	100.000	1059	0	0	1	1059	1	1059	0.0	1956
```
Column explanation:
1. query_ID (e.g. g735.t1)
2. seq_ID (e.g. g741.t1)
3. percentage_identity (e.g. 96.237)
4. aligned length (e.g. 744)
5. mismatches (e.g. 28)
6. gap_openings (e.g. 0)
7. query_start (e.g. 1)
8. query_end (e.g. 744)
9. sequence_start (e.g. 1)
10. sequence_end (e.g. 744)
11. e-value (e.g. 0.0)
12. bit-score (e.g. 1219)

Input File 2: Protein sequence in FASTA format
*Example of the 13-column input file 2:*
```
g735.t1	c82510c09b797ecced03c40f4da02ffb	247	Pfam	PF11999	Protein of unknown function (DUF3494)	57	241	2.2E-47	T	15-11-2019	IPR021884	Ice-binding protein-like
g735.t1	c82510c09b797ecced03c40f4da02ffb	247	ProSiteProfiles	PS51257	Prokaryotic membrane lipoprotein lipid attachment site profile.	1	19	5.0	T	15-11-2019
g741.t1	8cf52deba53cb877fbd0af222ed48ce3	247	ProSiteProfiles	PS51257	Prokaryotic membrane lipoprotein lipid attachment site profile.	1	19	5.0	T	15-11-2019
g741.t1	8cf52deba53cb877fbd0af222ed48ce3	247	Pfam	PF11999	Protein of unknown function (DUF3494)	57	241	7.8E-47	T	15-11-2019	IPR021884	Ice-binding protein-like
g8053.t1	3d70a0c7f160037bf79f409bd805d577	248	Pfam	PF11999	Protein of unknown function (DUF3494)	58	244	2.5E-47	T	15-11-2019	IPR021884	Ice-binding protein-like
g7171.t1	9455b619e60679693d39c8191c410d18	249	Pfam	PF11999	Protein of unknown function (DUF3494)	58	244	8.0E-47	T	15-11-2019	IPR021884	Ice-binding protein-like
g11305.t1	299faccc0b8751e2919a8a332d5e123f	352	Pfam	PF11999	Protein of unknown function (DUF3494)	157	348	7.8E-55	T	15-11-2019	IPR021884	Ice-binding protein-like
```
Column explanation: 
1. Protein accession (e.g. g735.t1)
2. Sequence unique code (e.g. c82510c09b797ecced03c40f4da02ffb)
3. Sequence length (e.g. 247)
4. Protein signature (e.g. Pfam)
5. Signature accession (e.g. PF11999)
6. Signature description (e.g. Protein of unknown function (DUF3494))
7. Start location
8. Stop location
9. Score - is the e-value (or score) of the match reported by member database method (e.g. 2.2E-47)
10. Status - is the status of the match (T: true)
11. Date - is the date of the run (e.g. 15-11-2019)
12. InterPro annotations - accession (e.g. IPR021884)
13. InterPro annotations - description (e.g. Ice-binding protein-like)

Note: If a value is missing in a column, for example, the match has no InterPro annotation, a ‘-‘ is displayed.
<a name="sec3"></a>
### 3. Running HSDFinder

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
<a name="sec4"></a>
### 4. OUTPUT
HSDFinder generates one output files: 8-column spreadsheet integrating with the information of HSD identifier, gene copies number and Pfam domain.

*Example of the 8-column spreadsheet:*
```
g735.t1 	g735.t1; g741.t1; g8053.t1 	744; 744; 747 	Pfam PF11999; PF11999; PF11999 	Protein of unknown function (DUF3494); Protein of unknown function (DUF3494); Protein of unknown function (DUF3494) 	2.2E-47; 7.8E-47; 2.5E-47 	IPR021884; IPR021884; IPR021884 	Ice-binding protein-like ; Ice-binding protein-like ; Ice-binding protein-like 
```
Column explanation:
1. Highly Similar Duplicates (HSDs) identifiers: The first gene model of the duplicate gene copies is used as the HSD identifers in default. (e.g. g735.t1)
2. Duplicate gene copies (within 10 amino acids, ≥90% pairwise identities)(e.g. g735.t1; g741.t1; g8053.t1)
3. Amino acid length of duplicate gene copies (aa)(e.g. 744; 744; 747)
4. Pfam identifier (e.g. PF11999; PF11999; PF11999)
5. Analysis (e.g. Pfam / PRINTS / Gene3D)
6. Pfam Description (e.g. Protein of unknown function (DUF3494); Protein of unknown function (DUF3494); Protein of unknown function (DUF3494))
7. InterPro Entry Identifier (e.g. IPR021884; IPR021884; IPR021884)
8. InterPro Entry Description (e.g. Ice-binding protein-like ; Ice-binding protein-like ; Ice-binding protein-like)
<a name="sec5"></a>
### 5. Creating Heatmap
<a name="sec5.1"></a>
#### 1) INPUT
*Example of the 2-column input file for KO accession*
```
g10.t1	K07566
g11.t1
g12.t1
g13.t1
g14.t1
g15.t1	K09481
g16.t1	K00472
```
Column explanation:
1. Gene identifier (e.g. g10.t1)
2. KO accession with each gene model identifier retrieved from the KEGG database (e.g. K09481)
<a name="sec5.2"></a>
#### 2) RUNNING

```
Usage: python HSD_to_KEGG.py -h
 HSD_to_KEGG.py -i <HSD file> -k <Gene list file with KO annotation> -n <species name> -o <output file name>

e.g., python HSD_to_KEGG.py -i '/.../.../##.species.txt' -k '/.../.../##.species_ko.txt' -n ##.species -o ##.species.out.txt
```
<a name="sec5.3"></a>
#### 3) OUTPUT (.tsv and .eps)

*Example of the 8-column tab-delimited file (.tsv ) for HSDs of different species categorized under different KEGG functional categories* 
```
0	09101 Carbohydrate metabolism	00010 Glycolysis / Gluconeogenesis [PATH:ko00010]	K13979  yahK; alcohol dehydrogenase (NAP+) 		uwo241	g1713.t1	1
1	09101 Carbohydrate metabolism	00020 itrate cycle (TA cycle) [PATH:ko00020]	K00031  IH1, IH2, icd; isocitrate dehydrogenase 		uwo241	g3379.t1	1
2	09101 Carbohydrate metabolism	00030 Pentose phosphate pathway [PATH:ko00030]	K00036  G6P, zwf; glucose-6-phosphate 1-dehydrogenase 		uwo241	g852.t1	1
3	09101 Carbohydrate metabolism	00051 Fructose and mannose metabolism [PATH:ko00051]	K19355  MAN; mannan endo-1,4-beta-mannosidase 		uwo241	g3766.t1	1
4	09101 Carbohydrate metabolism	00053 Ascorbate and aldarate metabolism [PATH:ko00053]	K00434  E1.11.1.11; L-ascorbate peroxidase 		uwo241	g15878.t1	1
5	09103 Lipid metabolism	00073 utin, suberine and wax biosynthesis [PATH:ko00073]	K13356  FAR; alcohol-forming fatty acyl-CoA reductase 		uwo241	g6944.t1	1
6	09108 Metabolism of cofactors and vitamins	00130 Ubiquinone and other terpenoid-quinone biosynthesis [PATH:ko00130]	K17872  NC1, ndbB; demethylphylloquinone reductase 		uwo241	g269.t1, g13422.t1	2
```
Column explanation:
1. The identifier (e.g. 0)
2. Pathway category1	(e.g. 09101 Carbohydrate metabolism)
3. Pathway category2	(e.g. 00010 Glycolysis / Gluconeogenesis [PATH:ko00010])
4. KEGG ko_id	(e.g. K13979)
5. function	(e.g. yahK; alcohol dehydrogenase (NAP+))
6. species_name	(e.g. UWO241) Chlamydomonas sp. UWO241
7. hsds_id	(e.g. g1713.t1)
8. hsds_num (e.g. 1)

*Example of the heatmap file (.eps) visualizing the HSDs across seven green algae* 

![The heatmap example](https://github.com/zx0223winner/HSDatabse/blob/master/Test.png)

**The high resolution version can be found [here!](https://github.com/zx0223winner/HSDFinder/blob/master/Tutorial/Heatmap_example.pdf)** 

The color for the matrix reflects the number of HSDs across and the left hand side reflect different KEGG functional categories, such as carbohydrate metabolism, energy metabolism, and translation.

<a name="sec6"></a>
### 6. Common questions (FAQ):
<a name="sec6.1"></a>
#### How to prepare the input files?
Before running HSDFinder, two tab-delimited text files need to be prepared as inputs (Figure S1A). A protein BLAST search of the genes against themselves (Suggested parameters: E-value cut-off ≤10-5, BLASTP -outfmt 6) will yield the first input file. The BLAST result of the amino acid sequences shall be arranged in a 12-column tab-delimited text file, including the key information of the genes from the query name to percentage identity etc. (See more details in HSDFinder tutorial from GitHub). The second tab-delimited text file is acquired from the software InterProScan, which allow the genes to be scanned by different protein signature databases, such as Pfam domain. The output file of InterProsScan is tab-delimited text file in default. 
<a name="sec6.2"></a>
#### How to run HSDFinder?
The two tab-delimited text files then can be uploaded to HSDFinder with some personalized options. The default setting of HSDFinder filters highly similar duplicates (HSDs) with near-identical protein lengths (within 10 amino acids of each other) and ≥ 90% pairwise amino acid identities. Choosing such a relative strict cut-off might rule out other genuine duplicates from the list. But from our past experience with green algae genomes, the thresholds of the metrics selected here can represent the majority of detected highly similar duplicates. Since the duplicates vary from different eukaryotic organisms, users always have the option to lower the thresholds to filter duplicates on their datasets (e.g., from 30% to 100% pairwise amino acid identity and from within 0-100 amino acid length variances), although lowering the threshold of the metrics might risk of increasing of false positives. The output file of HSDFinder will be arranged in an 8-column tab-delimited text file containing the information, such as HSD identifier, gene copy number, and Pfam domain.
<a name="sec6.3"></a>
#### How to visualize the HSDs across species?
For comparative analyses of the HSDs across different species, we developed an online heatmap plotting option to visualize the HSDs results in different KEGG pathway categories. To do so, the user will need to generate HSDs results following the previous steps for the species of interest. The default for plotting the heatmap is at least two species and at least two files are needed to plot the heatmap. Examples are given to guide the appropriate input files (See more details in the hands-on protocol on creating heatmap with example data). The first input file is the outputs of your interest species after running HSDFinder; the second file is retrieved from the KEGG database documenting the correlation of KEGG Orthology (KO) accession with each gene model identifier (The detailed steps are guided in HSDFinder tutorial from GitHub). Once the input files have been submitted for each species, the HSDs will be displayed in a heatmap (the color for the matrix reflects the number of HSDs across species) and a tab-delimited text file under different KEGG functional categories, such as carbohydrate metabolism, energy metabolism, and translation.
<a name="sec6.4"></a>
#### How to acquire the length of the gene models?
In some situations, if running errors occur with missing the gene length information. You can follow the sulution below.
For the genome with amino acid sequences, simply copy and paste the code below to create length of amino acid, make sure the gene identifier is consistent with the ones used as input files.
```
awk '/^>/{if (l!="") print l; print; l=0; next}{l+=length($0)}END{print l}' '/.../.../protein.fa' |paste - - |sed 's/>//g'|awk -F'\t' '{print $1"\t"$1"\t"100"\t"$2}' >##.protein.length.aa
```
This output file "##.protein.length.aa" can simply paste into the "##.BLAST.tabular" to run as the input file.
<a name="sec6.5"></a>
#### What's NoBadWordsCombiner?
Unlike the NCBI-NR or UniProtKB/Swiss-Prot, although they provide valuable function description of the interested genes; however, many hypothetical proteins or ‘bad name’ proteins are also included in the respective database, which will mess up the interpretation of HSDs results. Although it is not the focus of this article, we have developed another software can integrate the gene function information together without ‘bad words’ including Nr-NCBI, UniProtKB/Swiss-Prot, KEGG, Pfam and GO etc..
```
Environmental Requirement: Pandas
To collect pandas packages : sudo pip install pandas

python NoBadWordsCombiner.py -h

Combiner.py -n <NCBI file> -s <Swiss file> -g <Gene list file> -k <Gene list file with KO annotation> -p <pfam file> -t <type> -o <output file name>
Or use Combiner.py --ncbi_file=<NCBI file> --swiss_file=<Swiss file> --gene_file=<Gene list file> --ko_file=<Gene list file with KO annotation> --pfam_file=<pfam file> --type=<type> -output_file=<output file name>
```
<a name="sec7"></a>
### Help 
The distribution version of HSDFinder is also available.
 Current version: v1 (5 August 2020) [download]. https://github.com/zx0223winner/HSDFinder
 
 Links to the InterProScan and KEGG
 InterProscan: https://github.com/ebi-pf-team/interproscan
 KEGG : https://www.kegg.jp/kegg/
<a name="sec8"></a>
### Contact
For comments and questions, send a message to Xi Zhang (xzha25@uwo.ca).
Usage of this site follows AWS’s Privacy Policy. In accordance with that policy, we use Matomo to collect anonymised data on visits to, downloads from, and searches of this site.
© Copyright (C) 2021
https://github.com/zx0223winner/HSDFinder.git
<a name="sec9"></a>
### Reference
X. Zhang, Yining. Hu, D. Smith (2020). HSDFinder- an integrated tool to predict highly similar duplicates in eukaryotic genomes. doi: XX.XX

