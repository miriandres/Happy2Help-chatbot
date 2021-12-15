import json
import numpy as np
import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.preprocessing import sequence
stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

def tokenize(sentence):
    """
    split sentence into array of words/tokens
    a token can be a word or punctuation character, or number
    """
    return nltk.word_tokenize(sentence.lower())


def stem(word):
    """
    stemming = find the root form of the word
    examples:
    words = ["organize", "organizes", "organizing"]
    words = [stem(w) for w in words]
    -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """
    return bag of words array:
    1 for each known word that exists in the sentence, 0 otherwise
    example:
    sentence = ["hello", "how", "are", "you"]
    words = ["hi", "hello", "I", "you", "bye", "thank", "cool"]
    bog   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    # stem each word
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag

def stopwords(sentence):
    return [x for x in sentence if x not in nltk.corpus.stopwords.words('english')]

def codificacion_sentence(sentence):
    corpus_codificado = []
    diccionario = load_file('diccionario_lemma.json')
    sentence = [lemmatizer.lemmatize(word) for word in sentence]
    for word in sentence:
        if word in diccionario:
          corpus_codificado.append(diccionario[word])
        else:
          corpus_codificado.append(0)
    return corpus_codificado

def padding(corpus):
    return sequence.pad_sequences([corpus], maxlen=15)

def load_file(filename):
    with open(filename) as f:
        dicc = json.loads(f.read())
    return dicc