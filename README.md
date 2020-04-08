

This is the implementation for our paper: Time sensitivity-based popularity prediction for online promotion on Twitter (Information Sciences, 2020).  https://www.sciencedirect.com/science/article/pii/S0020025520302371

This is an extended Latent Factor Model that can predict popularity values of tweets on Twitter when they are published at various times. The data includes Twitter user profiles and tweet information (tweetID, Text, published time, userID, retweetNumber).  



# TwitterPopularity

These are the code and data for our extended Latent Factor Model (LFM), which aims to predict a series of popularity values of a post when it is published in different times on Twitter. The codes are tested under win7+python2.7.

Because the basic LFM does not perform well for our prediction, we exploit the three factors, the syntactic units, temporal information and neighborhood influence, and incorporate them into the basic LFM to predict the popularity values at a series of future time points

It is too large to upload the data in 2DataRandom. And please download the data at https://pan.baidu.com/s/1Kr5nuDaIKIibMxUoew7H5w. After downloading and unziping the data,  put the 5 files under the folder “2DataRandom”. 

# 10LFMFeatureBasic

This is the basic LFM for our prediction problem. This builds a matrix in which the rows and columns represent posts and publication times, respectively. The unknown items (popularity values) of new posts can be determined via matrix factorization techniques.

To get the predictive accuracy, just execute 10LFMFeatureBasic\zLFMFeaturePerTweet.bat. And the results (SEN, SPE and G-Mean) will be saved in computePerTweetSum.txt.

# 12LFMFeatureNei

This is the basic LFM with neighborhood influence. This takes into account the factor that posts with similar topics should have similar popularity. Here, the neighborhood refers to the semantically similar posts from the same author and the same publication time bin. And the word mover’s distance is used to measure the similarity between posts.


To get the predictive accuracy, (1) copy 2DataRandom\NeighborFeature under the folder 12LFMFeatureNei. (2) Execute 12LFMFeatureNei\zLFMFeaturePerTweet.bat. And the results (SEN, SPE and G-Mean) will be saved in computePerTweetSum.txt.


# 13LFMFeatureSyn

This is the basic LFM with the dependency-based syntactic units. Here, posts are decomposed into syntactic units (primarily noun units and verb units).

To get the predictive accuracy, (1) copy 2DataRandom\TweetTimeRtSparseCleanDepend under the folder 13LFMFeatureSyn. (2)  Execute 13LFMFeatureSyn\zLFMFeaturePerTweet.bat. And the results (SEN, SPE and G-Mean) will be saved in computePerTweetSum.txt.


# 14LFMFeatureFull

This is our extended Latent Factor Model. In this model, we exploit the three factors, the syntactic units, temporal information and neighborhood influence, and incorporate them into the basic LFM.

To get the predictive accuracy, (1) copy 2DataRandom\TweetTimeRtSparseCleanDepend under the folder 14LFMFeatureSyn. (2) copy 2DataRandom\NeighborFeature under the folder 14LFMFeatureNei. (3)  Execute 14LFMFeatureSyn\zLFMFeaturePerTweet.bat. And the results (SEN, SPE and G-Mean) will be saved in computePerTweetSum.txt.


# CNN Baseline

CNNBaselinePrediction is the baseline of CNN. To run it, please see https://github.com/dennybritz/cnn-text-classification-tf.
