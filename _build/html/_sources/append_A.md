Appendix A: Function Catalog
=======================
**This is a (semi)comprehensive list of the built-in python functions we will use in this class.**

__Week 1__

`print()` prints to the screen the value of the variable in the parentheses or the `'text'` if in quote marks.

`dataframe.head()` prints the first 5 rows of the data table named `dataframe`.

`dataframe.describe()` prints some summary statistics of the data table named `dataframe`.

`dataframe.loc[0][column1]` refers to the element of the data table named `dataframe` in the first (zeroth) row of column `column1`.

Most basic mapping: 
```
plt.figure(figsize=(10,5))
ax = plt.axes(projection=ccrs.Mollweide())
ax.coastlines()
plt.show()
```
This defines a figure object, addes axes with a Mollweide map projection, adds coastlines, and prints the figure to the screen. Note: you will need to `import cartopy.crs as ccrs` and `import matplotlib.pyplot as plt` first for this to run.

`ax.tissot()` will add Tissot circles to a map. Do this to see the map projection created distortions.

`plt.scatter(x,y,c,s)` makes a matplotlib scatter plot of data located at (x,y) with color set by the variable `c` and markersize set with `s`.

`plt.savefig('filename')` saves the figure as _filename_.

`ax.gridlines()` or `plt.grid()` add gridlines to a figure.

__Week 2__

`np.loadtxt` is a `numpy` function to load data from a .txt (text) file format.

`pd.read_csv()` reads from a csv (comma separated values) formated file to a Pandas DataFrame.

`variablename.shape` returns the array size of a variable named _variablename_.

`np.reshape()` reshapes the variable named _variablename_ to the input size. For example 

```
a = np.array([[1,2,3], [4,5,6]])
np.reshape(a, 6)
array([1, 2, 3, 4, 5, 6])
```

`plt.hist(x,bins=n)` plots a histogram of the variable `x` with `n` number of bins. Setting `density=True` will normalize the histogram.

`np.max(x)` and `np.min(x)` returns the maximum and minimum value of the input `x`.

`np.mean` and `np.std` returns the mean and standard deviation value of the input `x`.

`len(x)` returns the length of the array `x`.

`np.random.normal()` generates random points from a normal distribution.

`sorted(x)` sorts the values of the array `x`.

`np.asarray(x)` converts the input to an array.

`np.linspace(a,b,n)` creates a number line list from `a` to `b` with `n` elements.

`np.arange(a,b,step)` creates a number line list from `a` to `b` in steps of `step`.

`np.repeat(x,n,axis=0)` repeats the array `x` `n` number of times along the `axis=0` (0 or 1) axis.
  
`np.tile(x,n)` makes an array by reapeating `x` `n` number of times.



__Week 3__

Fancier histogram:
```
fig = plt.figure(1,(6,6))
ax = fig.add_subplot()
plt.hist(x,edgecolor='black',bins=4,label='Magnitude',log=True)
plt.xlabel('Magnitude, Mw', fontsize=16)
plt.ylabel('Number of Events', fontsize=16)
plt.title('Earthquake Magnitudes', fontsize=18)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlim([5, 9])
plt.grid(True)
plt.show()
```

`plt.figure` makes a object and `add_subplot` adds subplots. `edgecolor` sets the color of the bin outline. `log=True` makes the y-axis logarithmic. `fontsize` sets the size of the fonts. 

`pd.to_datetime()` converts a string column of a dataframe with date and time data to a `datetime` object.

`plt.annotate` add annotation to a plot.

__Week 4__

`dataframe_name.drop(columns=['a','b'])` drops the columns `a` and `b` from the dataframe `dataframe_name`.

`np.isnan(x)` returns a boolean array with `True` values where `x` has `NaN` values.

Defining a function:
```
def name_of_function(input):
    """
    Function to compute something
    
    parameters
    ----------
    input variable in units
    
    output variabel in units
    """
    # write your code here
    output = 2 * input
    return output
```

__Week 5__

`a = dataframe_name['column b'].values` converts the DataFrame Series `column b` into the numpy array `a`.

`a = dataframe_name['column b'].index[dataframe_name['column b']==x]` returns the index value where it is true that `dataframe_name['column b']==x`.

`np.power(base,exponent)` numpyt function to execute $base^{exponent}$

`np.count_nonzero(x)` counts the non-zero elements of the array `x`.

`np.delete(x,del,axis=0)` deletes the indices `del` from the array `x` along the `axis=` (0 or 1) axis.

`np.unique(x)` finds the unique elements of the array `x`.

`a = dataframe_name.sort_values(by=['column b'])` sorts the rows of the dataframe `datafram_name` by the values in `column b`.

__Week 6__

`np.random.choice(a)` generates a random sample pulled from elements in the 1D array `a`.

`np.random.binomial(n,p,size=s)` Samples are drawn from a binomial distribution with specified parameters, `n` trials and `p` probability of success where `n` an integer >= 0 and `p` is in the interval [0,1]. 

`np.random.poisson(lam,size=n)` Samples are drawn from a Poisson distribution with specified parameters, `lam` average rate of event occurance.

`np.random.gamma(shape, scale=1.0, size=n)` Samples are drawn from a Gamma distribution with specified parameters, shape (sometimes designated “k”) and scale (sometimes designated “theta”), where both parameters are > 0.

`a.append(b)` Appends (adds on) the variable `b` to the end of the array `a`.

`np.sum(x)` Adds up the elements of the array `x`. 

`np.cumsum(x)` Return the cumulative sum of the elements along a given axis.

