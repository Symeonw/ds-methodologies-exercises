import unicodedata
import re
import json

import nltk
from nltk.tokenize.toktok import ToktokTokenizer
from nltk.corpus import stopwords

import pandas as pd

from acquire import get_article_text


original = get_article_text()
print(original)



def basic_clean(article):
    article = article.lower()
    