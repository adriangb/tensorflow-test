import os
import tensorflow as tf


model = tf.keras.Sequential([tf.keras.Input((1,)), tf.keras.layers.Dense(1)])
model.compile(loss="mse")
model.fit(x=[[1]], y=[1])

model.save("ram://test")

print(tf.io.gfile.listdir("ram://test")
