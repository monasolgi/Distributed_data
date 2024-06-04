#!/usr/bin/env python3
import sys
import nltk
from nltk.corpus import stopwords

stopwords=set(stopwords.words('english'))

def mapper():
    for line in sys.stdin:
        sentence=line.stripe()
        tokens=sentence.split()
        cleaned_tokens=[word for word in tokens if word.lower() not in stopwords]







if __name__=="__main__":
    mapper()