import random
import json

import torch
import numpy as np

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

def get_response(msg, score):
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
    input_score = output_sentimientos[0]
    #If the model can`t recognize the input, set the value to 0
    non_valid_input_score = [0]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    pred_item = prob.item()
    
    #Change tags in order to lead the conversation
    if len(score) == 1:
        tag = 'interest'
    elif len(score) == 2:
        tag = 'time'
    #Release the direction of the speech, so user can access more conversation options or finish it anytime
    elif len(score) >= 3 and pred_item < 0.75 or len(score) >=3 and tag == 'about':
        #Tag-about prevents bot to redirect conversation to greeting phase if 'day' is used
        if tag == 'about':
            input_score = [0]
        score.pop(0)
        average = np.average(score)
        print(average)
        if average < 0.2:
            tag = 'joy'
        else:
            tag = 'support'

    #Select an answer for our bot
    if prob.item() > 0.75:
        # Return a tuple (response + user input input_score)
        for intent in intents['intents']:
            if tag == intent['tag']:
                return random.choice(intent['responses']), input_score

    return "Not sure I understand", non_valid_input_score


if __name__ == "__main__":
    print(random.choice(intents['intents']['tag'=='greeting']['responses']))
    #print("Hi! How are you feeling right now? (type 'quit' to exit)")
    # Declare an array to keep track on user reponses score
    score_resp = []
    
    while True:
        # sentence = "I feel sad"
        sentence = input("You: ")
        if sentence == "quit":
            break

        answer = get_response(sentence, score_resp)
        #Bot response will be the first part of the tuple provided by the 'get_response' function
        resp = answer[0]
        #Add the score to a previous array
        score_resp.append(answer[1][0])
        
        print(resp)
        print(score_resp)

