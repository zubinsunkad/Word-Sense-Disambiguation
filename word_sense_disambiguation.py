#!/usr/bin/env python3

from nltk.corpus import wordnet as wn
import argparse
from collections import defaultdict

'''
Below function is used to obtain the input - 
word and sentence to disambiguate.
'''

def input_parser():
    parser = argparse.ArgumentParser(description='Program for word sense disambiguation with overlap words', epilog = 'Sample commandline - $python simplified_lesk.py --word \
    "bank" --sentence "I need to withdraw money from bank"')
    parser.add_argument('--word', type=str, help='please provide word to disambiguate.',action='store')
    parser.add_argument('--sentence', type=str, help='please provide the input sentence',action='store')
    args = parser.parse_args()
    return args

'''
Below function is used to find the set of words in gloss
& examples of senses 
#line 6 of algorithm.
'''

def get_signature(sense):
    
    signature=[]
    defination_list = (sense.definition()).split(" ")
    for example in sense.examples():
        for word in example.split(" "):
            defination_list.append(word)
    
    signature=defination_list
    return(signature)

'''
Below function is used to compute word overlap
for each sense of word in wordnet.
'''
def compute_overlap(sense, signature,context):
    
    count = 0
    overlap_words = defaultdict(list)
    
    for word in context:
        if word in signature:
            count = count+1
            
            overlap_words[sense].append(word)
        else:
            pass
        
    print(dict(overlap_words))
    return(count)
    
'''
Below is the simplified lesk algorithm
as provided from the problem statement.
'''
def simplifiedLesk(word, sentence):
   
    senses = wn.synsets(word) ###get all the senses.
    best_sense = senses[0]   ###Initialize best sense to first sense.
    max_overlap = 0   ### Initial overlap = 0
    context = sentence.split(" ")   ### Assigning set of words in sentence to context.
   
    for sense in senses:
        
        signature = get_signature(sense)
        overlap = compute_overlap(sense, signature,context) ###compare the overlap
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = sense
    return(best_sense)


def main():
    
    args = input_parser()
    word = args.word
    sentence = args.sentence
    print("Here are the overlapping words - ")
    chosen_sense=simplifiedLesk(word, sentence) 
    print('The final chosen sense = ',chosen_sense)   
    
if __name__ == "__main__":
    main()