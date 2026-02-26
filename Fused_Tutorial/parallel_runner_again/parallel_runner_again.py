@fused.udf
def udf(n: int = 10):
    import time
    import pandas as pd

    # Load the slow compute UDF
    slow_udf = fused.load("slow_compute_udf")

    # Run it 10 times in parallel with udf.map()
    start = time.time()
    results = slow_udf.map(range(n)).df()
    elapsed = time.time() - start

    print(f"Ran {n} jobs (each 5s) in {elapsed:.1f}s total")
    print(f"Speedup: {n * 5 / elapsed:.1f}x")

    return results
