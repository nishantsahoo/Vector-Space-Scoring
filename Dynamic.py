'''
Author  	   - Nishant Sahoo
Python version - 3.0.0
Project Name   - Vector Space Scoring
Team Members   - Nishant Sahoo, Vaibhav Mehrotra, Srishti Goyal, Samarth Aggarwal
'''

#!python3

from __future__ import division # to obtain force division to be floating point
import math

import platform
print('Python version ', platform.python_version())

# Title of the project
print('Vector Space Scoring')

# Initializing all variables --------------------------------------------------
doc_1 = "Just keep using random words without any punctuation because because that's what we need need"
doc_2 = "Another set of words which are added here just so that I can can complete doc_2"
doc_3 = "Shinjini After doc_2 comes doc_3 what do you think we should do next after we're done done typing random words"

dict_doc = {"Doc_1": doc_1, "Doc_2": doc_2, "Doc_3": doc_3}

query = "Shinjini we do doc_2 what"
query_list = query.split(' ')

###################################################################################

doc_1_list = doc_1.split(' ')
doc_2_list = doc_2.split(' ')
doc_3_list = doc_3.split(' ')
all_words  = list(set(doc_1_list + doc_2_list + doc_3_list))

number_of_documents = 3

# Display data collection
print('List of all words -')
print(all_words)
print()
print('Query -', query)
print()

doc_1_tf   = {} # term frequency of doc_1
doc_2_tf   = {} # term frequency of doc_1
doc_3_tf   = {} # term frequency of doc_1
doc_all_df = {} # document frequency

### Dynamic code ##################################################################

documents = []
for each in dict_doc:
	documents += [str(dict_doc[each])]

print('Documents:', documents)
doc_list = []
for each in documents:
	doc_list += [each.split(' ')]

print('Doc_list variable value:', doc_list)

dynamic_all_words = [] # empty set
for doc in doc_list:
	dynamic_all_words += doc

dynamic_all_words = list(set(dynamic_all_words))
print("dynamic_all_words: ", dynamic_all_words)

dynamic_number_of_documents = len(documents)
print("dynamic_number_of_documents:", dynamic_number_of_documents)

doc_tf    = [] # term frequency of documents
doc_df    = {} # document frequency
query_tf  = {} # term frequency of query
doc_score = [] # Scores of each document

dynamic_idf = {}

# term frequency for each document
for doc in doc_list:
	t = {}
	for word in dynamic_all_words:
		t.update({word: doc.count(word)})
	doc_tf += [t]

print("doc_tf:", doc_tf)

# Term Frequency calculation for query
for each in dynamic_all_words:
	query_tf.update({each: query_list.count(each)})

for word in dynamic_all_words:
	temp_sum = 0
	for tf in doc_tf:
		temp_sum += tf[word]

	doc_df[word] = temp_sum

print("Dynamic document frequency:", doc_df)

# Calculation of Inverse Document Frequency (idf)
for word in dynamic_all_words:
	dynamic_idf[word] = math.log10((number_of_documents/doc_df[word]))

print('Dynamic Inverted Document Frequency -')
print(dynamic_idf)

# Calculation of doc_tf_idf

### End ###########################################################################

idf = {} # Inverse Document Frequency

doc_1_tf_idf = {} # tf-df of doc_1
doc_2_tf_idf = {} # tf-df of doc_2
doc_3_tf_idf = {} # tf-df of doc_3
query_tf_idf = {} # tf-df of query

# Initializing scores as 0
score_doc_1  = 0
score_doc_2  = 0
score_doc_3  = 0

# Variable initialization complete --------------------------------------------

# Term Frequency calculation for document 1
for each in all_words:
	doc_1_tf.update({each: doc_1_list.count(each)})

# Term Frequency calculation for document 2
for each in all_words:
	doc_2_tf.update({each: doc_2_list.count(each)})

# Term Frequency calculation for document 3
for each in all_words:
	doc_3_tf.update({each: doc_3_list.count(each)})

# Document Frequency Calculation
for each in all_words:
	doc_all_df[each] = (doc_1_tf[each] + doc_2_tf[each] + doc_3_tf[each])

print('Term frequency of Document 1 -')
print(doc_1_tf)
print()
print('Term frequency of Document 2 -')
print(doc_2_tf)
print()
print('Term frequency of Document 3 -')
print(doc_3_tf)
print()
print('Term frequency of Query -')
print(query_tf)
print()
print('Document Frequency -')
print(doc_all_df)

# Calculation of Inverse Document Frequency (idf)
for each in all_words:
	idf[each] = math.log10((number_of_documents/doc_all_df[each]))

print('Inverted Document Frequency -')
print(idf)

# tf-idf calculation

for each in all_words:
	doc_1_tf_idf[each] = idf[each]*doc_1_tf[each]
	doc_2_tf_idf[each] = idf[each]*doc_2_tf[each]
	doc_3_tf_idf[each] = idf[each]*doc_3_tf[each]
	query_tf_idf[each] = idf[each]*query_tf[each]

print()
print('tf-idf value of Document 1 -')
print(doc_1_tf_idf)
print()
print('tf-idf value of Document 2 -')
print(doc_2_tf_idf)
print()
print('tf-idf value of Document 3 -')
print(doc_3_tf_idf)
print()
print('tf-idf value of Query -')
print(query_tf_idf)
print()

# Calculation of partial scores of documents for the given query
for each in doc_1_tf_idf.keys():
	score_doc_1 += doc_1_tf_idf[each]*query_tf_idf[each]

for each in doc_2_tf_idf.keys():
	score_doc_2 += doc_2_tf_idf[each]*query_tf_idf[each]

for each in doc_3_tf_idf.keys():
	score_doc_3 += doc_3_tf_idf[each]*query_tf_idf[each]

# Calculation of euclidean_length
def euclidean_length(vector):
	t_sum = length = 0
	for each in vector.values():
		t_sum += each**2

	length = math.sqrt(t_sum)
	return length

# Calculation of scores of documents for the given query
score_doc_1 /= (euclidean_length(doc_1_tf_idf)*euclidean_length(query_tf_idf))
score_doc_2 /= (euclidean_length(doc_2_tf_idf)*euclidean_length(query_tf_idf))
score_doc_3 /= (euclidean_length(doc_3_tf_idf)*euclidean_length(query_tf_idf))

sorted_list_score = [("Doc_1", score_doc_1), ("Doc_2", score_doc_2), ("Doc_3", score_doc_3)]

# Custom function for sorting (Sorts according to the score)
def score_cmp(list_item):
    return list_item[1]

# Sorting the document scores in descending order
sorted_list_score.sort(key=score_cmp, reverse=True)

print('Rank of the documents -')
for each in sorted_list_score:
	print(each[0], 'score -' , each[1])
