#!/bin/bash
echo 'Starting AI-Butlers-v2'
source /root/Softwares/Miniconda3/etc/profile.d/conda.sh
conda activate server
cd /root/Projects/AI-Butlers-v2
python ./AI_Butlers.py -p "./config.yaml"
