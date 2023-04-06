import pandas as pd
import numpy as np


chat_id = 861665812

def solution(x: np.array) -> float:
    s, loc, scale = lognorm.fit(x, floc=0)
    x = np.log(s**2 / np.sqrt(scale**2 + loc**2))
    return x.mean()



