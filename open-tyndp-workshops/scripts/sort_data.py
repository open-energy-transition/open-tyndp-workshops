import pandas as pd

if __name__ == "__main__":
    
    # import input data
    df = pd.read_csv(snakemake.input[0])
    
    # sort the data by the maximum import potential per corridor
    df = df.sort_values(by="MAX ENERGY YEAR [GWh]", ascending=False)

    # export filtered data
    df.to_csv(snakemake.output[0])