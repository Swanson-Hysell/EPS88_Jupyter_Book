Appendix A: Function Catalog
=======================
**This is a (semi)comprehensive list of the built-in python functions we will use in this class.**


`print()` prints to the screen the value of the variable in the parentheses or the `'text'` if in quote marks.

`pd.read_csv()` reads from a csv (comma separated values) formated file to a Pandas DataFrame.

`dataframe.head()` prints the first 5 rows of the data table named `dataframe`.

`dataframe.loc[0][column1]` refers to the element of the data table named `dataframe` in the first (zeroth) row of column `column1`.

Most basic mapping: \
`plt.figure(figsize=(10,5))` \
`ax = plt.axes(projection=ccrs.Mollweide())` \
`ax.coastlines()` \
`plt.show()` \
This defines a figure object, addes axes with a Mollweide map projection, adds coastlines, and prints the figure to the screen. Note: you will need to `import cartopy.crs as ccrs` and `import matplotlib.pyplot as plt` first for this to run.

`ax.tissot()` will add Tissot circles to a map. Do this to see the map projection created distortions.

`plt.scatter()` makes a matplotlib scatter plot.

`plt.savefig('filename')` saves the figure as _filename_.

`ax.gridlines()` or `plt.grid()` add gridlines to a figure.

`np.loadtxt` is a `numpy` function to load data from a .txt (text) file format.

`variablename.shape` returns the array size of a variable named _variablename_.