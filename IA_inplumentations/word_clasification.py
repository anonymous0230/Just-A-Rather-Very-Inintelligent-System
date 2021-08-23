from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline
import pyarrow.feather as feather
from transformers.utils.dummy_pt_objects import CanineForTokenClassification
import pandas as pd
import numpy as np
from day_and_time import I_time



tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")

nlp = pipeline("ner", model=model, tokenizer=tokenizer)
example = input()

ner_results = nlp(example)
some_variable_entitys = [nr['entity'] for nr in ner_results]
some_variable_indexs = [nr['index'] for nr in ner_results]
some_variable_words = [nr['word'] for nr in ner_results]
some_variable_starts = [nr['start'] for nr in ner_results]
some_variable_ends = [nr['end'] for nr in ner_results]

print(ner_results)

data = {
  "spoken_sentence": [example] * len(ner_results), 
  "entity": some_variable_entitys,
  "index": some_variable_indexs,
  "word": some_variable_words,
  "start": some_variable_starts,
  "finish": some_variable_ends,
  "time": [I_time] * len(ner_results),
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
df.to_csv('word_clasification.csv')
print(df)

'''
if __name__ == '__main__':
    main()
'''