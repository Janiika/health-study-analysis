from  visualization import plot_scatter_with_trendline
from statistics_utils import calculate_bmi
from sklearn.linear_model import LinearRegression
import pandas as pd

class HealthAnalyzer:
    """
    Analyserar sambandet mellan BMI och systoliskt blodtryck i datasetet.
    """

    def __init__(self, df):
        self.df = df

    def bmi_bp_correlation(self):
        """
        Beräknar Pearsons korrelation mellan BMI och systoliskt blodtryck.
        """
        bmi = calculate_bmi(self.df)
        return bmi.corr(self.df["systolic_bp"])

    def plot_bmi_vs_bp(self, ax):
        """
        Skapar ett scatter diagram med trendlinje för BMI och systoliskt blodtryck.
        """
        bmi = calculate_bmi(self.df)
        plot_scatter_with_trendline(
            ax,
            x=bmi,
            y=self.df["systolic_bp"],
            title="BMI vs. blodtryck",
            xlabel="BMI",
            ylabel="Systoliskt blodtryck (mmHg)"
        )

    def age_bp_regression(self):
        X = self.df[["age"]]
        y = self.df["systolic_bp"]

        model = LinearRegression()
        model.fit(X, y)
        return model

    def predict_bp(self, ages):
        model = self.age_bp_regression()

        X_new = pd.DataFrame({"age": ages})

        return pd.DataFrame({
            "Ålder": ages,
            "Predikterat blodtryck": model.predict(X_new)
        })