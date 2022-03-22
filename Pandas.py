'''
 use the dictionary to create a data frame with the produce names as rows and columns named - "Cost Per Pound", "Quantity Sold" and "Total Sale". NOTE: Please include the questions as part of your print statements so it is easier to grade.

Using Pandas Dataframe methods, display the following information:

1. Produce that had the highest and lowest sales in total sales (both name of produce and value)
2. Using 'loc', display the quantity and total sales for 'Orange' and 'Beets' (together)
3. Using 'loc', display the total sales for 'Apples' through 'Lettuce'
4. Using 'at', update the quantity sold for Apricots to 11,955 and total sales to 44,353.05
5. What is the average quantity sold across all products? (print out ONLY quantity sold)
6. Create a new dataframe for only those produce that have sold between 11,500 to 12,000 (quantity)
7. What is the total sales for the products in the above new dataframe? (print out ONLY total sales)
'''
import pandas as pd
import numpy as np

open_file = open('produce_dictionary.py', 'r')
info = open_file.read()
print(info)