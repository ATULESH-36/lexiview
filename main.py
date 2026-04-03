import os
import sys
sys.path.append(os.path.abspath('..'))
from src.preprocessing import clean_text,tokenize_text,remove_stopwords
from src.metrics import calculate_ttr,calculate_mattr,rare_word_ttr
from src.analysis import book_analysis
from config.config import LOW_THRESHOLD,HIGH_THRESHOLD
from src.utils import explain_lri

def calculate_LRI(text):
    text=clean_text(text)
    tokens=tokenize_text(text)
   
    tokens=remove_stopwords(tokens)
    
    if len(tokens)<=15:
        print("\n⚠️ Text too short for reliable analysis. Please provide a longer input.\n")
        return  None,None,None,None
    
    ttr=calculate_ttr(tokens)
    mattr=calculate_mattr(tokens)
    rw_ttr=min(rare_word_ttr(tokens),0.85)##capping the rare_word ttr to 0.85 to avoid it dominating the LRI 
    lri=0.6*mattr+0.25*ttr+0.15*rw_ttr
    return lri,ttr,mattr,rw_ttr


    
def main():
    text=input("Enter the text to analyze:")    
    
    lri,ttr,mattr,rw_ttr=calculate_LRI(text)
    if lri is None:
        return 
  
    print(f"Metrics with respect to the given text:\n")
    print(f"TTR:{ttr:.4f}")
    print(f"MATTR:{mattr:.4f}")
    print(f"Rare Word TTR:{rw_ttr:.4f}")
    print(f"Lexical Richness Index(LRI):{lri:.4f}")
    
    print(f"\n Lexical Complexity Analysis:\n")
    print(explain_lri(ttr,mattr,rw_ttr,lri))
    

if __name__=='__main__':
   main()