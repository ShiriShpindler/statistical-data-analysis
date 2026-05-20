import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def count_mutations_per_sample(path):
    df = pd.read_csv(path, sep='\t')
    unique_count_df = (
        df.groupby("Sample name")["Mutation ID"]
        .nunique()
    )
    muta_per_sample_dict = unique_count_df.to_dict()
    return(muta_per_sample_dict)

def count_mutation_types(path):
    df = pd.read_csv(path, sep='\t')
    type_count_df = (
        df.groupby("Mutation Type")
        .size()
        .sort_values()
    )
    return(type_count_df.to_dict())

def count_mutations_per_tissue(path):
    df = pd.read_csv(path, sep='\t')
    type_count_per_site_df = (
        df.groupby(["Primary site", "Mutation Type"])
          .size()
          .reset_index(name="mutation_type_count")
    )
    temp = (
        type_count_per_site_df
        .groupby("Primary site")[["Mutation Type", "mutation_type_count"]]
        .apply(lambda x: dict(zip(x["Mutation Type"],
                                  x["mutation_type_count"])))
    )
    return(temp.to_dict())
    
def extract_above_median_samples(d):
    mutation_counts = list(d.values())
    median_val = np.median(mutation_counts)
    above_median = [sample for sample, count in d.items() if count >= median_val]
    return above_median

def count_mutations_per_tissue_2(path, sample_lst):
    df = pd.read_csv(path, sep='\t')
    df_filtered = df[df["Sample name"].isin(sample_lst)]
    type_count_per_site_df = (
        df_filtered.groupby(["Primary site", "Mutation Type"])
          .size()
          .reset_index(name="mutation_type_count")
    )
    temp = (
        type_count_per_site_df
        .groupby("Primary site")[["Mutation Type", "mutation_type_count"]]
        .apply(lambda x: dict(zip(x["Mutation Type"],
                                  x["mutation_type_count"])))
    )
    return(temp.to_dict())
    
if __name__ == '__main__':
    pass #you can change this main section however you would like