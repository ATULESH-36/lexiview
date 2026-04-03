import numpy as np
from collections import Counter

def calculate_ttr(tokens):
    total_tokens=len(tokens)
    unique_tokens=len(set(tokens))
    
    if total_tokens==0:
        return 0.0
    return unique_tokens/total_tokens

def calculate_rttr(tokens):
    total_tokens=len(tokens)
    unique_tokens=len(set(tokens))
    
    if total_tokens==0:
        return 0.0
    
    return unique_tokens/np.sqrt(total_tokens)

def calculate_cttr(tokens):
    total_tokens=len(tokens)
    unique_tokens=len(set(tokens))
    
    if total_tokens==0:
        return 0.0
    
    return unique_tokens/np.sqrt(2*total_tokens)

def calculate_mattr(tokens,window_size=100):
    window_size=min(window_size,len(tokens)//2) ##to ensure that window size is not too big for shorter text
    if len(tokens)<window_size:
        return calculate_ttr(tokens)
    
    ttr_values=[]
    for i in range(len(tokens)-window_size+1):
        window=tokens[i:i+window_size]
        ttr_values.append(calculate_ttr(window))
        
    return np.mean(ttr_values)    
        
def rare_word_ttr(tokens,threshold=2):
    
    freq=Counter(tokens)
    rare_words=[w for w in tokens if freq[w]<=max(2,0.05*len(tokens))]
    # print(f"Here is the list of rare words:{rare_words}")
    if len(rare_words)==0:
        return 0.0
    
    return calculate_ttr(rare_words)
    
def normalize(value,min_val,max_val):
    if max_val==min_val:
        return 0.0
    return (value-min_val)/(max_val-min_val)
    
