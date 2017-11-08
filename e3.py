import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

Election = []
for year in range(1924,2020,4):
    header = pd.read_csv("president_general_{}.csv".format(year), nrows=1).dropna(axis=1)
    d = header.iloc[0].to_dict()
    df = pd.read_csv("president_general_{}.csv".format(year), index_col = 0, thousands = ",", skiprows = [1])
    df.rename(inplace = True, columns = d)
    df.dropna(inplace = True, axis = 1)
    df["Year"] = year
    Election.append(df.loc[:, ["Democratic", "Republican", "Total Votes Cast", "Year"]])

# Creating the new column Republican Share
Election = pd.concat(Election)
Election["Republican Share"] = Election["Republican"]/Election["Total Votes Cast"]

# Plot accomack
accomack = Election.loc["Accomack County"].sort_values(by = 'Year', ascending = True)
plot = accomack.plot(x = "Year", y = "Republican Share")
plt.ylabel("Accomack County")
plt.title("Republican Share: Accomack county")
plt.grid(True)
plot.get_figure().savefig("accomack_county.pdf")

# Plot albemarle
albemarle = Election.loc["Albemarle County"].sort_values(by = 'Year', ascending = True)
plot = albemarle.plot(x = "Year", y = "Republican Share")
plt.ylabel("Albemarle County")
plt.title("Republican Share: Albemarle County")
plt.grid(True)
plot.get_figure().savefig("albemarle_county.pdf")

# Plot alexandria
alexandria = Election.loc["Alexandria City"].sort_values(by = 'Year', ascending = True)
plot = alexandria.plot(x = "Year", y = "Republican Share")
plt.ylabel("Alexandria City")
plt.title("Republican Share: Alexandria City")
plt.grid(True)
plot.get_figure().savefig("alexandria_county.pdf")

# Plot alleghany
alleghany = Election.loc["Alleghany County"].sort_values(by = 'Year', ascending = True)
plot = alleghany.plot(x = "Year", y = "Republican Share")
plt.ylabel("Alleghany County")
plt.title("Republican Share: Alleghany County")
plt.grid(True)
plot.get_figure().savefig("alleghany_county.pdf")
