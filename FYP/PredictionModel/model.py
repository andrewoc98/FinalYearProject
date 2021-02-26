import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os


def create_model():
    
    NewsInput=Input(shape=[10])
    SentimentInput=Input(shape=[10])

    Sentimentmodel = layers.Dense(1000,activation='relu')(SentimentInput)
    Sentimentmodel = layers.Dense(1000,activation='relu')(Sentimentmodel)
    Sentimentmodel = layers.Dense(1000,activation='relu')(Sentimentmodel)
    Sentinmentmodel= Model(inputs=SentimentInput, outputs=Sentimentmodel)

    NewsModel = layers.Dense(1000,activation='relu')(NewsInput)
    NewsModel = layers.Dense(1000, activation='relu')(NewsModel)
    NewsModel = layers.Dense(1000, activation='relu')(NewsModel)
    NewsModel= Model(inputs=NewsInput,outputs=NewsModel)

    combined =concatenate([Sentimentmodel.output,NewsModel.output])

    finalModel= Dense(2,activation='relu')(combined)
    finalModel= Dense(1,activation='linear')(Model)

    model=Model(inputs=[Sentimentmodel.input,NewsModel.input], outputs=finalModel)
    model.compile(optimizer='adam',loss='mean_absolute_error', metrics=['accuracy'])


    return model

    