# Happy2Help Chatbot
Working from home and lack of physical contact has become our new reality. We are faced with uncertainty and mental healthcare tools are more necessary than ever.
Happy2Help provides assistance to people with no access to therapy and estimates their mental condition. A conversational interface with automated text interactions that recognizes behavioural patterns and give advice for those who are struggling.  High-risk patients are advised to contact with a licensed therapist.

<p align="center">
  <img width="250" src="https://user-images.githubusercontent.com/86624207/147703339-6a74f2f3-22b3-4d64-882d-d84caccdf4fb.gif" />
</p>

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
