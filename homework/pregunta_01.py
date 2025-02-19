# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import matplotlib.pyplot as plt
import pandas as pd
import os

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """

    os.makedirs("docs", exist_ok=True)

    df=pd.read_csv("files/input/shipping-data.csv")

    copia = df.copy()


    plt.figure()
    counts=copia["Warehouse_block"].value_counts()
    counts.plot.bar(
        title='Shipping per Warehouse',
        xlabel='Warehouse block',
        ylabel='Record Count',
        color='tab:blue',
        fontsize=8,
    )

    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig("docs/shipping_per_warehouse.png")



    plt.figure()
    counts=copia["Mode_of_Shipment"].value_counts()
    counts.plot.pie(
        title='Mode of Shipment',
        wedgeprops=dict(width=0.35),
        ylabel="",
        colors=['tab:blue','tab:orange','tab:green'],
    )

    plt.savefig("docs/mode_of_shipment.png")


    plt.figure()
    copia = (copia[["Mode_of_Shipment", "Customer_rating"]]
            .groupby("Mode_of_Shipment").describe())
    copia.columns = copia.columns.droplevel()
    copia = copia[["mean","min","max"]]
    plt.barh(
        y=copia.index.values,
        width=copia["max"].values -1,
        left=copia["min"].values,
        height=0.9,
        color="lightgray",
        alpha=0.5
    )
    colors=["tab:green" if value>=3.0 else "tab:orange" for value in copia["mean"].values]
    plt.barh(
        y=copia.index.values,
        width=copia["max"].values - 1,
        left=copia["min"].values,
        height=0.5,
        color=colors,
        alpha=1.0
    )
    plt.title("Average customer rating")
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.gca().spines["left"].set_visible(False)
    plt.gca().spines["bottom"].set_visible(False)

    plt.savefig("docs/average_customer_rating.png")



    copia2 = df.copy()
    plt.figure()
    copia2.Weight_in_gms.plot.hist(
        title="Shipping weight distribution",
        color="tab:orange",
        edgecolor="white",
    )
    plt.gca().spines["top"].set_visible(False)
    plt.gca().spines["right"].set_visible(False)
    plt.savefig("docs/weight_distribution.png")

pregunta_01()