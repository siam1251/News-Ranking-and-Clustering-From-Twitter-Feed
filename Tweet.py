import re


class Tweet:
    delimiter = ' | '

    def __init__(self, str_id, retweet_count, favorite_count, created_at, text):

        self.id_str = str_id
        self.retweet_count = retweet_count
        self.favorite_count = favorite_count
        self.created_at = created_at
        exp = r'https?:\/\/.*'
        text = re.sub(exp, '', text)
        self.text = text

    def get_url(self):
        s = 'https://twitter.com/statuses/'+'status/'+self.id_str
        return s

    def __str__(self):

        s = ''
        s += self.id_str + self.delimiter
        s += self.retweet_count + self.delimiter
        s += self.favorite_count + self.delimiter
        s += self.created_at + self.delimiter
        tmp = str(self.text.encode('utf8'))
        s += tmp.replace('\n','')


        return s
