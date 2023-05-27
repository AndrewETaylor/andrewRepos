import pandas as pd
import matplotlib.pyplot as plt
# This is the location of the penguin data file on the internet.
PENGUINS_URL ='https://gist.githubusercontent.com/anibali/c2abc8cab4a2f7b0a6518d11a67c693c/raw/3b1bb5264736bb762584104c9e7a828bef0f6ec8/penguins.csv'
# Download the penguin data and turn it into a Pandas DataFrame object.
df = pd.read_csv(PENGUINS_URL)
# Display the first few rows of the DataFrame object.
print(df.head())


gentoo_data = df[(df['species'] == "Gentoo")]

gentoo_male_data = gentoo_data[(gentoo_data["sex"]) == "MALE"]
gentoo_female_data = gentoo_data[(gentoo_data["sex"]) == "FEMALE"]

gentoo_male_bill_depth = gentoo_male_data["bill_depth_mm"].values
gentoo_male_flipper_length = gentoo_male_data["flipper_length_mm"].values
plt.scatter(gentoo_male_bill_depth, gentoo_male_flipper_length,color = '#88c999',label="MALE")

gentoo_female_bill_depth = gentoo_female_data["bill_depth_mm"].values
gentoo_female_flipper_length = gentoo_female_data["flipper_length_mm"].values
plt.scatter(gentoo_female_bill_depth, gentoo_female_flipper_length,label='FEMALE')


plt.title('Gentoo Penguin Characterstics by Sex')
plt.xlabel("Bill Depth(mm)")
plt.ylabel("Flipper Length(mm)")
plt.legend(loc="upper left")
plt.show()