# Create a TF specific implementation of join
# this would go in tf.io.gfile.join
import os
join_orig = os.path.join
from posixpath import join as urljoin

def join(*paths):
    root = str(paths[0])
    if root.startswith("ram://") or root.startswith("gs://"):
        return urljoin(*paths)
    return join_orig(*paths)

os.path.join = join

import tensorflow as tf

model = tf.keras.Sequential([tf.keras.layers.InputLayer((1,)), tf.keras.layers.Dense(1)])
model.compile(loss="mse")
model.fit(x=[[1]], y=[1], verbose=0)

model.save("ram://test")

for root, _, filenames in tf.io.gfile.walk("ram://test"):
    for filename in filenames:
        path = os.path.join(root, filename)
        with tf.io.gfile.GFile(path, mode="rb") as f:
            f.size()
