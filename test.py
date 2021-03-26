import tensorflow as tf


tf.io.gfile.makedirs("ram://test/inner")

with tf.io.gfile.GFile("ram://test/inner/file.txt", mode="w") as f:
    f.write("data")

print(tf.io.gfile.listdir("ram://test/inner"))

for root, _, filenames in tf.io.gfile.walk("ram://test"):
    for filename in filenames:
        path = root + "/" + filename
        print(f"root: {root}")
        print(f"filename: {filename}")
        print(f"path: {path}")
        assert path == "ram://test/inner/file.txt"
