import csv
import cPickle
import sys
from sklearn.feature_extraction.text import CountVectorizer
import pickle
from nltk import ngrams
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import WordPunctTokenizer
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures

def get_bigrams(myString):
    tokenizer = WordPunctTokenizer()
    tokens = tokenizer.tokenize(myString)
    stemmer = PorterStemmer()
    bigram_finder = BigramCollocationFinder.from_words(tokens)
    bigrams = bigram_finder.nbest(BigramAssocMeasures.chi_sq, 500)

    for bigram_tuple in bigrams:
        x = "%s %s" % bigram_tuple
        tokens.append(x)

    result = [' '.join([stemmer.stem(w).lower() for w in x.split()]) for x in tokens if x.lower() not in stopwords.words('english') and len(x) > 8]
    return result

def main():


#make all lexicons

#####################################################################

	with open('Codemix_SWN.txt','r') as file:
		SWN_dict={}
		list_SWN=file.readlines()
		for word in list_SWN:
			parts=word.split()
			SWN_dict[parts[0]]=float(parts[1])+float(parts[2])



	with open('fb_vocab_tfidf.pkl','r') as f:
		BOW_words = cPickle.load(f)


	with open('fb_word_bigram.pkl','r') as f:
		Bigram_words = cPickle.load(f)

	with open('emoji-style.txt','r') as file:
		emoji_list=[]
		emoji_listu=file.readlines()

		for emoji in emoji_listu:
			emoji_list.extend(emoji.split('\n'))


	with open('topics.pkl','rb') as f:
		Topics=cPickle.load(f)
	count_curse=0
	count_other=0




	with open('swear.txt','r') as file:
		swear_list=[]
		list_swear=file.readlines()
		for word in list_swear:
			swear_list.append(word.strip('\r\n'))
		


	with open('fb_ngram.pkl','r') as f:
		char_words = cPickle.load(f)

	with open('Big_data_Model.pkl','r') as f:
		clf_1=cPickle.load(f)

	with open('Big_data_Model_Curse.pkl','r') as f:
		clf_2=cPickle.load(f)
	with open('Big_data_Model_4class.pkl','r') as f:
		clf_3=cPickle.load(f)

#####################################################################
	cv = CountVectorizer(analyzer='char_wb', ngram_range=(2,3), min_df = 0 , max_features = None)
	while True:

		input_sentence = raw_input('Please enter your sentence ')

		if input_sentence=='exit':
			break

		print 'Analysing...'


		feature_matrix_ng=[]


			#preprocessing
		vector=[]
		chars_post=[]
		words_post=[]
		corpus=input_sentence.splitlines()
		X  = cv.fit_transform(corpus)
		chars_post_inter = cv.get_feature_names()
		for ch in chars_post_inter:
			chars_post.append(ch.lower())
		words_p=input_sentence.split()
		words_post_inter=list(set(input_sentence.split()))
		for wr in words_post_inter:
			words_post.append(wr.lower())
		text=[input_sentence.lower()]
		Bigrams_post = get_bigrams(str(text))
		#print Bigrams_post

		#BOW
		for word in BOW_words:
			if word in words_post:

				vector.append(words_post.count(word))
			else:
				vector.append(0)

		#Word Bigrams
		for word in Bigram_words:
			if word in Bigrams_post:
				vector.append(words_post.count(word))
			else:
				vector.append(0)


		#emoji
		for word in emoji_list :
			if word in words_post:
				#print word
				vector.append(1)
			else:
				vector.append(0)

		#topics
		for topic in Topics :
			intersection = [filter(lambda x: x in topic, sublist) for sublist in words_post]
			vector.append(len(intersection))




		#Charecter ngrams
		for word in char_words:
			if word in chars_post:
				
				vector.append(1)
			else:
				vector.append(0)

		

#####################################################################
		#SWN
		positive=[]
		negative=[]
		for word in words_post:
			if word in SWN_dict:

				if SWN_dict[word]>0:
					positive.append(word)
				else:
					negative.append(word)
		if len(positive)!=0:
			vector.append(len(negative)/float(len(positive)))
		else:
			vector.append(len(negative))

				


	    		
#####################################################################


		#SWEAR WORDS


		for word in swear_list :
			if word in words_post:
				#print word
				vector.append(1)
			else:
				vector.append(0)



			
		pred_1=[]
		pred_2=[]
		pred_3=[]

		feature_matrix_ng.append(vector)
		
		pred_class_1=clf_1.predict(feature_matrix_ng)
		if pred_class_1==0:
				pred_1.append('Overtly Aggressive')
		if pred_class_1==1:
				pred_1.append('Covertly Aggressive')
		if pred_class_1==2:
				pred_1.append('Non Aggressive')

		print pred_1[0]
			
		if pred_1[0]=='Covertly Aggressive' or pred_1[0]=='Overtly Aggressive':
			pred_class_2=clf_2.predict(feature_matrix_ng)
			if pred_class_2==0:
				pred_2.append('Curse/Abuse')
			else:
				pred_2.append('Not Curse/Abuse')

			print pred_2[0]
			pred_class_3=clf_3.predict(feature_matrix_ng)
			if pred_class_3==0:
				pred_3.append('Non-threatening Aggression')
			if pred_class_3==1:
				pred_3.append('Physical threat')
			if pred_class_3==2:
				pred_3.append('Sexual Aggression')
			if pred_class_3==3:
				pred_3.append('Identity threat')

			print pred_3[0]
			

		print 'type "exit" to break'

				
	

	

	
			


main()
