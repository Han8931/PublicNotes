from dataclasses import dataclass
from string import Template
import timeit

TEMPLATE = Template("$name is from $country")

def template():
    name = "Arajan"
    country = "The Netherlands"
    _ = TEMPLATE.substitute(name=name, country=country)

def perc_format():
    name = "Arajan"
    country = "The Netherlands"
    _ = "%s is from %s" % (name, country)

def f_string():
    name = "Arajan"
    country = "The Netherlands"
    _ = f"{name} is from {country}"

def main():
    print(
            "perc_format:",
            timeit.timeit(
                perc_format,
                number=10000,
                ),
            )
    print(
            "f_string:",
            timeit.timeit(
                f_string,
                number=10000,
                ),
            )

    print(
            "template:",
            timeit.timeit(
                template,
                number=10000,
                ),
            )

if __name__ == "__main__":
    main()
