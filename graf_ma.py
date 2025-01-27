import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Datos
hb_control_alto = [18.8, 18.7, 18.8, 18.7, 18.7, 18.9, 19.1, 18.8, 19.1, 19.0, 19.0, 19.1, 19.0, 19.0, 18.8, 18.9, 18.9, 18.8, 18.7, 18.6, 18.9, 18.8, 18.9, 18.9, 19.7, 19.4, 18.8, 19.5, 18.9, 19.1, 18.7]
rbc_control_normal = [4.71, 4.7, 4.76, 4.69, 4.78, 4.6, 4.72, 4.73, 4.66, 4.75, 4.63, 4.75, 4.67, 4.7, 4.68, 4.68, 4.76, 4.69, 4.71, 4.73, 4.65, 4.76, 4.64, 4.73, 4.67, 4.69, 4.6, 4.77, 4.67, 4.69, 4.62]

# Función para generar gráficos de control
def plot_control_chart(data, title):
    mean = np.mean(data)
    std = np.std(data)

    # Límites de control
    ucl_2s = mean + 2 * std
    lcl_2s = mean - 2 * std
    ucl_3s = mean + 3 * std
    lcl_3s = mean - 3 * std

    # Crear DataFrame
    df = pd.DataFrame({"Value": data, "Día": range(1, len(data) + 1)})
    # Asegurarse de que los datos tengan una longitud de 30 días
    if len(data) < 30:
        data = data + [np.nan] * (30 - len(data))
    elif len(data) > 30:
        data = data[:30]
    df = pd.DataFrame({"Value": data, "Día": range(1, 31)})

    # Configurar gráfico
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x="Día", y="Value", marker="o", label="Valores")
    plt.axhline(mean, color="green", linestyle="--", label="Media")
    plt.axhline(ucl_2s, color="orange", linestyle="--", label="Límite 2SD")
    plt.axhline(lcl_2s, color="orange", linestyle="--")
    plt.axhline(ucl_3s, color="red", linestyle="--", label="Límite 3SD")
    plt.axhline(lcl_3s, color="red", linestyle="--")

    # Personalización
    plt.title(title)
    plt.xlabel("Día")
    plt.ylabel("Valor")
    plt.legend()
    plt.grid(alpha=0.5)
    plt.show()

# Graficar ambos gráficos de control
plot_control_chart(hb_control_alto, "Gráfico de Control - Hb Control Alto")
plot_control_chart(rbc_control_normal, "Gráfico de Control - RBC Control Normal")
