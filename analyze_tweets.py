"""
Analyze the Tweets
MP 3: Text Mining

@author: Sam Coleman
"""

from get_tweets import TrumpWords, BernieWords, BidenWords
#from get_tweets import BernieWords
from PIL import Image
from wordcloud import WordCloud
from matplotlib import pyplot as plt

def get_freq_dict(user_list, del_file):
    """
    Get dictionry of top words and their respective frequencies.

    user_list: Which list of words (TrumpWords, BernieWords, BidenWords)
    """
    d_freq = dict()

    #meaningless words to not include
    ignore_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that']
    ignore_words += ['it', 'for', 'on', 'by', 'from', 'this', 'is']
    ignore_words += ['—', 'are', 'as', 'at', 'an']

    for word in user_list:
        if word not in ignore_words:
            d_freq[word] = d_freq.get(word,0) + 1

    f = open(del_file, 'w')
    f.write(str(d_freq))
    f.close()

    return d_freq

BidenDict = get_freq_dict(BidenWords, 'BidenAllDelete.txt')
TrumpDict = get_freq_dict(TrumpWords, 'TrumpAllDelete.txt')
BernieDict = get_freq_dict(BernieWords, 'BernieAllDelete.txt')

def get_top_n(n, dict, file_name):

    d_sorted = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
    top = d_sorted[0:n]
    top_words = []
    for pair in top:
        for key in pair:
            top_words.append(key)

    index = 0
    while index < len(top_words):
        if isinstance(top_words[index], int):
            del top_words[index]
        else:
            index += 1

    #Save to file
    f = open(file_name, 'w')
    f.write(str(top_words))
    f.close()
    return top_words

biden_top = get_top_n(50, BidenDict, 'BidenTopWords.txt')
trump_top = get_top_n(50, TrumpDict, 'TrumpTopWords.txt')
bernie_top = get_top_n(50, BernieDict, 'BernieTopWords.txt')

# def create_word_cloud(dict, file_name, title):
#
#     wc = WordCloud(background_color="white",width=3000,height=3000, max_words=30,relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(dict)
#     plt.imshow(wc, interpolation='bilinear')
#     plt.axis("off")
#     plt.title(title)
#     plt.savefig(file_name)
#
# trump_cloud = create_word_cloud(TrumpDict, 'TrumpWordCloud', 'Trump Top Words Visualization')
# bernie_cloud = create_word_cloud(BernieDict, 'BernieWordCloud', 'Bernie Top Words Visualization')
# biden_cloud = create_word_cloud(BidenDict, 'BidenWordCloud', 'Biden Top Words Visualization')
