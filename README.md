# Chatbot 
Q/A bot to embed in the cli github that is trained on zowe docs, zowe command tree and any relevant github docs. Created during innovation week and intended to be finished during the December MSD Hackathon. 

Currently this chatbot is in a primitive state. Codebase includes previous attempts with other NLP SDKs. Chosen SDKs are [rasa](https://rasa.com/docs/rasa/) and [huggingface](https://huggingface.co/gpt2). Only just begining to understand the interactions between rasa file types (nlu, actions, stories, domain) and how to train created models.

Still need to:
- <b>Data-preprocessing</b>: figure out how to best gather all of the unstructured CLI documentation data (best if dynamically) and structure it/make it more homogenous for feeding into transformer.
- <b>nlu.yml</b>: create more intents / expanding the currently limited scope of the type of answers this chatbot can provide.

[Github Project Link](https://github.com/users/ATorrise/projects/2)
