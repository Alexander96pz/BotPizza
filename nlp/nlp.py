from rasa_nlu.training_data  import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu import config

# Loading DataSet
train_data = load_data('rasa_dataset.json')
# Config Backend using Sklearn and Spacy
trainer = Trainer(config.load("config_spacy.yaml"))
# Training Data
trainer.train(train_data)

model_directory = trainer.persist('/projects/')

import spacy
nlp = spacy.load('en')

docx = nlp(u"I am looking for an Italian Restaurant where I can eat")
for word in docx.ents:
    print("value",word.text,"entity",word.label_,"start",word.start_char,"end",word.end_char)

from rasa_nlu.model import Metadata, Interpreter
# where `model_directory points to the folder the model is persisted in
interpreter = Interpreter.load(model_directory)

interpreter.parse(u"I am looking for an Italian Restaurant where I can eat")