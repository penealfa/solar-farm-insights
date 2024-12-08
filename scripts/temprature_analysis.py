import seaborn as sns
import matplotlib.pyplot as plt


def relative_humidity_and_temprature_analysis(data):
    variables = ["RH", "Tamb", "GHI", "DNI", "DHI"]
    corr = data[variables].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Correlation Heatmap: RH, Temperature, and Solar Radiation")
    plt.show()

 
