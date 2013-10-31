a = [1, 2, 3, 4, 5, 6, 10]
b = [3, 6, 10, 15, 18]
c = [1, 10, 15]
d = [1, 10, 20]

doc_array = [a, b, c, d]

def find_intersection(a, b):
    n_intersection = i = j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            n_intersection += 1
            i += 1
            j += 1
        elif a[i] > b[j]:
            j += 1
        elif a[i] < b[j]:
            i += 1
    return n_intersection
    
def find_similarity(a, b):
    n_i = find_intersection(a, b)
    n_u = len(a) + len(b) - n_i
    return (n_i/(n_u * 1.0)) if n_u else 0
    
from collections import defaultdict
    
def construct_index(docs):
    index = defaultdict(list)
    for i, doc in enumerate(docs):
        for word in doc:
            index[word].append(i)
    return index
    
def find_doc_pair_uniq(index): # returns ...
    counts = defaultdict(int)
    for posting_list in index.values():
        for doc1 in posting_list: # go through cross product
            for doc2 in posting_list:
                if doc1 < doc2:
                    doc_pair = (doc1, doc2)
                    counts[doc_pair] += 1
    return counts
    
def print_similarities(doc_array):
    # todo: insert sanity checks
    
    inverted_index = construct_index(doc_array)
    doc_pairs = find_doc_pair_uniq(inverted_index)

    for doc_pair, intersection in doc_pairs.iteritems():
        doc1, doc2 = doc_pair
        print doc_pair, ((intersection * 1.0) / (len(doc_array[doc1]) + len(doc_array[doc2]) - intersection))

print_similarities(doc_array)    
