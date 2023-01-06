import spacy
nlp = spacy.load('en_core_web_md')  # More complex NLP model (sm vs md)

'''
nlp = spacy.load('en_core_web_sm') - When using the simpler model, this warning is output to the console:

UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
'''

## Semantic Similarity Between Words ##

# Default example

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print("\n----------Semantic Similarity Between Words------------")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# My example

print("\n")
word4 = nlp("trousers")
word5 = nlp("glasses")
word6 = nlp("sun")
print(word4.similarity(word5))
print(word6.similarity(word5))
print(word6.similarity(word4))

'''
Note - In the case of the words "banana" and "monkey," it is likely that these words appear in similar contexts more often than "banana" and "cat," which could explain why the similarity measure is higher for "banana" and "monkey." For example, "monkey" and "banana" might both appear in contexts related to similar environments or a stereotypical source of sustenance, while "cat" might appear in a more diverse range of contexts including domestication and humour. 
'''

## Working with Vectors ##

print("\n\n----------Working with Vectors------------")

tokens = nlp("cat apple monkey banana")

for i in tokens:
    for y in tokens:

        print(i.text, y.text, i.similarity(y))


# Working with Sentences
print("\n\n----------Working with Sentences------------")

sentence_to_compare = "Why is my cat on the car"

sentences = [
    "where did my dog go",
    "Hello, there is my car",
    "I\'ve lost my car in my car",
    "I\'d like my boat back",
    "I will name my dog Diana",
    "blah blah blah"
]
model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)
