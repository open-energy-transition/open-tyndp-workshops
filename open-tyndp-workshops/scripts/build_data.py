# -*- coding: utf-8 -*-
import pandas as pd

if __name__ == "__main__":

    # import input data
    df = pd.read_csv(snakemake.input[0])

    # filter for import corridors for 2030 with capacity larger than 0
    df = df.query("YEAR == 2030 and `MAX CAPACITY [MW]` > 0")

    # export filtered data
    df.to_csv(snakemake.output[0])
