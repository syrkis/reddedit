# Paper

## Background

The self-reinforcing nature of popularity has been thoroughly documented in various realms, including that of social media posts (CITE). The phenomena is not self-evident—one could conceive of an online culture with a more philanthropic inclination in which a most became increasingly more unlikely to receive another like with every like received. In addition to not being self-evident it is also not particularly surprising that, to put in in layperson's terms, people tend to like posts that other people have already liked. It is what is explored here, focusing specifically on the social network Reddit, by upvoting randomly selected Reddit posts, and monitoring how upvote count develops.

## Experiment

The experimental setup used to test the effect was that of a randomised control trial, the treatment being upvoting a post (the control being not doing so). Everyday for seven days, a new batch of 150 posts were selected, half of which were given the treatment. All posts were monitored for a week. The code is available at github.com/syrkis/reddedit. The experiment was conducted using cron on a Linux server. On the seventh day (and seventh script call) a total of 1050 posts are monitored, which, with various API calls per post (and pausing in loops to not get banned) amounted to a two hour run time. The posts were monitored in order so as to have as close to a 24 hour period between upvote logging as possible.

Two questions were asked of the data.
1. Does the upvote distribution of for posts that received the treatment come from the same distribution as those who did not? (this was tested using non parametric bootstrapping).
2. How does the treatment effect virality? Specifically, is the probability of a posts receiving more than 1, 10, 100 and 1000 votes positively affected by the treatment.

## Results

| threshold   | 1      | 10    | 100    | 1000   |
| p-value     | 0.1236 | 4e-05 | 0.0709 | 0.0005 |
| significant | no     | yes   | no     | yes    |

A more abstract question could be does the distribution from which upvotes of treatment receiving posts come have a different mean that those of the control group. Parametric bootstrapping is used to determine this, by sampling with replacement 10,000 incarnations of both treatment and control group, and counting how often the treatment sample mean is below that of the controls. This happens in 1.13 % percent of times, thus below our significance threshold of 5 %.


## Analysis

The experiment reveals that a post is more likely to receive more than 10 and 1000 uproots when receiving the treatment, with a significance level 0.05, while falling just shy of the level when looking at the probability of receiving 1 vote and 100 votes. Had we had more samples the statistical power might have pushed those two thresholds above the relevance threshold as well.

More generally, we understand that the mean number of up votes a posts receives when receiving the treatment is from a different, higher distribution than that of the control group.

 Notably: the treatment is believed within less than a second of the post being posted. To the extent that the posts has the possibility of being seen by more posts because it has two upvotes as opposed to one. many of the avenues though which the posts could be discord might use upvote sorting, and the vast majority of posts have no other upvotes that quickly. Thus the treatment puts the post in front of the proverbial queue. 

## Conclusion

In conclusion, it seems that at the time of this experiment, a reddit post is more lively to receive more upvotes if i gets an upvote initially. As the
