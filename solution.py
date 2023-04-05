import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 451783978 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    std = np.std(x, ddof=1)
    return 2 * x.mean() - 2 * std * norm.ppf(alpha / 2) / np.sqrt(len(x)), 2 * x.mean() + 2 * std * norm.ppf(1 - alpha / 2) / np.sqrt(len(x))
