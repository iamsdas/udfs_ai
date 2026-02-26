@fused.udf
def udf(i: int = 0):
    import time
    import pandas as pd

    # Simulate heavy compute
    time.sleep(5)

    return pd.DataFrame({"i": [i], "result": [i * 10]})
