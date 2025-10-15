# -*- coding: utf-8 -*-
import pypsa
import pandas as pd

if __name__ == "__main__":

    # import input data
    df = pd.read_csv(snakemake.input[0])

    # create a network
    n = pypsa.Network()
    n.add("Carrier", "H2")
    n.add("Bus", ["NO", "DE"], carrier="H2")
    p_nom = df.query("`NODE FROM` == 'NO' and `NODE TO` == 'DE'")[
        "MAX CAPACITY [MW]"
    ].values[0]
    n.add("Link", "pipeline", bus0="NO", bus1="DE", p_nom=p_nom)

    # export filtered data
    n.export_to_netcdf(snakemake.output[0])
