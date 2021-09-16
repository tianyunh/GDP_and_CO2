import pandas as pd
import matplotlib

df = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv",
    usecols=[
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ],
)

df.plot.scatter(
    x="Mortality rate, infant (per 1,000 live births)",
    y="GDP per capita (constant 2010 US$)",
)
