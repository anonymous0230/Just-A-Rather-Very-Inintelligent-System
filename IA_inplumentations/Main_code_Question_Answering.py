from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
model_name = "deepset/roberta-base-squad2"

'''
a = input('what is your quesiton?')
'''

input_1 = 'how is tony stark'

# a) Get predictions
nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question':(input_1),
    'context':('time is 8 past 9 the day is monday the month is januari the year is 2002 my name is sebasitaan i live in the netherlands') 
}

res = nlp(QA_input)

# b) Load model & tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
from wiki_api import get_wiki_ans
thisdict = res 

score = (thisdict["score"])
answer = (thisdict["answer"])

print(score, answer)

if score > 0.9:
	print(answer) 
else: 
    try_wiki = input_1
    print(get_wiki_ans(try_wiki))