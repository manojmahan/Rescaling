import sys
import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_length_frequencies(ref_df, freq_df, output_file):
    plt.figure(figsize=(12, 6))
    #print("manoj kumar")
    plt.plot(ref_df['length'], ref_df['norm_query_freq'], label='rescaled', color='red')
    plt.plot(freq_df['length'], freq_df['norm_freq'], label='query', color='blue')
    plt.plot(ref_df['length'], ref_df['norm_freq'], label='reference', color='orange')
    plt.xlabel('Length')
    plt.ylabel('Normalized Frequency')
    plt.legend()
    plt.grid(True)
    plt.savefig(output_file)

def main(file_paths):
    for path in file_paths:
        ref_file = path.replace(".bed", "_rescaled_freq.tsv")
        query_file = path.replace(".bed", "_query_freq.tsv")
        ref_df = pd.read_csv(ref_file, sep='\t')
        freq_df = pd.read_csv(query_file, sep='\t')
        #print(ref_df.head())
        # Plot frequencies
        plot_length_frequencies(ref_df, freq_df, f"{path}_plot.png")
        
        # Remove temporary files after plotting
        os.remove(ref_file)
        os.remove(query_file)


if __name__ == "__main__":
    main(sys.argv[1:])
