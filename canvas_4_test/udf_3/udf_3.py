@fused.udf(cache_max_age="0s")
def udf(name: str = "world"):
    import pandas as pd

    if not name or not name.strip():
        return "empty name provided"

    return name
