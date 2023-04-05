import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 451783978 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    return 2 * (x.mean() + norm.ppf(alpha / 2) * np.var(x) / np.sqrt(len(x))), 2 * (x.mean() + norm.ppf(1 - alpha / 2) * np.var(x) / np.sqrt(len(x)))
