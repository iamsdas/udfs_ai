@fused.udf()
# new comment here
def udf(name: str = "world"):
    import pandas as pd

    return pd.DataFrame({"hello": [name]})
