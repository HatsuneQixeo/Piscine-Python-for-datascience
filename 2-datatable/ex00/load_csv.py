import pandas


def load(path: str) -> pandas.DataFrame:
    try:
        data = pandas.read_csv(path)

        print("Loading dataset of dimensions", data.shape)
        return data
    except OSError as e:
        print(f"{e.strerror}: {e.filename}")
    except Exception as e:
        print(f"{e.__class__.__name__}:", e)
