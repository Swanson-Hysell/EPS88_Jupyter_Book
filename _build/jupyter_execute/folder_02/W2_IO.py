# 2.1 Data I/O (Input/Output)

## Open the data file and have a look

Use the text editor of your choice and open the text file. Make sure it's the file you want. 

Take note of: 
-  number of header rows
-  number of columns and rows
-  are they string/integer/float types
-  what is the delimiter

Usually this will be straight foward. For example:

<img src="figures/csv_example.png" width="600">

Or slightly more complicated, but still do-able:

<img src="figures/more_complicated_example.png" width="700">

Sometimes you'll mess up and get something crazy.

<img src="figures/AHHH_example.png" width="700">


It's much better to catch this early than to struggle trying to troubleshoot.

<img src="figures/meme_AHHH_example.png" width="700">

## Data Input

The functions we will use most for reading data in text format are `np.loadtxt`,`pd.read_csv`, and `pd.read_table`. They are similar except `pd.read_csv` has a default comma delimiter and `pd.read_table` has tab (`'\t'`) as its default delimiter.

The syntax will look something like: `pd.read_csv('filename.csv',header=2, sep=',',names=['Date','Time','Location'])`

<img src="figures/Table_6_2.png" width="700">

> Source: Python for Data Analysis, McKinney

## Writing Data to Text Format



