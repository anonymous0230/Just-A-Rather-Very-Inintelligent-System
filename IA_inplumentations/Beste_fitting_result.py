'''
from transformers import AutoTokenizer, AutoModel
import torch


#Mean Pooling - Take attention mask into account for correct averaging
def mean_pooling(model_output, attention_mask):
    token_embeddings = model_output[0] #First element of model_output contains all token embeddings
    input_mask_expanded = attention_mask.unsqueeze(-1).expand(token_embeddings.size()).float()
    return torch.sum(token_embeddings * input_mask_expanded, 1) / torch.clamp(input_mask_expanded.sum(1), min=1e-9)


# Sentences we want sentence embeddings for
sentences = ['This is an example sentence', 'Each sentence is converted']

# Load model from HuggingFace Hub
tokenizer = AutoTokenizer.from_pretrained('sentence-transformers/paraphrase-xlm-r-multilingual-v1')
model = AutoModel.from_pretrained('sentence-transformers/paraphrase-xlm-r-multilingual-v1')

# Tokenize sentences
encoded_input = tokenizer(sentences, padding=True, truncation=True, return_tensors='pt')

# Compute token embeddings
with torch.no_grad():
    model_output = model(**encoded_input)

# Perform pooling. In this case, max pooling.
sentence_embeddings = mean_pooling(model_output, encoded_input['attention_mask'])

print("Sentence embeddings:")
print(sentence_embeddings)'''

import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/paraphrase-xlm-r-multilingual-v1"
headers = {"Authorization": "Bearer api_JNsBrCzatvkZCWcEvfNlUckdOzxEvzRlyl"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

output = query({
    "inputs": {
		"source_sentence": "That is a happy person",
		"sentences": [
			"That is a happy dog",
			"That is a very happy person",
			"Today is a sunny day"
		]
	},
})


print(output)