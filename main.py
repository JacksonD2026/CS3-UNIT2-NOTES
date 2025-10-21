import numpy as np
import pandas as pd

 # Series object is a 1D array of indexed data
 # Like a COLUMN (one catagory)
month = pd.Series(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
print(month)
print(month.values)
print(month.index)

# you can set the index explicitly!!!
betterMonth = pd.Series(month, index=[1,2,3,4,5,6,7,8,9,10,11])

print(f'My birthday is in {betterMonth[7]}ust')

# Can also think of series like a simple dictionary with key:value pairs
birth_Months = {'Kevin':'Mar',
                'Jackson' : 'Aug',
                'Finny':'Jul',
                'Bryce':'Nov',
                'Natalie':'Mar',
                'Paige':'Feb',
                'Maia':'Apr'}
birth_series = pd.Series(birth_Months)
print(birth_series)


# Create a DataFrame from a single Series object
df = pd.DataFrame(birth_series, columns=['Birth Month'])
print(df) # Data frame objects have column headers

pokemon_df = pd.read_csv('pokemon_data.csv')
print(pokemon_df)
print(pokemon_df.columns)
print(pokemon_df["Speed"])
print(pokemon_df.HP)
