# Swinburne_project

This project is to understand community attitudes towards violence against women in Australia.

Data are from the Twitter and Instagram.

## 0. Requisite package:
matplotlib

vaderSentiment

json

wordcloud

nltk

* If you are doing this for first time you need to use nltk.download('punkt') for word_tokenize to work and nltk.download('averaged_perceptron_tagger') for pos_tag to work. 

* Part-of-speech tags list:

   https://www.ling.upenn.edu/courses/Fall_2003/ling001/penn_treebank_pos.html


## 1.Functions
* convert:

To convert numbers to months.

* filtered:

Clean and filter Twitter/Instagram raw data with hashtag #metoo & #timesup and reserve 5 attributes:
"tweet_id", "user_id", "user_name", "post_text" and "post_time"

* sentiment:

Sentiment analysis on Twitter/Instagram filtered data based on vaderSentiment package.
To evaluate the attitude (positive or negative) of each Twitter/Instagram post.

* find_trollers 

Find trollers (who always have negative comments on women).

* word_identify

Collect all the tweet and instagram posts, split them and identify the part-of-speech of the words. 
Then store as a txt file.

* word_cloud

Generate word cloud for Twitter/Instagram filtered data. 

