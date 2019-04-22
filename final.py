def calculate_final(perc: int, scores: list, bonus: int) -> float:
    """
    Return a lower bound score for the final exam in order 
    to get an A (85)
    perc: the weight of the final exam
    scores: the scores you have right now, 
    key is a weight, value is the score you got
    
    >>> my_scores = [(0.2, 83), (0.25, 100), (0.05, 100)]
    >>> perc = 0.5
    >>> calculate_final(perc, my_scores, 0)
    76.8
    """
    sum = 0
    for pair in scores:
        sum += pair[0] * pair[1]
    lost = 100 * (1 - perc) - sum - bonus
    return round(100 - ((15.5 - lost) / perc), 1)

if __name__ == "__main__":
    my_scores = [(0.05, 100), (0.1, 100), (0.1, 94), (0.05, 95), (0.1, 100), (0.2, 100)]
    perc = 0.4
    print(calculate_final(perc, my_scores, 0))