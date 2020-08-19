# 1.2 What is Data Science?

**Goals:** Introduce the broad concepts of data science and data structures. Prepare to look at tabular data.
    
**Outline:**
* Tables
* Indexing

## Additional Assigned Reading (or Review)
Data 8 text book "Computational and Inferential Thinking: The Foundations of Data Science" By Ani Adhikari and John DeNero [Chapter 1 Data Science](https://www.inferentialthinking.com/chapters/01/what-is-data-science.html) & [Chapter 2 Causality and Experiments](https://www.inferentialthinking.com/chapters/02/causality-and-experiments.html). This should overlap with your assigned reading for Data 8. An excerpt:

> ## What is Data Science? 
Data Science is about drawing useful conclusions from large and diverse data sets through exploration, prediction, and inference. Exploration involves identifying patterns in information. Prediction involves using information we know to make informed guesses about values we wish we knew. Inference involves quantifying our degree of certainty: will the patterns that we found in our data also appear in new observations? How accurate are our predictions? Our primary tools for exploration are visualizations and descriptive statistics, for prediction are machine learning and optimization, and for inference are statistical tests and models.

>Statistics is a central component of data science because statistics studies how to make robust conclusions based on incomplete information. Computing is a central component because programming allows us to apply analysis techniques to the large and diverse data sets that arise in real-world applications: not just numbers, but text, images, videos, and sensor readings. Data science is all of these things, but it is more than the sum of its parts because of the applications. Through understanding a particular domain, data scientists learn to ask appropriate questions about their data and correctly interpret the answers provided by our inferential and computational tools.


## Tables
Imagine you're preparing to collect some data. Say you play Yahtzee with your Grandma once a week and want to track your scores. What's the first thing you would do? Make a table! 

| Date  | My Score | G-Ma Score |
|-------|----------|------------|
| 06/06 | 150      | 230        |
| 06/13 | 165      | 166        |
| 06/20 | 136      | 198        |
| 06/27 | 195      | 260        |
| 07/04 | 168      | 154        |
| 07/11 | 138      | 520        |
| 07/18 | 220      | 320        |
| 07/25 | 196      | 175        |
| 08/01 | 127      | 188        |

A table is just a way of organizing data using columns and rows. While intuitive for a basic dataset they are also very powerful. Just by transfering the scores from scattered score cards to this table a pattern begins to emerge: your grandma is way better at Yahtzee than you! This table has three columns, we will consider each column a "variable". The first column "Date" is the independent variable, it is just when we made our observations. The second and third columns are the observations of our experiment. This counting of columns lead right to our next topic: indexing.

## Indexing

Indexing is the method for navigating around through a dataset. We use numbers to reference each row and column of a table. The python language indexes starting at 0. So in the previous section I should have written: "The zeroth column 'Date' is the independent variable, it is just when we made our observations. The first and second columns are the observations of our experiment."

|Row Index| Date  | My Score | G-Ma Score |
|-----|-------|----------|------------|
|  0  | 06/06 | 150      | 230        |
|  1  | 06/13 | 165      | 166        |
|  2  | 06/20 | 136      | 198        |
|  3  | 06/27 | 195      | 260        |
|  4  | 07/04 | 168      | 154        |
|  5  | 07/11 | 138      | 520        |
|  6  | 07/18 | 220      | 320        |
|  7  | 07/25 | 196      | 175        |
|  8  | 08/01 | 127      | 188        |

Both rows and columns are indexed, starting at zero.

| 0     | 1        |  2         |
|-------|----------|------------|
| 06/06 | 150      | 230        |
| 06/13 | 165      | 166        |
| 06/20 | 136      | 198        |
| 06/27 | 195      | 260        |
| 07/04 | 168      | 154        |
| 07/11 | 138      | 520        |
| 07/18 | 220      | 320        |
| 07/25 | 196      | 175        |
| 08/01 | 127      | 188        |

The convention is to put the row index first. So the `[4,1]` element of our table is `168` which is from row `07/04` and column `My Score`.

