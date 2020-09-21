# 4.1 Data Wrangling and Advanced Indexing

**Goal:** Build data wrangling skills to clean and navigate datasets.

**Outline:**
* Numpy Array and DataFrame methods and functions
* Table indexing and slicing
* Boolean (logical) indexing
* Sorting
* Data cleaning and inspection

## Additional Required Reading: Functions
Data 8 textbook "Computational and Inferential Thinking: The Foundations of Data Science" By Ani Adhikari and John DeNero [Chapter 8 Functions and Tables](https://www.inferentialthinking.com/chapters/08/Functions_and_Tables.html). This should overlap with your assigned reading for Data 8.

## Numpy Arrays and DataFrames

NumPy and Pandas offer several types of data structures, the two main structures that we use are `nparray` and `DataFrame`. A `nparray` is a fast and flexible container for large datasets that allows you to perform operations on whole blocks of data at once. `nparray`s are best suited for homogenous (just one type) numerical data. `DataFrames` are designed for tabular datasets, and can handle heterogenous data (multiple types: int, float, string, etc.).


import numpy as np
import pandas as pd

### nparray

Here is an example of a `nparray` with random float data:

# Generate a random nparray called arr_data
arr_data = np.random.randn(5,3)
arr_data

The function `arrayName.shape` is useful for finding the number of rows and columns in an array.

# use .shape to determine the shape of arr_data
arr_data.shape

`arrayName.dtype` will display the data type of the data stored in the array.

# use .dtype to determine the type of arr_data
arr_data.dtype

The functions `np.zeros` and `np.ones` are similar, they create arrays full of zeros and ones respectively. The input for these functions is the shape of the array you want. This is an effective way of setting up an array of place-holders that you can then fill in with a loop or to make an array of a single value.

# Generate a nparray of zeros with np.zeros
arr0 = np.zeros((4,4))
arr0

# Generate a nparray of ones with np.ones
arr1 = np.ones((4,4))
arr1

# np.ones is handy for making a nparray of any single value
arr5 = arr1 * 5
arr5

The functions `np.arange` and `np.linspace` can be used to make monotonic number lines. They are really useful! `np.arange` makes an array of integers or floats between the starting and ending (note that the ending point is exclusive) in steps that you set as inputs. `np.linspace` will make evenly spaced float points between the starting and ending (note that the ending point is inclusive) you set.

# Generate an array of integers between 0 and 10 in steps of 1, including 0 (start) but not 11 (end)
arr2 = np.arange(0,11,1) 
arr2

# Generate an array of floats between 0 and 10 in steps of 2, including 0 (start) but not 11 (end)
arr2 = np.arange(0.0,11.0,2.0) 
arr2

# Generate an array of 14 evenly spaced numbers between 0 and 10, including 0 (start) and 10 (end).
arr3=np.linspace(0,10,14) 
arr3

### DataFrames 

`Series` and `DataFrames` are like nparrays but they have the added feature of index labels assigned to each row and column -- the bold labels in the below `DataFrame`. These labels can be used to bin and select data.

# generate a new DataFrame
# note that index values (like the column labels) don't have to integers and don't have to be in order
frame = pd.DataFrame(np.random.rand(3, 3), index=['Nevada','Montana','Arizona'], columns=['sedimentary','igneous','metamorphic'])
frame

We've seen `DataFrame` structures before in our tabular data files. The Earthquake catalog we were dealing with last week was a .csv (Comma Separated Variable) data file of all the earthquakes. We imported it as a DataFrame from the USGS API by setting up a query URL and using `pd.read_csv`. This time we'll look at the earthquakes of magnitude 2.5 and greater from the past week.

start_day = '2020-09-07'
end_day = '2020-09-14'
standard_url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=csv&orderby=magnitude'

query_url = standard_url + '&starttime=' + start_day + '&endtime=' + end_day + '&minmagnitude=2.5'
EQ_data = pd.read_csv(query_url)
EQ_data .head()

We have seen referencing individual columns (which are called `Series`) with: `DataFrame['Column_Name']`.

EQ_data['depth']

The `.values` function can be used to return the values of the `Series` as a `nparray`, so without the labled index values of the `Series`.

print(type(EQ_data['depth']))

EQ_data['depth'].values

type(EQ_data['depth'].values)

## Indexing and Slicing

Arrays and dataframes have two axes of indices, rows and columns. Remember that python indexing starts at zero, and the end bounds are generally exclusive.

![indices](./figures/indices.png)
> Source: Python for Data Analysis (2nd Edition) McKinney, W.

<br>

Using square brackes we can select subsections of tables to work with:

![slicing](./figures/array_slicing.png)
> Source: Python for Data Analysis (2nd Edition) McKinney, W.

# generate a random array
arr_data = np.random.randn(10,5)
arr_data

**slice out the first 3 rows of arr_data**

a = arr_data[:3]
a

**slice out the last 2 columns of arr_data**

b = arr_data[:,-2:]  
b

#Or this works too
b = arr_data[:,3:] 
b

Slicing a `DataFrame` is a bit different because you can reference the index labels and use `.iloc`.

**slice out the first 10 rows of EQ_data**

EQ_data.iloc[:10]

**slice out the a chunk of depths starting at index 5 and up to (but excluding) index 10**

EQ_data.iloc[5:10]['depth']

Notice that this is still a `Series` with corresponding index values. If you just want the values from that chunk and not the index labels use `.values`.

EQ_data.iloc[5:10]['depth'].values

## Boolean Indexing

We can use Boolean (i.e. logical) indexing to select values from our DataFrame where the argument we want is `True`. You'll use the logical symbols (`<`,`>`,`==`,`&`,`|`,`~`).

**Use Boolean Indexing to filter out data so that we are only looking at rows with magnitudes larger than or equal to 6.0**

EQ_data[EQ_data['mag']>=6.0]

## Sorting

DataFrames can be sorted by the values in a given column (`.sort_values`).

EQ_data.sort_values(by=['depth']).head()

You can reverse the order of sorting with `ascending=False`.

EQ_data.sort_values(by=['depth'],ascending=False).head()

## Data cleaning and inspection

`.drop()` can be used to drop whole columns from a DataFrame.

EQ_data_concise = EQ_data.drop(['magType','nst','gap','dmin','rms','net','id','updated','place','type','horizontalError','depthError','magError','magNst','status','locationSource','magSource',], axis='columns')
EQ_data_concise.head()

`.unique()` returns the unique values from the specified object.

unique_mags = EQ_data_concise['mag'].unique()
unique_mags.sort()
unique_mags

`.value_counts()` returns the count of each unique value from the specified object. This functionality can be used to find duplicate values.

EQ_data_concise['mag'].value_counts()

### Finding missing data (NaNs)

NaN stands for not a number and is used as a placeholder in data tables where no value exists. `np.isnan` returns a boolean object with True where NaNs appear in the DataFrame.

np.isnan(EQ_data['nst'])

~np.isnan(EQ_data['nst'])

You can use this boolean object to filter-out rows that contain NaNs.

EQ_data[~np.isnan(EQ_data['nst'])]

## Further Reading (Optional)

This user guide has lots of useful examples and documentation:
https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html

