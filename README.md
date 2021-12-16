# Happy2Help Chatbot
Working from home and lack of physical contact has become our new reality. We are faced with uncertainty and mental healthcare tools are more necessary than ever.
Happy2Help provides assistance to people with no access to therapy and estimates their mental condition. A conversational interface with automated text interactions that recognizes behavioural patterns and give advice for those who are struggling.  High-risk patients are advised to contact with a licensed therapist.


## Initial Setup:
This repo currently contains the starter files.

Clone repo and create a virtual environment
```
$ git clone https://github.com/miriandres/Happy2Help-chatbot.git
$ cd HAPPY2HELP-CHATBOT
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk tensorflow
$ (venv) pip install numpy
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
