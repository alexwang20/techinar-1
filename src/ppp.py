import pandas as pd
import math

data = pd.read_csv("C:/Users/27wanga/Documents/techinar/data/pizzas.csv")

data["Area"] = (data["Size"]/2 **2 * math.pi)
data["price per sqin"] = (data["Price"]/data["Area"])

df = pd.DataFrame(data)
sorted_df = df.sort_values(by=['price per sqin'], ascending=True)
print(sorted_df)



