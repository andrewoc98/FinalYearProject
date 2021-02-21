import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os


def create_model(input,targets):
    
    inputs=keras.Input(shape=(1000))
    model = layers.Dense(1000,activation='relu')(inputs)
    model = layers.Dense(1000,activation='relu')(model)
    model = layers.Dense(1000,activation='relu')(model)
    model = layers.Dense(1000,activation='relu')(model)
    model = layers.Dense(1000,activation='relu')(model)
    outputs = layers.Dense(1,activation='sigmoid')

    model=keras.Model(inputs=inputs, outputs=output)

    model.compile(
        loss=keras.losses.BinaryCrossentropy(from_logits = False),
        optimizer=keras.optimizer.Adam(lr=0.001),
        metrics=['accuracy']
    )

    