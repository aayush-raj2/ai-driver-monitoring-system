import numpy as np

def mouth_aspect_ratio(mouth):
    A = np.linalg.norm(mouth[2] - mouth[6])
    B = np.linalg.norm(mouth[3] - mouth[5])
    C = np.linalg.norm(mouth[0] - mouth[4])
    return (A + B) / (2.0 * C)
