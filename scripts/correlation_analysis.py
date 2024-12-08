import seaborn as sns
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

def cor_solar_raditation_and_temprature(data):
    sns.pairplot(data, vars=['GHI', 'DNI', 'DHI', 'TModA', 'TModB'], kind='reg', diag_kind='kde', plot_kws={'scatter_kws': {'alpha': 0.6}})
    plt.suptitle('Pair Plot for Solar Radiations and Module Temperatures', y=1.02)
    plt.show()

def cor_solar_raditation_and_wind_coditions(data):
    scatter_matrix(data[['GHI', 'DNI', 'DHI', 'WS', 'WSgust', 'WD']], alpha=0.6, figsize=(10, 10), diagonal='kde', marker='o')
    plt.suptitle('Scatter Matrix for Solar Radiations and Module Temperatures', y=1.02)
    plt.show()