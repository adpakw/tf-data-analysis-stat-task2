import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 451783978 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    s = np.std(significance_levels, ddof=1)
    SE = s / np.sqrt(len(x))
    return x.mean() + SE * norm.ppf(1 - alpha / 2), \
           x.mean() + SE * norm.ppf(alpha / 2)
