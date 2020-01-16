# API-chat-Linux-Senegal-Bot
AI Chat Bot en Python avec AIML

### Prérequis

Python versions 2.7 ou 3.3+.
Consulter le fichier requirements.txt pour activer la version du AIML qui correspond à la version de votre python

### Installation

Installer à partir de la source avec:

```
git clone https://github.com/Linux-Senegal/API-chat-Linux-Senegal-Bot.git
cd API-chat-Linux-Senegal-Bot
pip install -r requirements.txt
```
## Guide de démarrage

Lancer l'API
```
python app.py
```
### Teste

Teste l'API, sur votre navigateur taper l'adreese suivante 
http://127.0.0.1:5000/bot/?id=ID&talk=MESSAGE&user=UTILISATEUR
* **ID** - id de l'utilisateur  exemple 123456789
* **MESSAGE** - votre message exemple "qui est tu"
* **UTILISATEUR** - Non de l'interlocuteur exemple "Fatou"

http://127.0.0.1:5000/bot/?id=12345678&talk=qui%20est%20tu&user=fatou

## Développer avec

* [AIML](https://fr.wikipedia.org/wiki/AIML) - L’Artificial Intelligence Markup Language (AIML)
* [Python AIML](https://pypi.org/project/aiml/) - aiml implements an interpreter for AIML, the Artificial Intelligence Markup Language developed by Dr. Richard Wallace of the A.L.I.C.E. Foundation. It can be used to implement a conversational AI program.

## contribuer

Les contributions de toutes tailles sont les bienvenues. S'il vous plaît examiner notre [guide de contribution](CONTRIBUTING.md) pour commencer. Vous pouvez également aider en [rapportant des erreurs](https://github.com/Linux-Senegal/API-chat-Linux-Senegal-Bot/issues/new).

## License

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails
