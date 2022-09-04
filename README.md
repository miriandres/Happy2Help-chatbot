# Happy2Help Chatbot
<img width="1552" src="/design/banner.png" />

<div align="center">

  Samsung Innovation Campus **IA bootcamp** final project. Málaga University.

  [![Github Repository](https://img.shields.io/static/v1?label=&message=Github%20Repository&color=85b3ff&style=for-the-badge&logo=github&logoColor=white)](https://github.com/miriandres/Happy2Help-chatbot/)
  
</div>

## Team Members:
- Miriam Andrés:  [@miriandres](https://github.com/miriandres)
- Jesica Míguez:  [@jemrosas](https://github.com/jemrosas)
- Sandra Orengo:  [@sof1508](https://github.com/sof1508)

## Built with 🛠️
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://www.tensorflow.org/)
[![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/en/2.2.x/)
[![JavaScript](https://img.shields.io/static/v1?label=&message=JavaScript&color=f7df1e&logo=javascript&logoColor=black&style=for-the-badge)](https://www.javascript.com/)
[![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)](https://www.w3schools.com/css/)
[![BEM Methodology](https://img.shields.io/static/v1?label=&message=BEM%20Methodology&color=17A1E6&logo=bem&logoColor=white&style=for-the-badge)](http://getbem.com/)

## Project:
**Happy2Help** is a **conversational interface** with automated text interactions that recognizes behavioral patterns and gives advice for those who are struggling. Built as a natural language understanding app in **Flask API**, using a **jinja2 template** and JavaScript. 

Tweets related to depression issues categorized from a labeled dataset gathered from Twitter API’s service using. TF-IDF weighting to classify their polarity.

### User Interface (UI)
<p align="center">
  <img width="250" src="https://user-images.githubusercontent.com/86624207/147703339-6a74f2f3-22b3-4d64-882d-d84caccdf4fb.gif" />
</p>
<img src="/design/palette.png" />

### Workflow
![Workflow](https://user-images.githubusercontent.com/86624207/187969376-b6e98cae-41d6-4647-b7d0-56d2607fd833.png)

### System Diagram
```
- app.py                    Graphical user interface
- chat.py                   Building a chatbot framework
- intents.json              Contains every reply under each intent in JSON format
- model.py                  Deep learning components for chat interaction
- model_sentiments.h5       Deep learning model for sentiments
- nltk_utils.py             Natural language processing with nltk
- diccionario.json          Contains the dictionary of words
- train.py                  Training
```

### Flowchart
![Flowchart](https://user-images.githubusercontent.com/86624207/187955932-1ba4ea3b-1ce2-47e4-a490-19581ee0848c.png)

### Training Methodology
![Training Methodology](https://user-images.githubusercontent.com/86624207/187957533-82632f90-8ab1-4626-a5b2-8a6ff5a14b6d.png)

### Model
![Model](https://user-images.githubusercontent.com/86624207/187970178-9c037a2d-cd16-42d5-88cd-43d77059bd7e.png)

## Initial Setup:
### a. Basic version
Clone repo and create a virtual environment
```
$ git clone https://github.com/miriandres/Happy2Help-chatbot.git
$ cd HAPPY2HELP-CHATBOT
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision tensorflow
$ (venv) pip install numpy nltk
```
Install nltk packages
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
>>> nltk.download('wordnet')
```
Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python app.py
```

### b. Conda version
```
$ git clone https://github.com/miriandres/Happy2Help-chatbot.git
$ cd HAPPY2HELP-CHATBOT
$ conda env create -f environment.yml
```
