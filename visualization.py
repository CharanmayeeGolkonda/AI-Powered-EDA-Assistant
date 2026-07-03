import os
import matplotlib.pyplot as plt
import seaborn as sns


def create_visualizations(df):
    """
    Generate charts and save them in the charts folder.
    """

    # Create charts folder if it doesn't exist
    os.makedirs("charts", exist_ok=True)

    # Select only numeric columns
    numeric_df = df.select_dtypes(include=["number"])

    # -----------------------------
    # Histogram
    # -----------------------------
    if not numeric_df.empty:
        numeric_df.hist(figsize=(10, 6))
        plt.tight_layout()
        plt.savefig("charts/histogram.png")
        plt.close()

    # -----------------------------
    # Correlation Heatmap
    # -----------------------------
    if len(numeric_df.columns) >= 2:
        plt.figure(figsize=(8, 6))
        sns.heatmap(numeric_df.corr(), annot=True, cmap="Blues")
        plt.tight_layout()
        plt.savefig("charts/heatmap.png")
        plt.close()

    # -----------------------------
    # Box Plot
    # -----------------------------
    if not numeric_df.empty:
        plt.figure(figsize=(10, 6))
        numeric_df.boxplot()
        plt.tight_layout()
        plt.savefig("charts/boxplot.png")
        plt.close()
        