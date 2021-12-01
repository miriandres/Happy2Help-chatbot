# Happy2Help Chatbot
Working from home and lack of physical contact has become our new reality. We are faced with uncertainty and mental healthcare tools are more necessary than ever. 
Happy2Help provides assistance to people with no access to therapy and estimates their mental condition. A conversational interface with automated text interactions that recognizes behavioural patterns and give advice for those who are struggling.  High-risk patients are advised to contact with a licensed therapist.


## Initial Setup:
This repo currently contains the starter files.

Clone repo and create a virtual environment
```
$ git clone https://github.com/miriandres/Happy2Help-chatbot.git
$ cd chatbot-deployment
$ python3 -m venv venv
$ . venv/bin/activate
```
Install dependencies
```
$ (venv) pip install Flask torch torchvision nltk
```
Install nltk package
```
$ (venv) python
>>> import nltk
>>> nltk.download('punkt')
```
Modify `intents.json` with different intents and responses for your Chatbot

Run
```
$ (venv) python train.py
```
This will dump data.pth file. And then run
the following command to test it in the console.
```
$ (venv) python chat.py
```

Now for deployment follow my tutorial to implement `app.py` and `app.js`.

## Note
We implement the first approach using jinja2 templates within our Flask app. Only slight modifications are needed to run the frontend separately. I put the final frontend code for a standalone frontend application in the [standalone-frontend](/standalone-frontend) folder.