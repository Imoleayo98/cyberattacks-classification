import tensorflow as tf
import pandas as pd
import numpy as np

model = tf.keras.models.load_model('cyberattack-severity')
dataframe = pd.read_csv("cyberattack-data.csv")

dataframe = dataframe[["Name", "Typical Severity"]].dropna()
x = dataframe["Name"]

text_vectorization = tf.keras.layers.TextVectorization(output_sequence_length=13)
text_vectorization.adapt(x)


def check_severity(names=None):
    if names is None:
        names = []

    names = list(names)
    x_test = text_vectorization(names)

    prediction = model.predict(x_test)

    f = open("severity-vocab.txt", "r")
    vocab = f.read().split(",")
    f.close()

    prediction = np.argmax(prediction, axis=-1)

    result = []
    for i in range(prediction.__len__()):
        result.append({"text": names[i:i + 1][0], "severity": vocab[prediction[i:i + 1][0]]})

    return result
