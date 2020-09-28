import sys
import pandas as pd
from collections import defaultdict
import getopt


class Des:
    def __init__(self, g_type, length, hit_des, hit_name, p_id, e_value):
        self.g_type = g_type
        self.length = length
        self.hit_des = hit_des
        self.hit_name = hit_name
        self.p_id = p_id
        self.e_value = e_value


class Pfam:
    def __init__(self, name, ftype, pf, domain1, value, ipr, domain2):
        self.name = name
        self.ftype = ftype
        self.pf = pf
        self.domain1 = domain1
        self.value = value
        self.ipr = ipr
        self.domain2 = domain2


def run(ncbi_file, swiss_file, gene_file, ko_file, pfam_file, selected, output_file_name):
    output = pd.DataFrame(columns=('Gene', 'Length', 'NoBadName_Hit_Des', 'NoBadName_Hit_Name',
                                   'NoBadName_%ID', 'NoBadName_eValue', 'NCBI_Hit_Des', 'NCBI_Hit_Name',
                                   'NCBI_%ID', 'NCBI_eValue', 'Swiss_Hit_Des', 'Swiss_Hit_Name',
                                   'Swiss_%ID', 'Swiss_eValue'))
    if ncbi_file and swiss_file and gene_file:
        gene_dic = defaultdict(list)
        # load ncbi data
        try:
            with open(ncbi_file, 'r') as f:
                ncbi_lines = f.readlines()
                for ncbi_line in ncbi_lines:
                    ncbi_line = ncbi_line.strip('\n')
                    ncbi_items = ncbi_line.split('\t')
                    if len(ncbi_items) > 13:
                        gene_dic[ncbi_items[0]].append(Des('ncbi', ncbi_items[1], ncbi_items[2], ncbi_items[3],
                                                           ncbi_items[7], ncbi_items[8]))
        except OSError as e:
            print(str(e) + ". Error in file " + ncbi_file)
            sys.exit()
        # load swiss data
        try:
            with open(swiss_file, 'r') as f:
                swiss_lines = f.readlines()
                for swiss_line in swiss_lines:
                    swiss_line = swiss_line.strip('\n')
                    swiss_items = swiss_line.split('\t')
                    if len(swiss_items) > 13:
                        gene_dic[swiss_items[0]].append(Des('swiss', swiss_items[1], swiss_items[2], swiss_items[3],
                                                            swiss_items[7], swiss_items[8]))
        except OSError as e:
            print(str(e) + ". Error in file " + swiss_file)
            sys.exit()
        # no bad name output
        for key, value in gene_dic.items():
            result = value[0]
            ncbi_result = None
            swiss_result = None
            if len(value) > 1:
                find1 = 0
                find2 = 0
                for item in value:
                    if ("Uncharacterized" not in item.hit_des) and ("hypothetical" not in item.hit_des):
                        result = item
                        find1 = 1
                    elif ("hypothetical" in item.hit_des) and find1 == 0:
                        result = item
                        find2 = 1
                    elif find1 == 0 and find2 == 0:
                        result = item
                    if item.g_type == 'ncbi':
                        ncbi_result = item
                    elif item.g_type == 'swiss':
                        swiss_result = item
            else:
                result = value[0]
                if value[0].g_type == 'ncbi':
                    ncbi_result = value[0]
                elif value[0].g_type == 'swiss':
                    swiss_result = value[0]
            if ncbi_result and swiss_result:
                output = output.append(
                    pd.DataFrame({'Gene': [key], 'Length': [result.length], 'NoBadName_Hit_Des': [result.hit_des],
                                  'NoBadName_Hit_Name': [result.hit_name], 'NoBadName_%ID': [result.p_id],
                                  'NoBadName_eValue': [result.e_value], 'NCBI_Hit_Des': [ncbi_result.hit_des],
                                  'NCBI_Hit_Name': [ncbi_result.hit_name], 'NCBI_%ID': [ncbi_result.p_id],
                                  'NCBI_eValue': [ncbi_result.e_value], 'Swiss_Hit_Des': [swiss_result.hit_des],
                                  'Swiss_Hit_Name': [swiss_result.hit_name], 'Swiss_%ID': [swiss_result.p_id],
                                  'Swiss_eValue': [swiss_result.e_value]}), ignore_index=True)
            elif ncbi_result:
                output = output.append(
                    pd.DataFrame({'Gene': [key], 'Length': [result.length], 'NoBadName_Hit_Des': [result.hit_des],
                                  'NoBadName_Hit_Name': [result.hit_name], 'NoBadName_%ID': [result.p_id],
                                  'NoBadName_eValue': [result.e_value], 'NCBI_Hit_Des': [ncbi_result.hit_des],
                                  'NCBI_Hit_Name': [ncbi_result.hit_name], 'NCBI_%ID': [ncbi_result.p_id],
                                  'NCBI_eValue': [ncbi_result.e_value]}), ignore_index=True)
            elif swiss_result:
                output = output.append(
                    pd.DataFrame({'Gene': [key], 'Length': [result.length], 'NoBadName_Hit_Des': [result.hit_des],
                                  'NoBadName_Hit_Name': [result.hit_name], 'NoBadName_%ID': [result.p_id],
                                  'NoBadName_eValue': [result.e_value], 'Swiss_Hit_Des': [swiss_result.hit_des],
                                  'Swiss_Hit_Name': [swiss_result.hit_name], 'Swiss_%ID': [swiss_result.p_id],
                                  'Swiss_eValue': [swiss_result.e_value]}), ignore_index=True)
        # load gene list
        try:
            with open(gene_file, 'r') as f:
                gene_lines = f.readlines()
                for gene_line in gene_lines:
                    gene_line = gene_line.strip('\n')
                    if gene_line not in output['Gene'].values:
                        output = output.append(pd.DataFrame({'Gene': [gene_line]}))
        except OSError as e:
            print(str(e) + ". Error in file " + gene_file)
            sys.exit()
    elif ncbi_file == '':
        print('NCBI file is required.')
        sys.exit()
    elif swiss_file == '':
        print('Swiss file is required.')
        sys.exit()
    else:
        print('Gene list is required.')
        sys.exit()
    if ko_file or pfam_file:
        ko_dic = {}
        pfam_output = {}
        k_dic = {}
        if ko_file:
            output['KEGG_KO'] = None
            output['KEGG_Des'] = None
            try:
                with open(ko_file, 'r') as f:
                    ko_lines = f.readlines()
                    for ko_line in ko_lines:
                        ko_line = ko_line.strip('\n')
                        ko_items = ko_line.split('\t')
                        if len(ko_items) > 1 and not ko_items[1] == '':
                            ko_dic[ko_items[0]] = ko_items[1]
            except OSError as e:
                print(str(e) + ". Error in file " + ko_file)
                sys.exit()
            try:
                with open('KO database and its category.keg', 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        line = line.strip('\n')
                        if not line == "" and line.startswith('D'):
                            line = line.replace('D', '')
                            line = line.replace('      ', '')
                            ks = line.split('  ')
                            k_dic[ks[0]] = '\t' + ' '.join(ks[1:])
            except OSError as e:
                print(str(e))
                sys.exit()
        # col names
        n_name = selected
        n_no = selected + '_No'
        n_des = selected + '_Des'
        n_evalue = selected + '_evalue'
        if pfam_file:
            # create cols
            output[n_name] = None
            output[n_no] = None
            output[n_des] = None
            output[n_evalue] = None
            output['Interpro_No'] = None
            output['Interpro_domain'] = None
            # read pfam file content
            try:
                with open(pfam_file, 'r') as f:
                    pfam_lines = f.readlines()
                    pfam_dic = defaultdict(list)
                    for pfam_line in pfam_lines:
                        pfam_line = pfam_line.strip('\n')
                        pfam_items = pfam_line.split('\t')
                        if len(pfam_items) > 12 and pfam_items[3].lower() == selected.lower():
                            temp_key = pfam_items[0] + '/' + pfam_items[4]
                            pfam_dic[temp_key].append(Pfam(pfam_items[0], pfam_items[3], pfam_items[4],
                                                           pfam_items[5], pfam_items[8], pfam_items[11],
                                                           pfam_items[12]))
                        elif len(pfam_items) > 10 and pfam_items[3].lower() == selected.lower():
                            temp_key = pfam_items[0] + '/' + pfam_items[4]
                            pfam_dic[temp_key].append(Pfam(pfam_items[0], pfam_items[3], pfam_items[4],
                                                           pfam_items[5], pfam_items[8], '', ''))
            except OSError as e:
                print(str(e) + ". Error in file " + pfam_file)
                sys.exit()
            # select the one with smallest value
            d_temp = {}
            for key in pfam_dic.keys():
                min_index = 0
                min_value = 99999.0
                for i in range(len(pfam_dic[key])):
                    try:
                        if float(pfam_dic[key][i].value) < min_value:
                            min_index = i
                            min_value = float(pfam_dic[key][i].value)
                    except ValueError:
                        pass
                d_temp[key] = pfam_dic[key][min_index]
            pfam_dic.clear()
            # use gene name as key
            pfam_result_dic = defaultdict(list)
            for name in d_temp.keys():
                gene_name, pf_num = name.split('/')
                pfam_result_dic[gene_name].append(d_temp[name])
            d_temp.clear()
            # to one line
            for gene in pfam_result_dic.keys():
                pf_line = ''
                domain1_line = ''
                value_line = ''
                ipr_line = ''
                domain2_line = ''
                for n in range(len(pfam_result_dic[gene])):
                    pf_line += pfam_result_dic[gene][n].pf
                    domain1_line += pfam_result_dic[gene][n].domain1
                    value_line += pfam_result_dic[gene][n].value
                    ipr_line += pfam_result_dic[gene][n].ipr
                    domain2_line += pfam_result_dic[gene][n].domain2
                    if n < len(pfam_result_dic[gene]) - 1:
                        pf_line += '; '
                        domain1_line += '; '
                        value_line += '; '
                        ipr_line += '; '
                        domain2_line += '; '
                pfam_output[gene] = Pfam(gene, selected, pf_line, domain1_line, value_line, ipr_line, domain2_line)
            pfam_result_dic.clear()
        # write to dataframe
        output = output.set_index(['Gene'])
        for g, row in output.iterrows():
            if ko_file:
                if g in ko_dic.keys():
                    row['KEGG_KO'] = ko_dic[g]
                    ko_name = ko_dic[g]
                    if ko_name in k_dic.keys():
                        des = k_dic[ko_name]
                        row['KEGG_Des'] = des
                    else:
                        print(ko_dic[g] + " Description not found.")
            if pfam_file:
                if g in pfam_output.keys():
                    row[n_name] = pfam_output[g].ftype
                    row[n_no] = pfam_output[g].pf
                    row[n_des] = pfam_output[g].domain1
                    row[n_evalue] = pfam_output[g].value
                    row['Interpro_No'] = pfam_output[g].ipr
                    row['Interpro_domain'] = pfam_output[g].domain2
        output.reset_index(level=['Gene'], inplace=True)
    output.to_csv(output_file_name, sep='\t')


def main(argv):
    n_file = ''
    s_file = ''
    g_file = ''
    k_file = ''
    p_file = ''
    p_type = 'Pfam'
    o_file = 'NoBadName_Combiner_output.tsv'
    try:
        opts, args = getopt.getopt(argv, "hn:s:g:k:p:t:o:", ["ncbi_file=", "swiss_file=", "gene_file=", "ko_file=",
                                                             "pfam_file=", "type=", "output_file="])
    except getopt.GetoptError as e:
        print(str(e) + '. Use Combiner.py -h to see argument options')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('Combiner.py -n <NCBI file> -s <Swiss file> -g <Gene list file> -k <Gene list file with '
                  'KO annotation> -p <pfam file> -t <type> -o <output file name>')
            print('Or use Combiner.py --ncbi_file=<NCBI file> --swiss_file=<Swiss file> --gene_file=<Gene list file>'
                  ' --ko_file=<Gene list file with KO annotation> --pfam_file=<pfam file> --type=<type> '
                  '-output_file=<output file name>')
            sys.exit()
        elif opt in ("-n", "--ncbi_file"):
            n_file = arg
        elif opt in ("-s", "--swiss_file"):
            s_file = arg
        elif opt in ("-g", "--gene_file"):
            g_file = arg
        elif opt in ("-k", "--ko_file"):
            k_file = arg
        elif opt in ("-p", "--pfam_file"):
            p_file = arg
        elif opt in ("-t", "--type"):
            p_type = arg
        elif opt in ("-o", "--output_file"):
            o_file = arg
    run(n_file, s_file, g_file, k_file, p_file, p_type, o_file)


if __name__ == "__main__":
    main(sys.argv[1:])
