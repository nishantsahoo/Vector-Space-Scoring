'''
Author - Nishant Sahoo
'''

print 'Vector Space Scoring'

doc_1 = "Just keep using random words without any punctuation because that's what we need"
doc_2 = "Another set of words which are added here just so that I can complete doc_2"
doc_3 = "After doc_2 comes doc_3 what do you think we should do next after we're done typing random words"

doc_1_list = doc_1.split(' ')
doc_2_list = doc_2.split(' ')
doc_3_list = doc_3.split(' ')

all_words  = list(set(doc_1_list + doc_2_list + doc_3_list))

print 'List of all words -'
print all_words
print

doc_1_tf   = {} # term frequency of doc_1
doc_2_tf   = {} # term frequency of doc_1
doc_3_tf   = {} # term frequency of doc_1
doc_all_df = {} # document frequency

# Initializing all tf lists to be empty
for each in all_words:
	doc_1_tf[each] = 0
	doc_2_tf[each] = 0
	doc_3_tf[each] = 0

# Term Frequency calculation for document 1
for each in all_words:
	if each in doc_1_list:
		doc_1_tf.update({each: doc_1_tf[each]+1})
	
# Term Frequency calculation for document 2
for each in all_words:
	if each in doc_2_list:
		doc_2_tf.update({each: doc_2_tf[each]+1})
	
# Term Frequency calculation for document 3
for each in all_words:
	if each in doc_3_list:
		doc_3_tf.update({each: doc_3_tf[each]+1})

# Document Frequency Calculation
for each in all_words:
	doc_all_df[each] = (doc_1_tf[each] + doc_2_tf[each] + doc_3_tf[each])


print 'Term frequency of Document 1 -'
print doc_1_tf
print
print 'Term frequency of Document 2 -'
print doc_2_tf
print
print 'Term frequency of Document 3 -'
print doc_3_tf
print
print 'Document Frequency -'
print doc_all_df

# Calculation of tf-tdf now
