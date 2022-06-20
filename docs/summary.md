# On Bias in Data Collection and its Implications

Data collection is inherently conducted from a point of view: The process that collects data cannot simultaneously be everywhere, nor are the processes from which the data emerges free from effects adverse to the phenomena of interest.
While few would disagree that it is *possible* to do a bad job in data collection,
the notion that significant errors need much less than the presence of incompetence to occur, is perhaps less intuitive.
Intuitive or not, biases are more often than not innate to the generation and processing of data.
Biases might in fact be impossible to eliminate completely.
Still, as we shall see, not every attempt at unbiased data collection is equally bad. To put it idiomatically "don't let the perfect be the enemy of the good".

When taking a step down that bias abstraction latter, we encounter several general types of biases all sharing the feature of being reliably off in particular directions (using a random number generator as an estimator for age is not biased, its just very likely wrong. Always guessing "20 years old" is equally likely to be wrong, *and* it will tend to be wrong in a particular direction). Selection bias and measurement bias are two common ways of being reliably wrong in certain directions *without* it necessarily being obvious. Biases are incorrect for reasons *external* to your model: They are ways of incorrectly relating to the impalpable greyness that is the reality.

One example of these innate limitations of data collection is that of predicting the disease severity in hospitalized patients. Largely fueled by convenience, an insurance agency, perhaps, I don't know, used expected expenditure as a proxy for measuring disease severity. This assumes that every large expenditure follows sever disease (and not luxuries like abundance of caution) or conversely that every small expenditure is so because of a lack of need as opposed to resources. This assumption is very often wrong, perhaps even more often than not. More than merely being wrong, though, this assumption is consistently wrong in a *particular* racial direction.

Even the untrained debiaser, might frown at how obviously incorrect the assumption made above are. Here the story takes a more cynical turn—removing assumptions and replacing them with commonsensical ones, does not entirely get rid of bias entirely.
The data itself, often thought to be neutral, in fact, in this case—and perhaps always—was not. It comes from a societal process, in which bias too exists.
To risk controversy: bias against blacks, could lead to tougher policing of black neighbourshoods, and in turn more black arrets, and in turn a higher offical black crime rate. This bias would be inherited by any sensible model training on that data. Thus there is a sort of maths of bias, with properties similar to transitivity. It can become contagious. Extremely hard to detect in this impalpable, ever shifting fantasia of reality.


On conclusion from these observations is the following: the debiasing of data and algorithms, is *not* an item that can be ticked of a to-do list, but rather a constant striving, similar in fact to the development process itself. Even the most well designed software system exists in a dynamic, changing environment. A system that is not meaningfully biased today, might loose this quality tomorrow, precisely due to this.
 
