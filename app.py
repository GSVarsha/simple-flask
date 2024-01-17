import time
from functools import wraps

from flask import Flask, Response

app = Flask(__name__)


def log_elapsed_time_decorator(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        total_time = time.perf_counter() - start_time
        print(f"Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds")
        return result

    return timeit_wrapper


@app.get("/")
def hello():
    return {"message": "Hello from Instana (profiling) World"}


@app.route("/dummy", methods=["POST", "GET"], endpoint="dummy")
@log_elapsed_time_decorator
def dummy():
    import numpy as np

    size = 5000
    result = np.mean(np.random.rand(size, size) * np.random.rand(size, size))
    app.logger.info(f"Dummy result: {result}")
    return Response(str(result))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080")
