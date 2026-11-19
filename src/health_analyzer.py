from  visualization import plot_scatter_with_trendline

class HealthAnalyzer:

    def __init__(self, df):
        self.df = df

    def calculate_bmi(self):
        return self.df["weight"] / (self.df["height"] / 100) ** 2

    def bmi_bp_correlation(self):
        bmi = self.calculate_bmi()
        return bmi.corr(self.df["systolic_bp"])

    def plot_bmi_vs_bp(self, ax):
        bmi = self.calculate_bmi()
        plot_scatter_with_trendline(
            ax,
            x=bmi,
            y=self.df["systolic_bp"],
            title="BMI vs. blodtryck",
            xlabel="BMI",
            ylabel="Systoliskt blodtryck (mmHg)"
        )