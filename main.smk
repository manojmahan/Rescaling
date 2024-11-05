import os 

def get_query_files_name(query_dir):
    return [os.path.join(query_dir, f) for f in os.listdir(query_dir)]

def get_reference_files_name(referenc_dir):
    return [os.path.join(referenc_dir, f) for f in os.listdir(referenc_dir)]


rule get_frequency:
    input:
        query_directory = lambda wildcards: get_query_files_name(wildcards.query_dir)
    output: 
        x = "freq/{query_dir}.tsv"
    shell:
        "zcat {input.query_directory} | python get_frequency.py {output.x}"

rule Rescaling:
    input:
        query_directory = lambda wildcards: get_query_files_name(wildcards.query_dir),
        freqency_file = lambda wildcards:"freq/{query_dire}.tsv".format(query_dire=wildcards.query_dir),
        reference_directory = lambda wildcards: get_reference_files_name(wildcards.referenc_dir)
    output:
        samples = "subsample/{query_dir}_subsample_to_{referenc_dir}_sample_{number}.bed"
    shell:
        "zcat {input.query_directory} | shuf | python rescale.py {input.freqency_file} {input.reference_directory} {output.samples}"

rule plot:
    input:
        files_to_plot = lambda wildcards:["subsample/{query_dir}_subsample_to_{referenc_dir}_sample_{number}.bed".format(number=i,query_dir=wildcards.query_dir,referenc_dir=wildcards.referenc_dir) for i in range(int(wildcards.num_of_samples))],
        reference_directory = lambda wildcards: get_reference_files_name(wildcards.referenc_dir)
    output: 
        output_format = "subsample/{query_dir}_subsample_to_{referenc_dir}_ewp_{num_of_samples}"
    shell:
        "python plot.py {input.files_to_plot}"