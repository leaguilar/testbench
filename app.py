import pickle as pkl
import numpy as np
import os

if __name__ == "__main__":
    print("Hello CE!")
    cwd = os.getcwd()
    print(cwd)
    arr = np.zeros((100,2))
    with open('/data/test.pkl','wb') as f:
        pkl.dump(arr, f)
