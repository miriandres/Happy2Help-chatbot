import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, codificacion_sentence, stopwords, tokenize, padding
from tensorflow.keras.models import load_model

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)

input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

# Cargar modelos

# Modelo torch: clasifica el tema de conversación
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

# Modelo keras: clasifica por sentimiento 
# Cerca de 0 joy
# Cerca de 1 sadness
model_sentiments = load_model('modelo_sentimientos_lemma.h5')

bot_name = "Happy2Help"

def get_response(msg):
    # Limpieza de la frase para el modelo Torch
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    # Limpieza de la frase para el modelo Keras
    sentence_sentiments = stopwords(sentence)
    X_sentimientos = codificacion_sentence(sentence_sentiments)
    
    # Predicción Torch
    output = model(X)
    _, predicted = torch.max(output, dim=1)
    
    tag = tags[predicted.item()]

    # Predicción Keras
    # Valor entre 0 y 1
    output_sentimientos = model_sentiments.predict(padding(X_sentimientos))

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    
    return "Not sure I understand"


if __name__ == "__main__":
    print("Hi! How are you feeling right now? (type 'quit' to exit)")
    while True:
        # sentence = "I feel sad"
        sentence = input("You: ")
        if sentence == "quit":
            break

        resp = get_response(sentence)
        print(resp)

