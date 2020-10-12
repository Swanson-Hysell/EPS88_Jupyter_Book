# 8.1 Bootstrap Resampling

If we were assuming a distribution, we could calculate a confidence interval (a standard deviation for example), but what if we don't know what the underlying distribution is. We can use the data set itself as an approximation of the population and resampling from it using a statistical technique called **the bootstrap** calculating the mean each time.

## Additional Assigned Reading

Data 8 textbook "Computational and Inferential Thinking: The Foundations of Data Science" By Ani Adhikari and John DeNero [Chapter 13 Estimation](https://www.inferentialthinking.com/chapters/13/Estimation.html). This should overlap with your assigned reading for Data 8.

## The Bootstrap: Resampling from the Sample 

> What we do have is a large random sample from the population. As we know, a large random sample is likely to resemble the population from which it is drawn. This observation allows data scientists to lift themselves up by their own bootstraps: the sampling procedure can be replicated by sampling from the sample.

> Here are the steps of the bootstrap method for generating another random sample that resembles the population:
> - Treat the original sample as if it were the population.
> - Draw from the sample, at random with replacement, the same number of times as the original sample size.

> It is important to resample the same number of times as the original sample size. The reason is that the variability of an estimate depends on the size of the sample. Since our original sample consisted of 500 employees, our sample median was based on 500 values. To see how different the sample could have been, we have to compare it to the median of other samples of size 500.

> If we drew 500 times at random without replacement from our sample of size 500, we would just get the same sample back. By drawing with replacement, we create the possibility for the new samples to be different from the original.

> Why is this a good idea? By the law of averages, the distribution of the original sample is likely to resemble the population, and the distributions of all the "resamples" are likely to resemble the original sample. So the distributions of all the resamples are likely to resemble the population as well.

> Source: https://www.inferentialthinking.com/chapters/13/2/Bootstrap.html

