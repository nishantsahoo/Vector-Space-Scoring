print 'Vector Space Scoring'

doc_1 = "Just keep using random words without any punctuation because that's what we need"
doc_2 = "Another set of words which are added here just so that I can complete doc_2"
doc_3 = "After doc_2 comes doc_3 what do you think we should do next after we're done typing random words"

doc_1_list = doc_1.split(' ')
doc_2_list = doc_2.split(' ')
doc_3_list = doc_3.split(' ')

doc_1_tf = {}
doc_2_tf = {}
doc_3_tf = {}
doc_all_df = {}

for each in doc_1_list:
	if each in doc_1_tf.keys():
		doc_1_tf.update({each: doc_1_tf[each]+1})
	else:
		doc_1_tf.update({each: 1})

for each in doc_2_list:
	if each in doc_2_tf.keys():
		doc_2_tf.update({each: doc_2_tf[each]+1})
	else:
		doc_2_tf.update({each: 1})

for each in doc_3_list:
	if each in doc_3_tf.keys():
		doc_3_tf.update({each: doc_3_tf[each]+1})
	else:
		doc_3_tf.update({each: 1})

# Document Frequency Calculation
for each in doc_1_list:
	if each in doc_all_df.keys():
		doc_all_df.update({each: doc_all_df[each]+1})
	else:
		doc_all_df.update({each: 1})

for each in doc_2_list:
	if each in doc_all_df.keys():
		doc_all_df.update({each: doc_all_df[each]+1})
	else:
		doc_all_df.update({each: 1})

for each in doc_3_list:
	if each in doc_all_df.keys():
		doc_all_df.update({each: doc_all_df[each]+1})
	else:
		doc_all_df.update({each: 1})

print 'Term frequency of Document 1'
print doc_1_tf
print
print 'Term frequency of Document 2'
print doc_2_tf
print
print 'Term frequency of Document 3'
print doc_3_tf
print
print 'Document Frequency'
print doc_all_df
