from scipy import stats

def calculate_bmi(df):
    """
    Beräknar BMI för varje individ i datasetet.
    """
    return df["weight"] / (df["height"] / 100) ** 2

def mean(series):
    """
    Beräknar medelvärdet för en pandas Series.
    """
    return series.mean()

def std(series):
    """
    Beräknar standardavvikelse för en pandas Series.
    """
    return series.std()

def mean_and_ci(series, confidence=0.95):
    """
    Returnerar medelvärde och konfidensintervall för medelvärdet.
    """
    mean = series.mean()
    se = stats.sem(series)

    ci = stats.t.interval(
        confidence=confidence,
        df=len(series) - 1,
        loc=mean,
        scale=se
    )

    return mean, ci[0], ci[1]