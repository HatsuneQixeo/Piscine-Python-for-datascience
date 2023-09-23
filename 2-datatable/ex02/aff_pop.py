from load_csv import load
import numpy as np
import matplotlib.pyplot as plt


def ssuftoa(string: str) -> int:
    """Convert the given human readable number in str to int."""

    multipliers = {
        'K': 1000,
        'M': 1000000,
        'B': 1000000000
    }

    m = multipliers.get(string[-1].upper())
    if m is None:
        return int(string)
    else:
        return int(float(string[:-1]) * m)


def itossuf(n: int, index: int) -> str:
    """Convert the given number into a more human readable format.
    Designed as a callback function for matplotlib.ticker.FuncFormatter.

    This function is callled each time the library requests a tick to be
    formatted.

    Note:
        index is the index of the tick in the axis provided by the caller.
        For example, this is the tick array given to yticks [20M, 40M, 60M],
        When the function is called with n == 20M, index is given as 0.
        Remained unused since the string can be calculated.

        Wonder what stopped me from just having a dictionary.
    """

    magnitude = 0
    while abs(n) >= 1000:
        magnitude += 1
        n /= 1000
    return str(int(n)) + ('', 'k', 'M', 'B')[magnitude]


def lstslice(lst: list, start_ele: int, end_ele: int) -> list:
    """Slice a list based on the range between start_ele to end_ele.

    Raises:
        ValueError when either start_ele or end_ele is not found.
    Note:
        The function assumes the list is sorted in ascending order.
    """

    return lst[lst.index(start_ele):lst.index(end_ele) + 1]


def get_pop_candy(filename: str, countries_name: list[str]) \
        -> tuple[list[int], np.ndarray]:
    """Extract the population data of the given countries from the given file.

    Raises:
        RuntimeError when any of the given country is not found.
    Returns:
        A tuple of year and countries_population.
    """

    df = load(filename)
    df.set_index("country", inplace=True)
    try:
        countries_data = df.transpose()[countries_name].transpose()
    except KeyError as e:
        raise RuntimeError(f"Country not found: {e}") from e
    year = countries_data.keys().astype(int).tolist()
    countries_population = countries_data.values
    return year, countries_population


def main():
    try:
        filename = "../population_total.csv"
        # countries_name = ["France", "Japan", "Malaysia"]
        # countries_color = ("tab:blue", "tab:green", "tab:orange")
        countries_name = ["Belgium", "France"]
        countries_color = ("tab:blue", "tab:green")
        year, countries_population = get_pop_candy(filename, countries_name)

        year = lstslice(year, 1800, 2050)
        countries_population = countries_population[:, :len(year)]
        countries_population = np.vectorize(ssuftoa)(countries_population)

        plt.title("Population Projections")
        for pop, name, color in \
                zip(countries_population, countries_name, countries_color):
            plt.plot(year, pop, label=name, color=color)
        plt.xlabel("Year")
        plt.xticks(year[0::40])

        plt.ylabel("Population")
        plt.yticks(range(20000000, countries_population.max() + 1, 20000000))
        plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(itossuf))

        plt.legend(loc="lower right")
        plt.savefig("population_total.jpg")
    except Exception as e:
        print('Error:', e)
        exit(1)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
