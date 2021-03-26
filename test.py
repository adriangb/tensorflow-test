import os
import tensorflow as tf


model = tf.keras.Sequential([tf.keras.Input((1,)), tf.keras.layers.Dense(1)])
model.compile(loss="mse")
model.fit(x=[[1]], y=[1])

model.save("ram://test")

for root, _, filenames in tf.io.gfile.walk("ram://test"):
    for filename in filenames:
        path = root + "/" + filename
        print(f"root: {root}")
        print(f"filename: {filename}")
        print(f"path: {path}")
        print("exists: ", tf.io.gfile.exists(path))
        with tf.io.gfile.GFile(path, mode="rb") as f:
            print(f.size())
