import pandas


def load(path: str) -> pandas.DataFrame:
    try:
        data = pandas.read_csv(path)

        print("Loading dataset of dimensions", data.shape)
        return data
    except OSError as e:
        raise e.__class__(f"{e.strerror}: {e.filename}")
