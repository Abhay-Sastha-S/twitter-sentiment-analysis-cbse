import pandas as pd

project_data_file_raw = open("C:/Users/MSI/Desktop/project_twitter_data updated.csv")
results_data_file = open("C:/Users/MSI/Desktop/resulting_data.csv", "w+")
project_data_file = open("C:/Users/MSI/Desktop/project_twitter_data_filtered.csv", 'r+')

#csv1 = pd.read_csv("C:/Users/MSI/Desktop/project_twitter_data updated.csv")
#print(csv1.head())
print("\n")

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use

positive_words = []
with open("C:/Users/MSI/Desktop/positive_words.txt") as pos_words_list:
    for lin in pos_words_list:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("C:/Users/MSI/Desktop/negative_words.txt") as neg_words_list:
    for lin in neg_words_list:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_pos(str_sentences):
    str_sentences = remove_punctuation(str_sentences)
    list_str_sentences = str_sentences.split()

    count = 0
    for word in list_str_sentences:
        for positiveWord in positive_words:
            if word == positiveWord:
                count += 1
    return count


def get_neg(str_sentences):
    str_sentences = remove_punctuation(str_sentences)
    list_str_sentences = str_sentences.split()

    count = 0
    for word in list_str_sentences:
        for negativeWord in negative_words:
            if word == negativeWord:
                count += 1
    return count


def remove_punctuation(str_word):
    for charPunct in punctuation_chars:
        str_word = str_word.replace(charPunct, "")
    return str_word


def write_in_data_file(resultingdatafile, pos_count=0, neg_count=0, neut_count=0, tweet_count=0):
    #project_data_file.truncate(0)
    search_in_data_file(project_data_file)
    resultingdatafile.write(
        "Tweet ID, Tweet Text, Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score, "
        "Sentiment, Created On, Location Coord")
    resultingdatafile.write("\n")

    lines_project_data_file = project_data_file.readlines()
    #print(lines_project_data_file)
    #header_dont_used = lines_project_data_file.pop(0)
    #print(header_dont_used)
    #print("\n", "Sample Data of Tweets", '\n', lines_project_data_file, "\n")

    for lines_tweet_data in lines_project_data_file:
        list_tweet_data = lines_tweet_data.strip().split(',')
        print("TWEET TEXT--", list_tweet_data[0], "\n", "-- Retweet Count", list_tweet_data[1], "-- Reply Count",
              list_tweet_data[2])
        # create a variable to store the tweet text, list_tweet_data[0] is the tweet text
        tweettext = list_tweet_data[0]
        tweetlocation = list_tweet_data[4]
        tweetcreated = list_tweet_data[5]
        tweetid = list_tweet_data[3]
        net_score = get_pos(list_tweet_data[0]) - get_neg(list_tweet_data[0])
        x = 0
        tweet_count += 1
        if net_score > 0:
            x = "positive"
            pos_count += 1
        elif net_score < 0:
            x = "negative"
            neg_count += 1
        elif net_score == 0:
            x = "neutral"
            neut_count += 1
        resultingdatafile.write(
            f"{tweetid}, {tweettext}, {list_tweet_data[1]}, {list_tweet_data[2]}, {get_pos(list_tweet_data[0])}, {get_neg(list_tweet_data[0])}, {(get_pos(list_tweet_data[0]) - get_neg(list_tweet_data[0]))}, {x}, {tweetcreated}, {tweetlocation} ")
        resultingdatafile.write("\n")

        if tweet_count > 0:
            print("\n", "total no of tweets -", tweet_count, "\n", "no of positive tweets -", pos_count, "\n",
                  "no of negative counts -", neg_count, "\n",
                  "no of neutral tweets -", neut_count, "\n")
            print("\n", "Percentage of postive tweets -", ((pos_count / tweet_count) * 100), "%", "\n",
                  "Percentage of negative tweets -", ((neg_count / tweet_count) * 100), "%", "\n",
                  "Percentage of neutral tweets -", ((neut_count / tweet_count) * 100), "%", "\n")
        elif tweet_count == 0 or tweet_count < 0:
            print("\n", "NO RESULTS FOR CHOSEN SEARCH, CHOOSE ANOTHER SEARCH TERM ", "\n")


def search_in_data_file(searchdatafile, search_word= input('enter search term --')): #search_condition = 0):
    project_data_file.truncate(0)
    searchdatafile.write(
        "Tweet Text, Number of Retweets, Number of Replies, Tweet ID, Location Coord, Created On")
    searchdatafile.write("\n")
    lines_project_data_file_search = project_data_file_raw.readlines()
    #header_dont_used_search = lines_project_data_file_search.pop(0)
    #print(header_dont_used_search)
    #print("\n", "Sample Data of Tweets", '\n', lines_project_data_file_search, "\n")
    list_tweet_data_search = []
    tweet_text_words = []
    data_line_current = []
    lines_project_data_file_search.pop(0)
    search_print_count = 0
    search_count = 0

    for lines_tweet_data_search in lines_project_data_file_search:
        search_condition = 0
        count = 0
        list_tweet_data_temp = lines_tweet_data_search.strip().split(',')
        list_tweet_data_search.append(lines_tweet_data_search.strip().split(','))
        #print(list_tweet_data_search)
        #print('\n')
        # create a variable to store the tweet text, list_tweet_data[0] is the tweet text

        data_line_current = list_tweet_data_search[count]
        #print(data_line_current)
        tweet_text = 0
        tweet_text = data_line_current[0]
        #print(tweet_text)
        tweet_text_words = tweet_text.split()
        #print("here is the one -", "\n", tweet_text_words)
        #search_condition = 0

        for tweettext_search in tweet_text_words:

            if tweettext_search == search_word:
                searchdatafile.write(
                    f"{list_tweet_data_temp[0]}, {list_tweet_data_temp[1]}, {list_tweet_data_temp[2]}, {list_tweet_data_temp[3]}, {list_tweet_data_temp[4]}, {list_tweet_data_temp[5]}")
                searchdatafile.write("\n")
                search_condition += 1
                search_print_count += 1


        if search_condition >=1 and search_count == 0:
            print("\n", "SEARCH TERM SPOTTED", "\n", "ANALYZING...","\n", "PLEASE HOLD")
            search_count += 1

        #else:
            #print("\n", "NO SEARCH TERM SPOTTED", "\n")

        list_tweet_data_search.pop(0)
    print("\n","RUN PROGRAM AGAIN IF DEEMED NECESSARY")



write_in_data_file(results_data_file)
project_data_file.close()
results_data_file.close()
project_data_file_raw.close()



