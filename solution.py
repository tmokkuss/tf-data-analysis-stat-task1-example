import pandas as pd
import numpy as np


chat_id = 861665812

def solution(x: np.array) -> float:
    n = x.size
    t = 68
    sum_x = x.sum()
    x_mean = sum_x / (n * t)
    return x_mean



