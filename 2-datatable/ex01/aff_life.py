from load_csv import load
import numpy as np
import pandas
import matplotlib.pyplot as plt


def list_tostr(lst: list[str]) -> str:
    """Join the list of strings into a single string delimited by comma,
    with the last element delimited by "and".
    """

    size = len(lst)
    if size == 0:
        return ""
    elif size == 1:
        return str(lst[0])
    else:
        return f"{', '.join(lst[:-1])} and {lst[-1]}"


def plotting(countries_name: list[str], df: pandas.DataFrame) -> None:
    """Plot the given countries' data from the given dataframe.

    Raises:
        RuntimeError when any of the given country is not found.

    Note:
        Does not do anything if countries_name is an empty list.
    """

    if len(countries_name) > 1:
        label = countries_name
    elif len(countries_name) == 1:
        label = countries_name[0]
    else:
        return
    try:
        countries_data = df.transpose()[countries_name]
    except KeyError as e:
        raise RuntimeError(f"Country not found: {e}") from e
    year_range = countries_data.transpose().keys().astype(int)
    plt.plot(year_range, countries_data.values, label=label)
    plt.xticks(np.arange(year_range[0], year_range[-1], 40))


def main():
    try:
        # countries_name = ["France", "Japan", "Malaysia"]
        # countries_name = ["France"]
        countries_name = ["Malaysia"]
        filename = "../life_expectancy_years.csv"
        df = load(filename)

        plt.title(f"{list_tostr(countries_name)} Life expectancy Projections")

        plotting(countries_name, df)

        plt.xlabel("Year")

        plt.ylabel("Life expectancy")

        plt.legend(loc="lower right")
        plt.savefig("life_expectancy_years.jpg")
    except Exception as e:
        print('Error:', e)
        exit(1)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
