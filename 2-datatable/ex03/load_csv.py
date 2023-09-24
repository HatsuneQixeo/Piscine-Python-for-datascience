import pandas


def load(path: str) -> pandas.DataFrame:
    """Load data from the given csv file as a pandas DataFrame,
     prints the shape of the DataFrame,
     and returns it.

    Formats any OSError thrown as f"{e.strerror}: {e.filename}".
    Probably not this function's job in the first place,
    but who needs a function just to encapsulate read_csv() in practice anyway?
    """

    try:
        data = pandas.read_csv(path, index_col=0)

        print("Loading dataset of dimensions", data.shape)
        return data
    except OSError as e:
        raise e.__class__(f"{e.strerror}: {e.filename}")
