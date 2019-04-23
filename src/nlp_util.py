
import spacy
import warnings

'''
To use the more accurate but slower model use "en_core_web_lg"
otherwise use "en_core_web_sm"
'''
nlp = spacy.load("en_core_web_lg")


'''
Tokenizing a sentence using spaCy model
And puts them in a list grouped by part of speech
'''
def tokenize(sentence):
    doc = nlp(sentence)
    tags = []
    if doc != [] :
        tags.append([doc[0].pos_])
        for w in doc :
            if w.pos_ == "PUNCT" or w.lemma_ == "be" or w.pos_ == "DET":
                continue
            istag=False 
            for t in tags :
                if t[0] == w.pos_ :
                    t.append(w.text)
                    istag=True
            if istag==False :
                tag=[w.pos_,w.text]
                tags.append(tag)
    return tags

'''
Using spaCy model to compare between words
Added warning ignore in orfer to ignore small model warnings
'''
def compare(word1,word2):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return nlp(word1).similarity(nlp(word2))


