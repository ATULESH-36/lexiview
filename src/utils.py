import os
from config.config import LOW_THRESHOLD,HIGH_THRESHOLD

def ensure_dir(path):
    os.makedirs(path,exist_ok=True)
    
def list_text_files(path):
    return [f for f in os.listdir(path) if f.endswith('.txt')]    

def save_plot(fig,path,filename):
    ensure_dir(path)
    fig.savefig(os.path.join(path,filename),bbox_inches='tight')
    

  
    
def explain_lri(ttr, mattr, rw_ttr, lri):

    explanation = []
    if ttr < 0.5:
        ttr_desc = f"low lexical diversity (TTR={ttr:.2f}), indicating repetition of words"
    elif ttr < 0.8:
        ttr_desc = f"moderate lexical diversity (TTR={ttr:.2f}), indicating a balanced vocabulary"
    else:
        ttr_desc = f"high lexical diversity (TTR={ttr:.2f}), indicating rich and varied word usage"
    
  
    if mattr < 0.6:
        mattr_desc = f"low consistency in vocabulary usage (MATTR={mattr:.2f})"
    elif mattr < 0.8:
        mattr_desc = f"moderate consistency in vocabulary usage (MATTR={mattr:.2f})"
    else:
        mattr_desc = f"highly consistent vocabulary usage throughout the text (MATTR={mattr:.2f})"
    
    
    if rw_ttr < 0.4:
        rw_desc = f"limited presence of rare or advanced words (RW-TTR={rw_ttr:.2f})"
    elif rw_ttr < 0.7:
        rw_desc = f"moderate presence of less frequent words (RW-TTR={rw_ttr:.2f})"
    else:
        rw_desc = f"strong presence of rare and informative words (RW-TTR={rw_ttr:.2f})"

    explanation.append(ttr_desc)
    explanation.append(mattr_desc)
    explanation.append(rw_desc)

    if ttr < 0.5 and mattr < 0.6:
        overall = "The text is simple and repetitive, with limited variation in vocabulary."
    
    elif ttr < 0.5 and mattr >= 0.6:
        overall = "The text exhibits repetition, but still maintains a degree of  consistency in  vocabulary usage."
    
    elif ttr >= 0.5 and mattr >= 0.7 and rw_ttr >= 0.7:
        overall = "The text demonstrates a high level of lexical richness, with consistent and diverse vocabulary usage across the text."
    
    elif ttr >= 0.5 and mattr >= 0.6:
        overall = "The text has a balanced level of complexity with moderate diversity and consistency."
    
    else:
        overall = "The text shows mixed characteristics, with varying levels of vocabulary richness."

   
    return (
        "Lexical Analysis:\n"
        f"- {ttr_desc}\n"
        f"- {mattr_desc}\n"
        f"- {rw_desc}\n\n"
        "Overall Interpretation:\n"
        f"{overall}"
    ) 