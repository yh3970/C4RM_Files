import numpy as np

def VaR(r, confidence, principal=1):
    # This function returns the left tail value
    # confidence = certain that losses are not greater than the VaR value
    # r = an array of stock returns
    # out = positively stated value of r at the 1-confidence percentile * principal

    percentile_value = np.percentile(r, (1 - confidence) * 100)
    out = abs(percentile_value) * principal

    return out
