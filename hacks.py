from os import path

orig = path.join

from posixpath import join as urljoin

def join(*paths):
    root = str(paths[0])
    if root.startswith("ram://") or root.startswith("gs://"):
        return urljoin(*paths)
    return orig(*paths)

path.join = join
