import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.python.keras.layers import Dense, Dropout
from tensorflow.python.keras.models import Sequential

dataframe = pd.read_csv('cyberattack-data.csv')

dataframe = dataframe[["Name", "Typical Severity"]].dropna()

x = dataframe["Name"]
y = dataframe["Typical Severity"]

vocab = np.unique(y)
string_lookup = tf.keras.layers.StringLookup(vocabulary=vocab, output_mode="one_hot")
y = string_lookup(y)

text_vectorization = tf.keras.layers.TextVectorization()
text_vectorization.adapt(x)
x = text_vectorization(x)

f = open('severity-vocab.txt', 'w')
f.write(",".join(string_lookup.get_vocabulary()))
f.close()

model = Sequential(
    [
        tf.keras.layers.Normalization(),
        Dense(256, input_shape=(13,), activation='relu'),
        Dense(128, activation='relu'),
        Dense(64, activation='relu'),
        Dense(32, activation='relu'),
        Dense(6, activation='softmax'),
    ]
)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x, y, batch_size=64, epochs=2000)
model.save('cyberattack-severity')
