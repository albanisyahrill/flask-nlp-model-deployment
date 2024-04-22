import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import nltk
from nltk.corpus import stopwords as sw
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import re
import pickle

nltk.download('stopwords')

MAXLEN = 16
TRUNCATING = 'post'
PADDING = 'post'

stop_words = set(sw.words('indonesian'))
factory = StemmerFactory()
stemmer = factory.create_stemmer()

tokenizer_path = './deploy/tokenizer/tokenizer.pkl'

with open(tokenizer_path, 'rb') as token:
  tokenizer = pickle.load(token)
    
def regex_preprocess(sentence):
  sentence = re.sub(r'[^a-zA-Z\s]', ' ', sentence)
  sentence = re.sub(r'\s+', ' ', sentence)

  return sentence

def remove_stopwords_and_stemming(sentence):
  sentence = sentence.lower()
  words = sentence.split()
  words = [word for word in words if word.lower() not in stop_words]
  filtered_words = [stemmer.stem(word) for word in words]
  sentence = " ".join(filtered_words)
  
  return sentence

def text_padded_seq(input_text):
  text = regex_preprocess(input_text)
  text = remove_stopwords_and_stemming(text)
    
  text_seq = tokenizer.texts_to_sequences([text])
  text_padded = pad_sequences(text_seq, maxlen=MAXLEN, padding=PADDING, truncating=TRUNCATING)
    
  return text_padded