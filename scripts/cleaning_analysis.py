# scripts/time_series_analysis.py
import matplotlib.pyplot as plt


def plot_cleaning(data):
    cleaned = data[data['Cleaning'] == 1]
    not_cleaned = data[data['Cleaning'] == 1]
    mean_cleaned = cleaned[['TModA', 'TModB']].mean()
    mean_not_cleaned = not_cleaned[['TModA', 'TModB']].mean()

    labels = ['TModA', 'TModB']
    x = range(len(labels))

    plt.bar(x, mean_cleaned, width=0.4, label='Cleaning = 1', align='center', color='blue')
    plt.bar(x, mean_not_cleaned, width=0.4, label='Cleaning = 0', align='edge', color='orange')

    plt.xlabel('Columns')
    plt.ylabel('Mean Values')
    plt.title('Effect of Cleaning on TModA and TModB')
    plt.xticks(x, labels)
    plt.legend()
    plt.tight_layout()
    plt.show()
 
