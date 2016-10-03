
# author sayem.siam
# date: October 3, 2016
# This class is responsible to create features from
# each tweet object
# I basically used Bag of Words (BoW-tf-idf) technique to create a feature
# I used only noun and verbs from the sentence and also gave up the stock words
# If two words has a matching score greater than .6 (thresh = .6), I inserted only
# one of the two

import nltk.corpus
import nltk.tokenize.punkt
import nltk.stem.snowball
from nltk.corpus import wordnet
import string
from Tweet import Tweet

class TextFeatures:
    thresh = .6

    stopwords = nltk.corpus.stopwords.words('english')
    stopwords.extend(string.punctuation)
    stopwords.append('')
    lemmatizer = nltk.stem.wordnet.WordNetLemmatizer()

    def __init__(self, all_tweets):
        self.__all_tweets = all_tweets

    # this method create features from all the tweet texts and return as
    # a 2 dimensional array
    def get_features(self):
        self.create_dictionary()
        all_status_features = []
        feature_length = len(self.feature_dict)

        for each_status_text in self.all_filtered_words:
            single_status_features = [0]*feature_length
            for w in each_status_text:
                index = self.feature_dict[self.all_words_dict[w]]
                single_status_features[index] += 1
            all_status_features.append(single_status_features)
        return all_status_features

    # I initially used this method; but currently not using
    # this method doesn't care about similarity score between two words
    def create_dictionary_unique_words(self):

        self.all_words_dict = {}
        self.feature_dict = {}
        self.all_filtered_words = []
        index = 0
        w_count = 0
        for t in self.__all_tweets:
            words = self.get_filtered_words(t.text)
            self.all_filtered_words.append(words)
            w_count += len(words)
            for w in words:
                # check if it's a completely new words, doesn't match
                # with previous ones
                if w not in self.feature_dict:
                        # enter new words in the feature dictionary
                        self.feature_dict[w] = index
                        index +=1
                        self.all_words_dict[w] = w
        print(self.feature_dict.keys())

    # this method create a dictionary for feature space and also manage mapping
    # between two similar words
    def create_dictionary(self):

        self.all_words_dict = {}
        self.feature_dict = {}
        self.all_filtered_words = []
        index = 0
        w_count = 0
        for t in self.__all_tweets:
            words = self.get_filtered_words(t.text)
            self.all_filtered_words.append(words)
            w_count += len(words)
            for w in words:
                # check if it's a completely new words, doesn't match
                # with previous ones
                if w not in self.feature_dict:
                    match = False
                    for feature_word in self.feature_dict.keys():
                        s = self.get_similarity(feature_word, w)
                        if s > self.thresh:
                            match = True
                            # do not add new words in feature dictionary
                            # i.e., these are basically same words
                            self.all_words_dict[w] = self.all_words_dict[feature_word]
                    if not match:
                        # enter new words in the feature dictionary
                        self.feature_dict[w] = index
                        index +=1
                        self.all_words_dict[w] = w
        # print(index)
        # print(len(self.feature_dict))
        # print(len(self.all_words_dict))
        # print(self.feature_dict.keys())
        print(self.feature_dict.keys())
        # print(self.all_words_dict.keys())


    # this method returns the pars of speech of a word
    def get_wordnet_pos(self, pos_tag):
        if pos_tag[1].startswith('J'):
            return (pos_tag[0], wordnet.ADJ)
        elif pos_tag[1].startswith('V'):
            return (pos_tag[0], wordnet.VERB)
        elif pos_tag[1].startswith('N'):
            return (pos_tag[0], wordnet.NOUN)
        elif pos_tag[1].startswith('R'):
            return (pos_tag[0], wordnet.ADV)
        else:
            return (pos_tag[0], wordnet.NOUN)

    # filter the words in a sentence
    # it discard the stock words
    # it only returns the words which are either noun or verb
    def get_filtered_words(self,a):
        pos_a = map(self.get_wordnet_pos, nltk.pos_tag(nltk.tokenize.word_tokenize(a)))
        lemmae_a = []
        for token, pos in pos_a:
            # did not used it
            if ((pos == wordnet.NOUN or pos == wordnet.VERB)and token.lower().strip(string.punctuation) not in self.stopwords):
                lemmae_a.append(self.lemmatizer.lemmatize(token.lower().strip(string.punctuation), pos))
        return lemmae_a

    # returns the similarity score between two words
    def get_similarity(self,a,b):
        s1 = wordnet.synsets(a)
        s2 = wordnet.synsets(b)
        score = 0
        if len(s1) >= 1 and len(s2) >= 1:
            score = wordnet.wup_similarity(s1[0], s2[0])
        return score


# for testing purpose

if __name__ == '__main__':
    print('dfsds')
    lst = []
    t = Tweet('','','','','','The new range data huge dhaka common https:go.com')
    lst.append(t)
    t = Tweet('', '', '', '','', 'The new range')
    lst.append(t)
    t = Tweet('', '', '', '', '', 'The highly valueable money range')
    lst.append(t)
    txtfeatures = TextFeatures(lst)
    txtfeatures.get_features()
    print(txtfeatures.feature_dict.keys())
    print(len(txtfeatures.all_filtered_words))


