import os
import shutil

def clear_files():

    for root, dirs, files in os.walk('files'):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))