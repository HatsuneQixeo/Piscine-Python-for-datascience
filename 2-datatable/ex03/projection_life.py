from load_csv import load
import numpy as np
import matplotlib.pyplot as plt


def ssuftoa(string: str) -> int:
    """Convert the given human readable number in str to int."""

    multipliers = {
        'k': 10**3,
        'M': 10**6,
        'B': 10**9
    }

    m = multipliers.get(string[-1])
    if m is None:
        return int(string)
    else:
        return int(float(string[:-1]) * m)


def itossuf(n: int | float, index: int | None = None) -> str:
    """Convert the given number into a more human readable format.
    Designed as a callback function for matplotlib.ticker.FuncFormatter.

    This function is callled each time the library requests a tick to be
    formatted.

    Note:
        index is the index of the tick in the axis provided by the caller.
        For example, this is the tick array given to yticks [20M, 40M, 60M],
        when the function is called with n == 20M, index is given as 0,
        n == 40M, index = 1, and so on.
        Remained unused since the return value can be calculated.
    """

    multipliers = {
        'B': 10**9,
        'M': 10**6,
        'k': 10**3,
    }

    for suf, value in multipliers.items():
        if abs(n) >= value:
            return str(int(n / value)) + suf
    return str(n)


def main():
    try:
        YEAR = '1900'
        fn = '../income_per_person_gdppercapita_ppp_inflation_adjusted.csv'
        df_gdp = load(fn)
        df_life = load('../life_expectancy_years.csv')

        x = df_gdp[YEAR].values
        y = df_life[YEAR].values
        x = np.vectorize(ssuftoa)(x.astype(str))
        plt.scatter(x, y)
        plt.title(YEAR)
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life expectancy')
        plt.xscale('log')
        plt.xticks((300, 1000, 10000), ('300', '1k', '10k'))
        # plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(itossuf))
        plt.savefig(YEAR + '.jpg')
    except Exception as e:
        print('Error:', e)
        exit(1)
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
