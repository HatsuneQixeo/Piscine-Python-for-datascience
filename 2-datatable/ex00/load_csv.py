import pandas


def load(path: str) -> pandas.DataFrame | None:
    """Load data from the given csv file as a pandas DataFrame,
     prints the shape of the DataFrame,
     and returns it.

    Returns:
        A pandas DataFrame containing the data from the given csv file.
        None if pandas.read_csv() throws an exception.
    """

    try:
        data = pandas.read_csv(path, index_col=0)

        print("Loading dataset of dimensions", data.shape)
        return data
    except OSError as e:
        print(f"{e.strerror}: {e.filename}")
    except Exception as e:
        print(f"{e.__class__.__name__}:", e)
