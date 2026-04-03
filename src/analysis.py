from src.preprocessing import tokenize_text
from src.metrics import calculate_ttr
from src.metrics import calculate_mattr
import os
import sys
from src.metrics import rare_word_ttr
from src.metrics import normalize
import pandas as pd

def book_analysis(CLEAN_DATA_PATH):
    data=[]
    for file in os.listdir(CLEAN_DATA_PATH):
        if file.endswith('.txt'):
            file_path=os.path.join(CLEAN_DATA_PATH,file)
            with open(file_path,'r',encoding='utf-8') as f:
                text=f.read()
            
                tokens=tokenize_text(text)
                ttr=calculate_ttr(tokens)
                mattr=calculate_mattr(tokens)
                rw_ttr=rare_word_ttr(tokens)
            
                data.append({
                'book':file.replace('.txt',''),
                'ttr':ttr,
                'mattr':mattr,
                'rw_ttr':rw_ttr
                })
    df=pd.DataFrame(data)
    df['normalized_ttr']=df['ttr'].apply(lambda x:normalize(x,df['ttr'].min(),df['ttr'].max()))
    df['normalized_mattr']=df['mattr'].apply(lambda x:normalize(x,df['mattr'].min(),df['mattr'].max()))
    df['normalized_rw_ttr']=df['rw_ttr'].apply(lambda x:normalize(x,df['rw_ttr'].min(),df['rw_ttr'].max()))
    df['LRI']=0.5*df['normalized_mattr']+0.2*df['normalized_ttr']+0.3*df['normalized_rw_ttr']
    return df     