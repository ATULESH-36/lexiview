import string
import re
from  nltk.corpus import stopwords

stop_words=set(stopwords.words('english'))

def remove_illustrations(text):
    return re.sub(r"\[illustration.*?\]", " ", text, flags=re.IGNORECASE)

def remove_contents_section(text):
    pattern = r"contents.*?chapter i\."
    return re.sub(pattern, "chapter i.", text, flags=re.IGNORECASE | re.DOTALL)

def remove_chapter_list(text):
    pattern = r"(chapter\s+[ivxlcdm]+\.\s*){5,}"
    return re.sub(pattern, " ", text, flags=re.IGNORECASE)

def remove_gutenberg_text(text):
    start_pattern=r"\*\*\* START OF .*?\*\*\*"
    end_pattern=r"\*\*\* END OF.*?\*\*\*"
    
    start_match=re.search(start_pattern,text,re.DOTALL)
    end_match=re.search(end_pattern,text,re.DOTALL)
    
    if start_match and end_match:
        return text[start_match.end():end_match.start()]
    
    return text


def clean_text(text):
    
    ##first converting the text into lower case
    text=text.lower()
    
    ##then removing the punctuation marks
    text = re.sub(f"[{re.escape(string.punctuation)}]", " ", text)
    
    ##remove digits 
    text=re.sub(r'\d+','',text)
    
    ##remove extra whitespaces
    text=re.sub(r'\s+',' ',text).strip()##here was the main culprit for the no spaces in the output file.
    
    return text

def tokenize_text(text):
    tokens=text.split()
    return tokens


def remove_stopwords(tokens):
    
    return [t for t in tokens if t not in stop_words]
def preprocess_pipeline(text):
    text=remove_gutenberg_text(text)
   
    text=remove_illustrations(text)
    
    text=remove_contents_section(text)
   
    text=remove_chapter_list(text)
   
    text=clean_text(text)
    
    tokens=tokenize_text(text)
    
    tokens=remove_stopwords(tokens)
   
    return tokens

