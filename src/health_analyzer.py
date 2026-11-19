from  visualization import plot_scatter_with_trendline
from statistics_utils import calculate_bmi

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
