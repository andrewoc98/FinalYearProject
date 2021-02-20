import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import os


def create_model(input):
    model=layers.Dense(512, activation='relu')(input)
    model=layers.Dense(256, activation='relu')(model)
    model=layers.Dense(128, activation='relu')(model)
    model=layers.Dense(64, activation='relu')(model)
    output=layers.Dense(1, activation='sigmoid')(model)

    model=keras.Model(inputs=inputs, outputs=output)

    model.compile(
        loss=keras.losses.BinaryCrossentropy(from_logits = False),
        optimizer=keras.optimizer.Adam(lr=0.001),
        metrics=['accuracy']
    )

    