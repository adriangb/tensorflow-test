import os
import tensorflow as tf


tf.io.gfile.makedirs("ram://folder")
with tf.io.gfile.GFile("ram://folder/file.txt", mode="w") as f:
    f.write("data")

for root, _, filenames in tf.io.gfile.walk("ram://folder"):
    for filename in filenames:
        print(f"filename: {filename}")
        assert tf.io.gfile.exists(root + "/" + filename))
