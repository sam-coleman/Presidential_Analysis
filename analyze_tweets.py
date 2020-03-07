"""
Analyze the Tweets
MP 3: Text Mining

@author: Sam Coleman
"""

from get_tweets import pull_all_tweets
from PIL import Image
from wordcloud import WordCloud
from matplotlib import pyplot as plt

def get_freq_dict(user_list):
    """
    Get dictionry of top words with words as keys and their respective frequencies as values.

    user_list: Which list of words to use(TrumpWords, BernieWords, BidenWords)

    returns: word-frequency dictionary
    """
    d_freq = dict()

    #meaningless words to not include
    ignore_words = ['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'it',
    'for', 'on', 'by', 'from', 'this', 'is', 'it', 'for', 'on', 'by', 'from',
    'this', 'is', '—', 'are', 'as', 'at', 'an', 'amp', 'if', 'has', 'was']

    for word in user_list:
        if word not in ignore_words:
            d_freq[word] = d_freq.get(word,0) + 1

    return d_freq

def get_top_n(n, dict, file_name):
    """
    Get list of top used words and write to file

    n: number of top words you want
    dict: dictionary to use
    file_name: name of file to write to (and create if needed)

    returns: top word list
    """
    d_sorted = sorted(dict.items(), key=lambda kv: kv[1], reverse=True)
    top = d_sorted[0:n]

    #put top n key and values into a list
    top_words = []
    for pair in top:
        for item in pair:
            top_words.append(item)

    #delete frequency numbers from list (just leave the actual words)
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

def create_word_cloud(dict, file_name, title):
    """
    create word cloud from frequency dictionary

    dict: dictionary to use
    file_name: name of file to save to
    title: title fo word cloud to display on image
    """
    wc = WordCloud(background_color="white",width=3000,height=3000, max_words=30,relative_scaling=0.5,normalize_plurals=False).generate_from_frequencies(dict)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.title(title)
    plt.savefig(file_name)

if __name__ == '__main__':
    TrumpWords, BernieWords, BidenWords = pull_all_tweets()
    BidenDict = get_freq_dict(BidenWords)
    TrumpDict = get_freq_dict(TrumpWords)
    BernieDict = get_freq_dict(BernieWords)
    biden_top = get_top_n(50, BidenDict, 'BidenTopWords.txt')
    trump_top = get_top_n(50, TrumpDict, 'TrumpTopWords.txt')
    bernie_top = get_top_n(50, BernieDict, 'BernieTopWords.txt')
    trump_cloud = create_word_cloud(TrumpDict, 'TrumpWordCloud1', 'Trump Top Words Visualization')
    bernie_cloud = create_word_cloud(BernieDict, 'BernieWordCloud1', 'Bernie Top Words Visualization')
    biden_cloud = create_word_cloud(BidenDict, 'BidenWordCloud1', 'Biden Top Words Visualization')
