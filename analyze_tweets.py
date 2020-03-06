"""
Analyze the Tweets
MP 3: Text Mining

@author: Sam Coleman
"""

from get_tweets import TrumpWords, BernieWords, BidenWords
from PIL import Image
from wordcloud import WordCloud
from matplotlib import pyplot as plt

def get_freq_dict(user_list, file_name):
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

    d_sorted = sorted(d_freq.items(), key=lambda kv: kv[1], reverse=True)

    #for fine tuning, delete all this later
    top = d_sorted[0:50]
    top_words = []
    for pair in top:
        for key in pair:
            top_words.append(key)

    f = open(file_name, 'w')
    f.write(str(top_words))
    f.close()
    #return top_words
    return d_freq

BidenDict = get_freq_dict(BidenWords, 'BidenDict.txt')
TrumpDict = get_freq_dict(TrumpWords, 'TrumpDict.txt')
BernieDict = get_freq_dict(BernieWords, 'BernieDict.txt')

def get_top_n(n, dict):

def create_word_clouds(dict)
wc = WordCloud(background_color="white",width=3000,height=3000, max_words=30,relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(TrumpDict)
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.title('Trump Top Words')
plt.savefig('deltePic')
