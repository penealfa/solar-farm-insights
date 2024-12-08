import seaborn as sns
import matplotlib.pyplot as plt


def histogram_analysis(data):
    variables = ["GHI", "DNI", "DHI", "WS", "Tamb"]
    plt.figure(figsize=(15, 10))

    for i, var in enumerate(variables, 1):
        plt.subplot(2, 3, i)
        sns.histplot(data[var], kde=True, bins=30, color="blue", edgecolor="black")
        plt.title(f"Histogram of {var}")
        plt.xlabel(var)
        plt.ylabel("Frequency")

    plt.tight_layout()
    plt.suptitle("Frequency Distribution of GHI, DNI, DHI, WS, and Tamb", y=1.02, fontsize=16)
    plt.show()

 
