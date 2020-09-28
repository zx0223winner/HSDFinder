# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


import sys
import getopt
import operation


def main(argv):
    input_file = ''
    percentage = 90.0
    length = -1
    pfam = ''
    p_type = "Pfam"
    output_file = 'HSDFinder_result.txt'
    try:
        opts, args = getopt.getopt(argv, "hi:p:l:f:t:o:", ["input_file=", "percentage_identity=", "length=", "file=",
                                                           "type=", "output_file="])
    except getopt.GetoptError:
        print('use main.py -h to see argument options')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('HSDFinder.py -i <inputfile> -p <percentage identity> -l <length> -f <pfam file> -t <type> -o '
                  '<output file>')
            print(
                'or use HSDFinder.py --input_file=<input file> --percentage_identity=<percentage identity> '
                '--length=<length> --file=<pfam file> --type=<type> --output_file=<output file>\n'
                '-i or --input_file\tyour fasta file\n'
                '-p or --percentage_identity\tidentity percent e.g. For 90%, input 90.0\n'
                '-l or --length\tlength e.g. 10\n'
                '-f or --file\tthe file contain pfam\n'
                '-t or --type\ttype e.g. Pfam\n'
                '-o or --output_file\toutput file name')
            sys.exit()
        elif opt in ("-i", "--input_file"):
            input_file = arg
        elif opt in ("-p", "--percentage_identity"):
            try:
                percentage = float(arg)
            except ValueError:
                print("Input value error: the percentage identity must be a number.\n"
                      "use HSDFinder.py -h to see more information.")
                sys.exit(2)
        elif opt in ("-l", "--length"):
            try:
                length = int(arg)
            except ValueError:
                print("Input value error: the length must be a number.\n"
                      "use HSDFinder.py -h to see more information.")
                sys.exit(2)
        elif opt in ("-f", "--file"):
            pfam = arg
        elif opt in ("-t", "--type"):
            p_type = arg
        elif opt in ("-o", "--output_file"):
            output_file = arg
    if length == -1:
        length = 10
    if input_file == "" or pfam == "":
        print("no input file or no pfam file.")
        sys.exit(2)
    else:
        result = operation.pfam_file_fun(input_file, percentage, length, pfam, p_type, output_file)
        print("Output file " + result + " saved")


if __name__ == "__main__":
    main(sys.argv[1:])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
