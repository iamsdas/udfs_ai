@fused.udf
def udf(path: str = "s3://fused-sample/demo_data/airbnb_listings_sf.parquet"):
    import pandas as pd
    df = pd.read_parquet(path)
    print(df.T)
    return df
