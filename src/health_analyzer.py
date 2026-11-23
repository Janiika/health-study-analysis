from  visualization import plot_scatter_with_trendline
from statistics_utils import calculate_bmi
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class HealthAnalyzer:
    """
    Analyserar sambandet mellan BMI och systoliskt blodtryck i datasetet.
    """

    def __init__(self, df):
        self.df = df.copy()


    def bmi_bp_correlation(self):
        """
        Beräknar Pearsons korrelation mellan BMI och systoliskt blodtryck.
        """
        bmi = calculate_bmi(self.df)
        return bmi.corr(self.df["systolic_bp"])


    def plot_bmi_vs_bp(self, ax):
        """
        Skapar ett scatterdiagram med trendlinje för BMI och systoliskt blodtryck.
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


    def bp_regression(self, predictor):
        """
        Returnerar en tränad linjär regressionsmodell som predikterar systolistk blodtryck utifrån en vald prediktor.
        Parametrar: predictor (str): Namnet på kolumnen som används som prediktor.
        """
        X = self.df[[predictor]]
        y = self.df["systolic_bp"]

        model = LinearRegression()
        model.fit(X, y)
        return model


    def predict_bp(self, predictor, values):
        """
        Använder en regressionsmodell för att predikera systoliskt blodtryck för givna värden på en predikator.
        """
        model = self.bp_regression(predictor)

        X_new = pd.DataFrame({predictor: values})

        return pd.DataFrame({
            predictor: values,
            "Predikterat blodtryck": model.predict(X_new)
        })


    def regression_summary(self, predictor):
        """
        Returnernar intercept, koefficient och R² för en regressionsmodell.
        """
        model = self.bp_regression(predictor)

        return {
            "predictor": predictor,
            "intercept": model.intercept_,
            "slope": model.coef_[0],
            "r2": model.score(
                self.df[[predictor]],
                self.df["systolic_bp"]
            )
        }


    def print_regression_summary(self, predictor):
        """
        Skriver ut en sammanfattning av en linjär regressionsmodell på ett snyggare sätt.
        """
        summary = self.regression_summary(predictor)

        print(f"""
        ---- Regression på vald prediktor ----
        Prediktor       : {summary["predictor"]}
        Intercept       : {summary["intercept"]:.2f}
        Slope           : {summary["slope"]:.3f}
        R²              : {summary["r2"]:.3f}
        """)


    def plot_regression_analysis(self, predictor):
        """
        Skapar en figur med två scatterdiagram: en för sambandet mellan den valda predikatoren och en med predikderade värden.
        """
        labels = {
            "age": "Ålder",
            "weight": "Vikt",
            "cholesterol": "Kolesterol"
        }

        predictor_label = labels.get(predictor, predictor)

        values = np.linspace(
            int(self.df[predictor].min()),
            int(self.df[predictor].max()),
            10
        )

        preds_df = self.predict_bp(predictor, values)

        fig, axes = plt.subplots(1, 2, figsize=(12, 4))

        plot_scatter_with_trendline(
            axes[0],
            x=self.df[predictor],
            y=self.df["systolic_bp"],
            title=f"{predictor_label} vs. systoliskt blodtryck",
            xlabel=predictor_label,
            ylabel="Systoliskt blodtryck (mmHg)"
        )

        axes[1].plot(
            preds_df[predictor],
            preds_df["Predikterat blodtryck"],
            marker="o"
        )
        axes[1].set(
            title="Predikterat blodtryck (linjär regression)",
            xlabel=predictor_label,
            ylabel="Systoliskt blodtryck (mmHg)"
        )
        axes[1].grid(True, alpha=0.5)

        plt.tight_layout()
        plt.show()