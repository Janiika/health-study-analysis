from  visualization import plot_scatter_with_trendline

class HealthAnalyzer:
    """
    Analyserar sambandet mellan BMI och systoliskt blodtryck i datasetet.
    """

    def __init__(self, df):
        self.df = df

    def calculate_bmi(self):
        """
        Beräknar BMI för varje individ i datasetet.
        """
        return self.df["weight"] / (self.df["height"] / 100) ** 2

    def bmi_bp_correlation(self):
        """
        Beräknar Pearsons korrelation mellan BMI och systoliskt blodtryck.
        """
        bmi = self.calculate_bmi()
        return bmi.corr(self.df["systolic_bp"])

    def plot_bmi_vs_bp(self, ax):
        """
        Skapar ett scatter diagram med trendlinje för BMI och systoliskt blodtryck.
        """
        bmi = self.calculate_bmi()
        plot_scatter_with_trendline(
            ax,
            x=bmi,
            y=self.df["systolic_bp"],
            title="BMI vs. blodtryck",
            xlabel="BMI",
            ylabel="Systoliskt blodtryck (mmHg)"
        )
