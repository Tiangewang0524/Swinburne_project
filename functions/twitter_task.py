"""
Tasks for Twitter data

1. call function for attitude to women
2. call function for finding trollers
3. call function for word cloud

"""

import json
import functions as fun


if __name__ == "__main__":
    month_attitude = dict()
    str_text = str()
    # filter task
    # with open('raw_twitter_data.json') as f1:
    #     with open('filter_twidata.json', 'w+') as f2:
    #         fun.twi_filtered(f1, f2)
    #     f2.close()
    # f1.close()

    # attitude task
    # with open('filter_twidata.json') as f1:
    #     with open('twi_attitude_data.json', 'w+') as f2:
    #         month_attitude = fun.twi_sentiment(f1, f2)
    #         print(month_attitude)
    #     f2.close()
    # f1.close()

    # find trollers
    # with open('twi_attitude_data.json') as f1:
    #     with open('twi_troller_list.json', 'w+') as f2:
    #         fun.find_troller(f1, f2)
    #     f2.close()
    # f1.close()

    # word identify
    with open('filter_twidata.json') as f1:
        with open('twi_words.txt', 'w+') as f2:
            str_text = fun.word_identify(f1, f2)
        f2.close()
    f1.close()
    # word cloud
    fun.word_cloud(str_text)

