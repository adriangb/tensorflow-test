# Silence TF noise
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf

# Create a TF specific implementation of join
# this would go in tf.io.gfile.join
from os import path
join_orig = path.join
from posixpath import join as urljoin

def join(*paths):
    root = str(paths[0])
    if root.startswith("ram://") or root.startswith("gs://"):
        return urljoin(*paths)
    return join_orig(*paths)


# define a test that uses savemodel and then walk to iterate over the saved data
def test():
    import os
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

# test with and without the hack

try:
    test()
    print("PASSED WITHOUT HACK")
except:
    print("FAILED WITHOUT HACK")


from unittest.mock import patch
with patch("os.path.join", new=join):
    # Test with the hack
    try:
        test()
        print("PASSED WITH HACK")
    except:
        print("FAILED WITH HACK")
