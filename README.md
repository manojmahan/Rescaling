# Rescaling

### download the data 
```
mkdir query_dir
cd query_dir
curl -JLO "https://figshare.com/ndownloader/files/49358275?private_link=727f8d920a1b8415f09a"
curl -JLO "https://figshare.com/ndownloader/files/49358278?private_link=727f8d920a1b8415f09a"
cd ..
```
```
mkdir referenc_dir
cd referenc_dir
curl -JLO "https://figshare.com/ndownloader/files/49358317?private_link=2d3d4d60a82de9cc3cc6"
cd ..
```
### I kept the 3 veriables 
1. query files
2. reference files
3. number of samples to extract/rescale

### run snakemake
```
snakemake --sankemfile main.smk subsample/query_dir_subsample_to_referenc_dir_ewp_3
```
 
