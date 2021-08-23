from numpy.core.fromnumeric import shape
from tensorflow.python.keras import activations
import yaml
import os
import json
import numpy as np

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.utils import to_categorical

data = yaml.safe_load(open('nlu\\train.yml').read())

# Reading the data

inputs, outputs = [], []

for command in data['commands']:
    inputs.append(command['input'].lower())
    outputs.append('{}\{}'.format(command['entity'], command['action']))

# Create a dataset
# Choose a level of tokenization: byte-level -> static vocab, handels out-out vocabulery words


# Create input data

max_sent = max([len(x) for x in inputs])

# Create arrays one hot encoding (number of eccamples, seq length, vocab_size)
# Create arrays sparse encoding (number of eccamples, seq length)

input_data = np.zeros((len(inputs), max_sent, 256), dtype='float32')

for i, inp in enumerate(inputs):
    for k, ch in enumerate(bytes(inp.encode('utf-8'))):
        input_data[i, k, int(ch)] = 1.0

#output_data = to_categorical(output_data, len(output_data))

#print(input_data.shape)

print(input_data[0].shape)

#print(len(chars))
#print('Max input seq:', max_sent)

labels = set(outputs)

label2idx = {}
idx2label = {}

for k, label in enumerate(labels):
   label2idx[label] = k
   idx2label[k] = label

output_data = []

for output in outputs:
   output_data.append(label2idx[output])

output_data = to_categorical(output_data, len(labels))

model = Sequential()
model.add(LSTM(128))
model.add(Dense(len(labels), activation='softmax'))

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['acc'])

model.fit(input_data, output_data, epochs=256)

# classify any given text into a categorpy of our nlu framework
def classify(text): 
     #create a input arry
     x = np.zeros((1, max_sent, 256), dtype='float32')

     #fill the x arry with date from input text
     for k, ch in enumerate(bytes(text.encode('utf-8'))):
         x[0, k, int(ch)] = 1.0

     out = model.perdict(x)
     idx = out.argumax()

     print('Text: "{}" is classified as "{}"'.format(text, idx2label[idx]))


while True:
      text = input('Enter some text:')
      classify(text)