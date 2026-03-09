import numpy as np

def ES(losses, confidence=.95, VaR=None):
    """
    Calculate the Expected Shortfall (ES) of losses.

    :param losses: array of positively stated loss values
    :param confidence: risk level (e.g., 0.99 for 99%)
    :param VaR: dollar value or percentage specifying the VaR threshold
    :return: Expected Shortfall as the average of losses exceeding VaR
    """

    losses = np.asarray(losses)

    if VaR is None:
        threshold = np.percentile(losses, confidence * 100)
    else:
        threshold = VaR

    tail_losses = losses[losses > threshold]
    es_value = np.mean(tail_losses)

    return es_value
