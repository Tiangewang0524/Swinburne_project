"""
Several functions:

1. Filter the data for Twitter/Instagram with hashtag and reserve 5 attributes:
"tweet_id", "user_id", "user_name", "post_text" and "post_time".

2. Sentiment analysis through nltk.vaderSentiment for Twitter/Instagram data

3. Find trollers (who always have negative comments on women)

4. Generate word cloud.

"""

import json
# from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick



key_hashtag_1 = "#metoo"
key_hashtag_2 = "#timesup"
ins_tag_1 = "metoo"
ins_tag_2 = "timesup"


# convert numbers to months
def convert(x):
    return{
        1:'Jan',
        2:'Feb',
        3:'Mar',
        4:'Apr',
        5:'May',
        6:'Jun',
        7:'Jul',
        8:'Aug',
        9:'Sep',
        10:'Oct',
        11:'Nov',
        12:'Dec'
    }.get(x)

# filter Twitter data
def twi_filtered(read_file, write_file):
    info = dict()
    write_file.write('{"rows":[\n')
    for each_row in read_file:
        try:
            # Remove the blank and comma in the end of each row.
            item = json.loads(each_row[:-2])
            # print(item)
            sub_post = item["doc"]["text"].split()
            if key_hashtag_1 in sub_post or key_hashtag_2 in sub_post:
                info["post_time"] = item["doc"]["created_at"]
                info["tweet_id"] = item["doc"]["id_str"]
                info["user_id"] = item["doc"]["user"]["id_str"]
                info["user_name"] = item["doc"]["user"]["name"]
                info["post_text"] = item["doc"]["text"]
                each = json.dumps(info)
                write_file.write(each + ',' + '\n')
                write_file.flush()
                print("User " + info["user_name"] + "'s filtered task done!")
        except:
            continue
    write_file.seek(write_file.tell() - 2)
    write_file.write(']}')


# filter Instagram data
def ins_filtered(read_file, write_file):
    list_a = []
    info = dict()
    write_file.write('{"rows":[\n')
    for each_row in read_file:
        try:
            # Remove the blank and comma in the end of each row.
            item = json.loads(each_row[:-2])
            # Removed '#' from hashtag
            if ins_tag_1 in item["doc"]["tags"] or ins_tag_2 in item["doc"]["tags"]:
                # created_time is a string of numbers which are hard to understand
                # and no document to interpret what they represent.
                # info["post_time"] = item["doc"]["created_time"]
                list_a.append(item["key"][1])
                list_a.append(convert(item["key"][2]))
                list_a.append(item["key"][3])
                info["post_time"] = list_a
                list_a = []
                info["ins_post_id"] = item["doc"]["caption"]["id"]
                info["user_id"] = item["doc"]["user"]["id"]
                info["user_name"] = item["doc"]["user"]["username"]
                info["post_text"] = item["doc"]["caption"]["text"]
                each = json.dumps(info)
                print(each)
                write_file.write(each + ',' + '\n')
                write_file.flush()
                print("User " + info["user_name"] + "'s filtered task done!")
        except:
            continue
    write_file.seek(write_file.tell() - 2)
    write_file.write(']}')


# twitter sentiment analysis
def twi_sentiment(read_file, write_file):
    month_attitude = dict()
    sid = SentimentIntensityAnalyzer()
    info = dict()
    write_file.write('{"rows":[\n')
    for each_row in read_file:
        try:
            # Remove the blank and comma in the end of each row.
            item = json.loads(each_row[:-2])
            post_time = item["post_time"].split()
            date = post_time[5] + "," + post_time[1]
            if date not in month_attitude.keys():
                month_attitude[date] = dict()
                month_attitude[date]["count"] = 0
                month_attitude[date]["pos_count"] = 0
                month_attitude[date]["neg_count"] = 0
            month_attitude[date]["count"] += 1
            sentence = item["post_text"]

            # evaluate the sentiment for each tweet and save as a new file for further analysis.
            info = dict(item)

            # 1. Positive score – Negative score > 0 => Positive sentiment.
            # 2. Positive score – Negative score < 0 => Negative sentiment.
            if sid.polarity_scores(sentence)['neg'] - sid.polarity_scores(sentence)['pos'] > 0:
                month_attitude[date]["neg_count"] += 1
                info["attitude"] = "negative"
            elif sid.polarity_scores(sentence)['neg'] - sid.polarity_scores(sentence)['pos'] < 0:
                month_attitude[date]["pos_count"] += 1
                info["attitude"] = "positive"

            each = json.dumps(info)
            write_file.write(each + ',' + '\n')
            write_file.flush()
            print("User " + info["user_name"] + "'s attitude task done!")
        except:
            continue
    write_file.seek(write_file.tell() - 2)
    write_file.write(']}')
    return month_attitude


# instagram sentiment analysis
def ins_sentiment(read_file, write_file):
    month_attitude = dict()
    sid = SentimentIntensityAnalyzer()
    info = dict()
    write_file.write('{"rows":[\n')
    for each_row in read_file:
        try:
            # Remove the blank and comma in the end of each row.
            item = json.loads(each_row[:-2])
            date = str(item["post_time"][0]) + "," + str(item["post_time"][1])
            if date not in month_attitude.keys():
                month_attitude[date] = dict()
                month_attitude[date]["count"] = 0
                month_attitude[date]["pos_count"] = 0
                month_attitude[date]["neg_count"] = 0
            month_attitude[date]["count"] += 1
            sentence = item["post_text"]

            # evaluate the sentiment for each tweet and save as a new file for further analysis.
            info = dict(item)

            # 1. Positive score – Negative score > 0 => Positive sentiment.
            # 2. Positive score – Negative score < 0 => Negative sentiment.
            if sid.polarity_scores(sentence)['neg'] - sid.polarity_scores(sentence)['pos'] > 0:
                month_attitude[date]["neg_count"] += 1
                info["attitude"] = "negative"
            elif sid.polarity_scores(sentence)['neg'] - sid.polarity_scores(sentence)['pos'] < 0:
                month_attitude[date]["pos_count"] += 1
                info["attitude"] = "positive"

            each = json.dumps(info)
            write_file.write(each + ',' + '\n')
            write_file.flush()
            print("User " + info["user_name"] + "'s attitude task done!")
        except:
            continue
    write_file.seek(write_file.tell() - 2)
    write_file.write(']}')
    return month_attitude


# draw the sentiment analysis
def draw_sentiment(attitude):
    # y axis related
    y_axis_pos = list()
    y_axis_neg = list()
    y_axis_difference = list()
    for each_data in attitude.values():
        y_axis_pos.append(int(-(each_data['pos_count'])))
        y_axis_neg.append(int(each_data['neg_count']))
        y_axis_difference.append(int(each_data['neg_count']) - int(each_data['pos_count']))

    # X axis related
    x_axis = list()
    for month in attitude.keys():
        x_axis.append(month)
    x_length = [i for i in range(len(x_axis))]

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    ax1.plot(x_length, y_axis_difference, 'or-', label='difference')
    ax1.set_title('The comparison between positive and negative comments\n', fontsize=12, color='r')
    for i, (_x, _y) in enumerate(zip(x_length, y_axis_difference)):
        plt.text(_x, _y, y_axis_difference[i], color='black', fontsize=10)

    # left legend
    ax1.legend(loc=1)
    ax1.set_ylim([-500, 1000])
    ax1.set_ylabel('difference')
    ax2 = ax1.twinx()
    plt.bar(x_length, y_axis_pos, alpha=0.3, color='blue', label='pos_count')
    plt.bar(x_length, y_axis_neg, alpha=0.3, color='red', label='neg_count')

    # right legend
    ax2.legend(loc=2)
    ax2.set_ylim([-500, 1000])
    ax2.set_ylabel('number of count')

    for i, (_x, _y) in enumerate(zip(x_length, y_axis_pos)):
        plt.text(_x, _y - 50, y_axis_pos[i], color='maroon', fontsize=8, ha='center', va='bottom')
    for i, (_x, _y) in enumerate(zip(x_length, y_axis_neg)):
        plt.text(_x, _y + 5, y_axis_neg[i], color='maroon', fontsize=8, ha='center', va='bottom')

    plt.xticks(x_length, x_axis)
    plt.show()


# find trollers
def find_troller(read_file, write_file):
    # count positive and negative comments for all users
    user_list = dict()
    nega_user = dict()
    troller_user = dict()
    write_file.write('{"Users":[\n')
    for each_row in read_file:
        try:
            # Remove the blank and comma in the end of each row.
            item = json.loads(each_row[:-2])
            user_id = item["user_id"]
            if user_id not in user_list.keys():
                user_list[user_id] = dict()
                user_list[user_id]["count"] = 0
                user_list[user_id]["pos_count"] = 0
                user_list[user_id]["neg_count"] = 0
            user_list[user_id]["count"] += 1
            if item["attitude"] == "negative":
                user_list[user_id]["neg_count"] += 1
            elif item["attitude"] == "positive":
                user_list[user_id]["pos_count"] += 1
        except:
            continue

    # for better sort, count negative comments for users and save as a dict.
    for each_user in user_list.keys():
        nega_user[each_user] = user_list[each_user]["neg_count"]

    # Select top 10 trollers who posted most negative commments on women.
    sort_user = sorted(nega_user.items(), key=lambda item:item[1], reverse=True)
    # count for 10 times
    count_a = 0
    read_file.seek(0)
    for each in sort_user:
        # each[0] is the user_id, each[1] is the number of negative comments.
        troller_user["user_id"] = each[0]
        for each_row in read_file:
            try:
                # Remove the blank and comma in the end of each row.
                item = json.loads(each_row[:-2])
                if each[0] == item["user_id"]:
                    troller_user["user_name"] = item["user_name"]
                    read_file.seek(0)
                    break
            except:
                continue
        troller_user["negative_comments"] = each[1]
        each = json.dumps(troller_user)
        write_file.write(each + ',' + '\n')
        write_file.flush()
        print("Troller " + troller_user["user_name"] + " has been found!")
        troller_user.clear()

        count_a += 1
        if count_a == 10:
            break

    write_file.seek(write_file.tell() - 2)
    write_file.write(']}')


# Collect all the tweet and instagram posts, split them and identify the part-of-speech of the words.
# Then store as a txt file.
def word_identify(read_file, write_file):
    text = list()
    for each_row in read_file:
        try:
            # Remove the blank and comma in the end of each row.
            item = json.loads(each_row[:-2])
            # Remove the identical retweets
            if item["post_text"] not in text:
                text.append(item["post_text"])
        except:
            continue
    str_text = " ".join(text)

    # split the str_text
    tokens = nltk.word_tokenize(str_text)
    # Add part-of-speech tag for each word
    tagged = nltk.pos_tag(tokens)
    text = list()
    for each in tagged:
        # each format : (word, 'tag')
        # Reserve nouns, verbs and adjectives, remove RT, @, https, SSS and URL。
        if each[1][0] == 'N' or each[1][0] == 'J' or each[1] == 'VB':
            if each[0] != '@' and each[0] != 'metoo' and each[0] != 'timesup' and each[0][0] != '/':
                if each[0] != 'RT' and each[0] != 'https' and each[0] != 'SSS':
                    text.append(each[0])
    # while 'RT' in text or 'https' in text or 'SSS' in text:
    #     text.remove('RT')
    #     text.remove('https')
    #     text.remove('SSS')
    str_text = " ".join(text)
    write_file.write(str_text)
    print("Word_identify task done!")
    return str_text


# word cloud display
def word_cloud(str_text):
    wordcloud = WordCloud(background_color="white", width=1000, height=860, margin=2).generate(str_text)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

    file_name = input("input file name:")
    wordcloud.to_file(file_name)
    print("Word_cloud task done!")
