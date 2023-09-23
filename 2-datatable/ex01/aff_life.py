from load_csv import load
import numpy as np
import pandas
import matplotlib.pyplot as plt


def list_tostr(lst: list) -> str:
    size = len(lst)
    if size == 0:
        return ""
    elif size == 1:
        return str(lst[0])
    else:
        return f"{', '.join(lst[:-1])} and {lst[-1]}"


def plottings(countries_name: list, df: pandas.DataFrame) -> None:
    try:
        countries_data = df[countries_name]
    except KeyError as e:
        raise RuntimeError(f"Country not found: {e}") from e
    year_range = countries_data.T.keys().astype(int)
    plt.plot(year_range,
             countries_data.values,
             label=(countries_name if len(countries_name) > 1
                    else countries_name[0])
             )
    plt.xticks(np.arange(year_range[0], year_range[-1], 40))


def get_data(path: str) -> pandas.DataFrame:
    df = load(path)
    df.set_index("country", inplace=True)
    return df.transpose()


def main():
    try:
        # countries_name = ["France", "Japan", "Malaysia"]
        # countries_name = ["France"]
        countries_name = ["Malaysia"]
        filename = "../life_expectancy_years.csv"

        plt.title(f"{list_tostr(countries_name)} Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plottings(countries_name, get_data(filename))
        plt.legend(loc="lower right")
        plt.savefig("life_expectancy_years.jpg")
        exit(0)
    except Exception as e:
        print('Error:', e)
        exit(1)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
