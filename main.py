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

# Initializing all vaariables
doc_1 = "Just keep using random words without any punctuation because because that's what we need need"
doc_2 = "Another set of words which are added here just so that I can can complete doc_2"
doc_3 = "After doc_2 comes doc_3 what do you think we should do next after we're done done typing random words"

query ="set just"

doc_1_list = doc_1.split(' ')
doc_2_list = doc_2.split(' ')
doc_3_list = doc_3.split(' ')
query_list = query.split(' ')

all_words = list(set(doc_1_list + doc_2_list + doc_3_list))
number_of_documents = 3

doc_1_tf   = {} # term frequency of doc_1
doc_2_tf   = {} # term frequency of doc_1
doc_3_tf   = {} # term frequency of doc_1
query_tf   = {} # term frequency of query
doc_all_df = {} # document frequency

idf = {} # Inverse Document Frequency

doc_1_tf_idf = {} # tf-df of doc_1
doc_2_tf_idf = {} # tf-df of doc_2
doc_3_tf_idf = {} # tf-df of doc_3
query_tf_idf = {} # tf-df of query

# Variable initialization complete

# Display data collection
print('List of all words -')
print(all_words)
print()
print('Query -', query)
print()

# Initializing all tf lists to be empty
for each in all_words:
	doc_1_tf[each] = 0
	doc_2_tf[each] = 0
	doc_3_tf[each] = 0

# Term Frequency calculation for document 1
for each in all_words:
	doc_1_tf.update({each: doc_1_list.count(each)})
	
# Term Frequency calculation for document 2
for each in all_words:
	doc_2_tf.update({each: doc_2_list.count(each)})

# Term Frequency calculation for document 3
for each in all_words:
	doc_3_tf.update({each: doc_3_list.count(each)})

# Term Frequency calculation for query
for each in all_words:
	query_tf.update({each: query_list.count(each)})

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