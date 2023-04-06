import pandas as pd
import numpy as np


chat_id = 861665812

def solution(x: np.array) -> float:
    # Оцениваем параметры распределения
    s, loc, scale = lognorm.fit(x, floc=0)
    # Вычисляем оценку параметра a
    x = np.log(s**2 / np.sqrt(scale**2 + loc**2))
    # Возвращаем оценку параметра a
    return x.mean()



