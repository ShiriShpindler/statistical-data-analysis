# Write your code instead of the 'pass' statements
import pandas as pd
import numpy as np
from scipy import stats

def calc_division_ml(path):
    with open(path, "r") as f:
        values = [float(line.strip()) for line in f]
        
    return len(values)/sum(values)

def calc_division_p_value(path):
    with open(path, "r") as f:
        data = np.array([float(line.strip()) for line in f if line.strip()])
    n = len(data)
    sample_mean = data.mean()

    # Parameters under H0 for Exp(lambda=1)
    mu0 = 1.0      # mean
    sigma0 = 1.0   # std
    se = sigma0/np.sqrt(n)

    # Z statistic
    z_stat = (sample_mean - mu0) / se

    # One-sided test: H1: mean < mu0
    p_value = stats.norm.cdf(z_stat)

    return p_value


if __name__ == '__main__':
    pass #you can change this main section however you would like