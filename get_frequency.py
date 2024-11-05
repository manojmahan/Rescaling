import sys
import pandas as pd

def calculate_frequency(input_stream):
    freq_dict = {}
    for line in input_stream:
        length = int(line.split('\t')[2]) - int(line.split('\t')[1])
        freq_dict[length] = freq_dict.get(length, 0) + 1
    return freq_dict

def main(output_path):
    freq_dict = calculate_frequency(sys.stdin)
    freq_df = pd.DataFrame(freq_dict.items(), columns=['length', 'frequency'])
    freq_df.to_csv(output_path, sep='\t', index=False)

if __name__ == "__main__":
    output_file = sys.argv[1]
    main(output_file)







#snakemake --snakefile main.smk subsample/query_files_subsample_to_reference_files_ewp_1 -j1