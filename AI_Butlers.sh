#!/bin/bash
echo 'starting project'
source /root/Software/miniconda3/etc/profile.d/conda.sh
conda activate AI
cd /root/Files/AI-Butlers-v2
python ./AI_Butlers.py -p "./config.json"
