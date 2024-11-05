import pandas as pd
import sys
import numpy as np
import matplotlib.pyplot as plt

def calculate_normalized_frequency(freq_df, total):
    freq_df['norm_freq'] = freq_df['frequency'] / total
    return freq_df

def rescale_reference(ref_df, max_norm_freq, max_length):
    ref_df['query_freq'] = ((ref_df['norm_freq'] / max_norm_freq) * max_length).astype(int)
    ref_df['norm_query_freq'] = ref_df['query_freq'] / ref_df['query_freq'].sum()
    return ref_df


def main(query_file, ref_file, output_file):
    freq_df = pd.read_csv(query_file, sep='\t').sort_values(by='length')
    ref_df = pd.read_csv(ref_file, sep='\t', names=['length', 'norm_freq']).sort_values(by='length')
    freq_df = calculate_normalized_frequency(freq_df, freq_df['frequency'].sum())

    max_index = np.argmax(abs(freq_df['norm_freq'] - ref_df['norm_freq']))
    max_norm_freq = ref_df['norm_freq'].iloc[max_index]
    max_length = ref_df['length'].iloc[max_index]

    rescaled_ref_df = rescale_reference(ref_df, max_norm_freq, max_length)
    length_query_dict = rescaled_ref_df.set_index('length')['query_freq'].to_dict()

    with open(output_file, 'w') as output_f:
        for line in sys.stdin:
            fields = line.split('\t')
            length = int(fields[2]) - int(fields[1])
            if length_query_dict.get(length, 0) > 0:
                output_f.write(line)
                length_query_dict[length] -= 1

    rescaled_ref_df.to_csv(output_file.replace(".bed", "_rescaled_freq.tsv"), sep='\t', index=False)
    freq_df.to_csv(output_file.replace(".bed", "_query_freq.tsv"), sep='\t', index=False)

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
