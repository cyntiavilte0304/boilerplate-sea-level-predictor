import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    # Cargamos el archivo con los datos históricos del nivel del mar.
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    # Dibujamos los puntos reales de Año vs Nivel del mar.
    plt.scatter(df["Year"], df["CSIRO Adjusted Sea Level"])

    # Create first line of best fit
    # Usamos regresión lineal con todos los datos para predecir hasta 2050.
    result_full = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    x_pred_full = range(1880, 2051)
    y_pred_full = result_full.slope * pd.Series(x_pred_full) + result_full.intercept
    plt.plot(x_pred_full, y_pred_full, 'r')

    # Create second line of best fit
    # Segunda regresión usando solo datos desde el año 2000.
    df_2000 = df[df["Year"] >= 2000]
    result_2000 = linregress(df_2000["Year"], df_2000["CSIRO Adjusted Sea Level"])
    x_pred_2000 = range(2000, 2051)
    y_pred_2000 = result_2000.slope * pd.Series(x_pred_2000) + result_2000.intercept
    plt.plot(x_pred_2000, y_pred_2000, 'green')

    # Add labels and title
    # Agregamos nombre a los ejes y título del gráfico.
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
