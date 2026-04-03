import os
#base directory
BASE_DIR=os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))

#data_paths
RAW_DATA_PATH=os.path.join(BASE_DIR,'data','raw')
CLEAN_DATA_PATH=os.path.join(BASE_DIR,'data','cleaned')

#results path
PLOTS_PATH=os.path.join(BASE_DIR,'results','plots')
REPORTS_PATH=os.path.join(BASE_DIR,'results','reports')

#PARAMETERS
WINDOW_SIZE=100
RARE_WORD_THRESHOLD=3

LOW_THRESHOLD=0.2984672514238451 
HIGH_THRESHOLD=0.5188878296529894
