# Project Documentation

Currently this chatbot is in a primitive state. Have only just begun to understand the interactions between rasa file types (nlu, actions, stories, domain) and how to use trainings and created models.

Still need to:
- <b>Data-preprocessing</b>: figure out how to best gather all of the unstructured CLI documentation data (best if dynamically) and structure it/make it more homogenous for feeding into transformer.
- <b>nlu.yml</b>: anticipate more intents / expanding the currently limited scope of the type of answers this chatbot can provide


## First Steps
1. `cd rasaProject` then `pip install -r requirements.txt`
2. <b>Train model</b> off of nlu data: `rasa train nlu`
3. <b>Run model</b>: `rasa run --model models --enable-api --endpoints endpoints.yml`
4. <b>Use model</b> :
    1. Open a new terminal and run shell:
        - `rasa run actions`: starts the actions server (REQUIRED)
        - `rasa shell -p 5006`
    2. OR Improve model through an interactive session with the following steps:
        - `rasa run actions`
        - `rasa interactive -p 5006`

    Must have actions server running when doing any interactive/shell work.
    Need to run interactive/regular shell on new port because other ports are being occupied by rasa server and action server:
    - rasa server http://0.0.0.0:5005
    - rasa action server http://0.0.0.0:5055

## Rasa Commands

Training Model:
- `rasa train nlu` : Trains only the NLU model, which is useful when you`ve made changes to your NLU data.
- `rasa train core` : Trains only the Core model. You can use this when you`ve made changes to your stories.

Running a Model:
- `rasa shell` : Allows you to interact with your assistant in the command line.
- `rasa run` : Starts a Rasa server to interact with your assistant via a REST API.
- `rasa run actions` : Runs the custom action server.
- `rasa run -m models --endpoints endpoints.yml` : Run a specific model with custom endpoints.

Data Import and Export:
- `rasa data split nlu` : Splits NLU training data into a train and test set.
- `rasa export nlu` : Exports NLU data in a structured format.
- `rasa import nlu` : Imports NLU data.

Interactive Learning:
- `rasa interactive` : Initiates an interactive learning session where you can improve your model by providing feedback.

Model Evaluation:
- `rasa test nlu` : Tests the NLU model`s performance.
- `rasa test core` : Tests the Core model`s performance.

Logging:
- You can enable logging for Rasa actions using the `--log-file` option. ie:
  - `--log-file my_rasa_logs.log`
