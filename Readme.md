ReadMe.md

## HSDFinder (http://hsdfinder.com)
HSDFinder - an integrated tool to predict highly similar duplicates (HSDs) in eukaryotic genomes.
HSDFinder aims to become a useful platform for the identification and analysis of HSDs in the eukaryotic genomes, which deepen our insights into the gene duplication mechanisms driving the genome adaptation.

### What's new
Jan. 16th, 2021: HSDFinder and HSDatabase were cited by the Cell Press Journal iScience with the aticle name "Draft genome sequence of the Antarctic green alga _Chlamydomonas_ sp. UWO241" DOI:https://doi.org/10.1016/j.isci.2021.102084

Aug. 5th, 2020: Updated to version 1.5.
The result of the predicted HSDs is displayed in a spreadsheet, which offers an alternative way to browse the result in graphical and tabular form. The software presented here is the primary selection of HSDs, the manually curation should be done to filter the partial and pseudogenes.

Aug. 1st, 2020: Updated to version 1.0.
The web server is able to analyze the unannotated genome sequences by integrating the results from InterProScan (e.g., Pfam) and KEGG.

### INSTALLATION
Download the package and run
```tar -xzvf HSDFinder_v1.0.tar.gz```
Make sure the three python scripts (HSDFinder.py, operation.py, pfam.py) are under the same dirctory. 

### INPUT

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
2. Sequence MD5 digest (e.g. c82510c09b797ecced03c40f4da02ffb)
3. Sequence length (e.g. 247)
4. Analysis (e.g. Pfam)
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

### Running HSDFinder

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

#### OUTPUT
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

### Creating Heatmap

#### INPUT
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

#### Running

```
Usage: python HSD_to_KEGG.py -h
 HSD_to_KEGG.py -i <HSD file> -k <Gene list file with KO annotation> -n <species name> -o <output file name>

e.g., python HSD_to_KEGG.py -i '/.../.../##.species.txt' -k '/.../.../##.species_ko.txt' -n ##.species -o ##.species.out.txt
```

#### OUTPUT (.eps and .tsv)

*Example of the 8-column input file for HSDs of different species categorized under different KEGG functional categories*
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

*Example of the heatmap visualizing the HSDs across seven green algae *

![The heatmap example](http://url/to/img.png)

The color for the matrix reflects the number of HSDs across and the left hand side reflect different KEGG functional categories, such as carbohydrate metabolism, energy metabolism, and translation.

### What's NoBadWordsCombiner?
Unlike the NCBI-NR or UniProtKB/Swiss-Prot, although they provide valuable function description of the interested genes; however, many hypothetical proteins or ‘bad name’ proteins are also included in the respective database, which will mess up the interpretation of HSDs results. Although it is not the focus of this article, we have developed another software can integrate the gene function information together without ‘bad words’ including Nr-NCBI, UniProtKB/Swiss-Prot, KEGG, Pfam and GO etc..
```
Environmental Requirement: Pandas
To collect pandas packages : sudo pip install pandas

python NoBadWordsCombiner.py -h

Combiner.py -n <NCBI file> -s <Swiss file> -g <Gene list file> -k <Gene list file with KO annotation> -p <pfam file> -t <type> -o <output file name>
Or use Combiner.py --ncbi_file=<NCBI file> --swiss_file=<Swiss file> --gene_file=<Gene list file> --ko_file=<Gene list file with KO annotation> --pfam_file=<pfam file> --type=<type> -output_file=<output file name>
```

### Common questions (FAQ):

#### How to acquire the length of the gene models?
In some situations, if running errors occur with missing the gene length information. You can follow the sulution below.
For the genome with amino acid sequences, simply copy and paste the code below to create length of amino acid, make sure the gene identifier is consistent with the ones used as input files.
```
awk '/^>/{if (l!="") print l; print; l=0; next}{l+=length($0)}END{print l}' '/.../.../protein.fa' |paste - - |sed 's/>//g'|awk -F'\t' '{print $1"\t"$1"\t"100"\t"$2}' >##.protein.length.aa
```
This output file "##.protein.length.aa" can simply paste into the "##.BLAST.tabular" to run as the input file.


#### How to prepare the input files?

First, before running HSDFinder to acquire the HSDs of your interest genome, there are two spreadsheets in tab-separated values (tsv) format shall be prepared as input files. File examples are provided to guide the appropriate input files. A protein BLAST search of the genome models against themselves (E-value cut-off 10-5, BLASTp output format 6) will yield the first input file. The BLAST results should be 12-column spreadsheets including the key information from query name to percentage identity etc. The second spreadsheet is acquired from InterProScan which is an automatically software providing the protein signatures such as Pfam domain. The output file of InterProsScan is tab-separated values (tsv) format in default. 

#### How to run HSDFinder?

Then, the two spreadsheets can be safely submitted to HSDFinder with some personalized options. The HSDFinder is set default to filter those with near-identical protein lengths (within 10 amino acids) and >90% pairwise identities. The users always have an option to try different parameters from 50% to 100% identity or from within 0 aa to 100 aa variances to acquire the duplicates they like. The output of this step will be an 8-column spreadsheet integrating with the information of HSD identifier, gene copies number and Pfam domain. Additionally, the user can conveniently set different values to create a trendline graph of the gene copies numbers under different criteria.

#### How to visualize the HSDs across species?

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

