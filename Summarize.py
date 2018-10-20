from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem.snowball import SnowballStemmer
import nltk

# If you get an error uncomment this line and download the necessary libraries
#nltk.download()

text = """If you write a really long blog post (1000 words or more), you have a higher chance of ranking well in Google. At Yoast, we have quite a few articles containing more than 2500 words and these really help in the growth of our organic traffic.

There are a number of reasons why blog post length is important for SEO. These reasons all have to do with the fact that in lengthy texts, Google just has more clues to determine what your text is about. If you optimize your copy well, your keyword will be in the text rather often, because it’s so lengthy. No need for keyword stuffing in lengthy texts! You’ll probably have more headings, more links, and more pictures, in which the keyword will be mentioned.

Above that, you’ll probably rank for multiple long tail variants of the keyword you optimized your text for. In a lengthy text, you probably address multiple topics. Your article will have a chance to turn up in search results for all these long tail variants. Combined this will result in a growth of the organic traffic to your site."""

stemmer = SnowballStemmer("english")
stopWords = set(stopwords.words("english"))
words = word_tokenize(text)

freqTable = dict()
for word in words:
	word = word.lower()
	if word in stopWords:
		continue

	word = stemmer.stem(word)

	if word in freqTable:
		freqTable[word] += 1
	else:
		freqTable[word] = 1

sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
	for word, freq in freqTable.items():
		if word in sentence.lower():
			if sentence in sentenceValue:
				sentenceValue[sentence] += freq
			else:
				sentenceValue[sentence] = freq



sumValues = 0
for sentence in sentenceValue:
	sumValues += sentenceValue[sentence]

# Average value of a sentence from original text
average = int(sumValues / len(sentenceValue))


summary = ''
for sentence in sentences:
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
		summary += " " + sentence

print(summary)
