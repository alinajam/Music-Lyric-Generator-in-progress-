import random
from collections import defaultdict

import inflect
import contractions
import nltk
from langdetect import detect
from nltk.corpus import PlaintextCorpusReader
import re, string, unicodedata

country_root = '/Users/alinajam/Desktop/DC3/'
electronic_root = '/Users/alinajam/Desktop/DC3/Electronic'
folk_root = '/Users/alinajam/Desktop/DC3/Folk'
hiphop_root = '/Users/alinajam/Desktop/DC3/Hiphop'
indie_root = '/Users/alinajam/Desktop/DC3/Indie'
jazz_root = '/Users/alinajam/Desktop/DC3/Jazz'
metal_root = '/Users/alinajam/Desktop/DC3/Metal'
pop_root = '/Users/alinajam/Desktop/DC3/Pop'
rb_root = '/Users/alinajam/Desktop/DC3/R&B'
rock_root = '/Users/alinajam/Desktop/DC3/Rock'

countrylist = PlaintextCorpusReader(country_root, '.*.txt')
electroniclist = PlaintextCorpusReader(electronic_root, '.*.txt')
folklist = PlaintextCorpusReader(folk_root, '.*.txt')
hiphoplist = PlaintextCorpusReader(hiphop_root, '.*.txt')
indielist = PlaintextCorpusReader(indie_root, '.*.txt')
jazzlist = PlaintextCorpusReader(jazz_root, '.*.txt')
metallist = PlaintextCorpusReader(metal_root, '.*.txt')
poplist = PlaintextCorpusReader(pop_root, '.*.txt')
rblist = PlaintextCorpusReader(rb_root, '.*.txt')
rocklist = PlaintextCorpusReader(rock_root, '.*.txt')

country_corpus = []
for fileid in countrylist.fileids():
    with open(country_root + '/' + fileid) as f:
        file = f.read()
        try:
            if detect(file) == 'en':
                country_corpus.append(file)
        except:
            pass

electronic_corpus = []
for fileid in electroniclist.fileids():
    with open(electronic_root + '/' + fileid) as f:
        file = f.read()
        try:
            if detect(file) == 'en':
                electronic_corpus.append(file)
        except:
            pass

folk_corpus = []
for fileid in folklist.fileids():
    with open(folk_root + '/' + fileid) as f:
        file = f.read()
        try:
            if detect(file) == 'en':
                folk_corpus.append(file)
        except:
            pass

hiphop_corpus = []
for fileid in hiphoplist.fileids():
    with open(hiphop_root + '/' + fileid) as f:
        file = f.read()
        try:
            if detect(file) == 'en':
                hiphop_corpus.append(file)
        except:
            pass

indie_corpus = []
for fileid in indielist.fileids():
    with open(indie_root + '/' + fileid) as f:
        file = f.read()
        try:
            if detect(file) == 'en':
                indie_corpus.append(file)
        except:
            pass

jazz_corpus = []
for fileid in jazzlist.fileids():
    with open(jazz_root + '/' + fileid) as f:
        file = f.read()
        try:
            if detect(file) == 'en':
                jazz_corpus.append(file)
        except:
            pass

metal_corpus = []
for fileid in metallist.fileids():
    with open(metal_root + '/' + fileid) as f:
        file = f.read()
        try:
            if detect(file) == 'en':
                metal_corpus.append(file)
        except:
            pass

pop_corpus = []
for fileid in poplist.fileids():
    with open(pop_root + '/' + fileid) as f:
        file = f.read()
        try:
            if detect(file) == 'en':
                pop_corpus.append(file)
        except:
            pass

rb_corpus = []
for fileid in rblist.fileids():
    with open(rb_root + '/' + fileid) as f:
        file = f.read()
        try:
            if detect(file) == 'en':
                rb_corpus.append(file)
        except:
            pass

rock_corpus = []
for fileid in rocklist.fileids():
    with open(rock_root + '/' + fileid) as f:
        file = f.read()
        try:
            if detect(file) == 'en':
                rock_corpus.append(file)
        except:
            pass

def replace_numbers(words):
    """Replace all interger occurrences in list of tokenized words with textual representation"""
    p = inflect.engine()
    new_words = []
    for word in words:
        if word.isdigit():
            new_word = p.number_to_words(word)
            new_words.append(new_word)
        else:
            new_words.append(word)
    return new_words

def remove_non_ascii(words):
    """Remove non-ASCII characters from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = unicodedata.normalize('NFKD', word).encode('ascii', 'ignore').decode('utf-8', 'ignore')
        new_words.append(new_word)
    return new_words

def remove_punctuation(words):
    """Remove punctuation from list of tokenized words"""
    new_words = []
    for word in words:
        new_word = re.sub(r'[^\w\s]', '', word)
        if new_word != '':
            new_words.append(new_word)
    return new_words


def normalize(words):
    words = remove_non_ascii(words)
    words = remove_punctuation(words)
    words = replace_numbers(words)

    return words

# Country
print('\n')
print('Country lyrics:  ')
country_words = []
for i in country_corpus:
    country_words = country_words + nltk.word_tokenize(i)

normalize(country_words)


cfd = defaultdict(lambda: defaultdict(lambda: 0))
for i in range(len(country_words) - 2):  # loop to the next-to-last word
    cfd[country_words[i].lower()][country_words[i+1].lower()] += 1


list(nltk.bigrams(country_words))

def generate_model(cfdist, word , num=20):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()
        if word[0].isupper() == True:
            print(' ')


bigrams = nltk.bigrams(country_words)
cfd = nltk.ConditionalFreqDist(bigrams)

generate_model(cfd, random.choice(country_words))

# Electronic
print('\n')
print('Electronic lyrics:  ')
electronic_words = []
for i in electronic_corpus:
    electronic_words = electronic_words + nltk.word_tokenize(i)
#print(electronic_words)
normalize(electronic_words)
#print(list(nltk.bigrams(electronic_words)))

def generate_model(cfdist, word, num=20):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()
        if word[0].isupper()==True:
            print(' ')

bigrams = nltk.bigrams(electronic_words)
cfd = nltk.ConditionalFreqDist(bigrams)
#print(cfd['The'].max())

generate_model(cfd, random.choice(electronic_words))


# Folk
print('\n')
print('Folk lyrics:  ')
folk_words = []
for i in folk_corpus:
    folk_words = folk_words + nltk.word_tokenize(i)
#print(folk_words)
normalize(folk_words)
#print(list(nltk.bigrams(folk_words)))

def generate_model(cfdist, word, num=20):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()
        if word[0].isupper()==True:
            print(' ')

bigrams = nltk.bigrams(folk_words)
cfd = nltk.ConditionalFreqDist(bigrams)
#print(cfd['The'].max())

generate_model(cfd, random.choice(folk_words))


# Hiphop
print('\n')
print('Hiphop lyrics:  ')
hiphop_words = []
for i in hiphop_corpus:
    hiphop_words = hiphop_words + nltk.word_tokenize(i)
#print(hiphop_words)
normalize(hiphop_words)
#print(list(nltk.bigrams(hiphop_words)))

def generate_model(cfdist, word, num=20):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()
        if word[0].isupper()==True:
            print(' ')

bigrams = nltk.bigrams(hiphop_words)
cfd = nltk.ConditionalFreqDist(bigrams)
#print(cfd['The'].max())

generate_model(cfd, random.choice(hiphop_words))


# Indie
print('\n')
print('Indie lyrics:  ')
indie_words = []
for i in indie_corpus:
    indie_words = indie_words + nltk.word_tokenize(i)
#print(indie_words)
normalize(indie_words)
#print(list(nltk.bigrams(indie_words)))

def generate_model(cfdist, word, num=20):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()
        if word[0].isupper()==True:
            print(' ')

bigrams = nltk.bigrams(indie_words)
cfd = nltk.ConditionalFreqDist(bigrams)
#print(cfd['The'].max())

generate_model(cfd, random.choice(indie_words))


# Jazz
print('\n')
print('Jazz lyrics:  ')
jazz_words = []
for i in jazz_corpus:
    jazz_words = jazz_words + nltk.word_tokenize(i)
#print(jazz_words)
normalize(jazz_words)
#print(list(nltk.bigrams(jazz_words)))

def generate_model(cfdist, word, num=20):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()
        if word[0].isupper()==True:
            print(' ')

bigrams = nltk.bigrams(jazz_words)
cfd = nltk.ConditionalFreqDist(bigrams)
#print(cfd['The'].max())

generate_model(cfd, random.choice(jazz_words))


# Metal
print('\n')
print('Metal lyrics:  ')
metal_words = []
for i in metal_corpus:
    metal_words = metal_words + nltk.word_tokenize(i)
#print(metal_words)
normalize(metal_words)
#print(list(nltk.bigrams(metal_words)))

def generate_model(cfdist, word, num=20):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()
        if word[0].isupper()==True:
            print(' ')

bigrams = nltk.bigrams(metal_words)
cfd = nltk.ConditionalFreqDist(bigrams)
#print(cfd['The'].max())

generate_model(cfd, random.choice(metal_words))


# Pop
print('\n')
print('Pop lyrics:  ')
pop_words = []
for i in pop_corpus:
    pop_words = pop_words + nltk.word_tokenize(i)
#print(pop_words)
normalize(pop_words)
#print(list(nltk.bigrams(pop_words)))

def generate_model(cfdist, word, num=20):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()
        if word[0].isupper()==True:
            print(' ')

bigrams = nltk.bigrams(pop_words)
cfd = nltk.ConditionalFreqDist(bigrams)
#print(cfd['The'].max())

generate_model(cfd, random.choice(pop_words))


# R&B
print('\n')
print('R&B lyrics:  ')
rb_words = []
for i in rb_corpus:
    rb_words = rb_words + nltk.word_tokenize(i)
#print(rb_words)
normalize(rb_words)
#print(list(nltk.bigrams(rb_words)))

def generate_model(cfdist, word, num=20):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()
        if word[0].isupper()==True:
            print(' ')

bigrams = nltk.bigrams(rb_words)
cfd = nltk.ConditionalFreqDist(bigrams)
#print(cfd['The'].max())

generate_model(cfd, random.choice(rb_words))


# Rock
print('\n')
print('Rock lyrics:  ')
rock_words = []
for i in rock_corpus:
    rock_words = rock_words + nltk.word_tokenize(i)
#print(rock_words)
normalize(rock_words)
#print(list(nltk.bigrams(rock_words)))

def generate_model(cfdist, word, num=20):
    for i in range(num):
        print(word, end=' ')
        word = cfdist[word].max()
        if word[0].isupper()==True:
            print(' ')

bigrams = nltk.bigrams(rock_words)
cfd = nltk.ConditionalFreqDist(bigrams)
#print(cfd['The'].max())

generate_model(cfd, random.choice(rock_words))