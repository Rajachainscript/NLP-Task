import math
import string


def preprocess(text):
    text=text.lower()
    text=text.translate(str.maketrans('','', string.punctuation))
    return text.split()

def fit(training_data):
    class_counts={'positive':0,'negative':0}
    class_word_counts={'positive':{},'negative':{}}
    vocab=set()
    total_docs=len(training_data)
    for sentence, label in training_data:
        
        class_counts[label]+=1
        words=preprocess(sentence)
        for word in words:
            vocab.add(word)
            class_word_counts[label][word]=class_word_counts[label].get(word,0)+1
    prior={
        'positive': class_counts['positive'] / total_docs,
        'negative': class_counts['negative'] / total_docs
     }
    likelihood={'positive':{},'negative':{}}
    vocab_size=len(vocab)
    for label in ['positive','negative']:
        total_words=sum(class_word_counts[label].values())
        for word in vocab:
            count=class_word_counts[label].get(word,0)
            likelihood[label][word ]=(count+1)/(total_words+vocab_size)
    return {
        'prior': prior,
        'likelihood':likelihood,
        'vocab':vocab
    }

def predict(sentence,model):
    words=preprocess(sentence)
    score={
        'positive':math.log(model['prior']['positive']),
        'negative':math.log(model['prior']['negative'])
    }
    for label in ['positive','negative']:
        for word in words:
            if word in model['vocab']:
                score[label]+=math.log(model['likelihood'][label][word])
    return 'positive'if score['positive']>score['negative'] else 'negative'

training_data = [
("This movie is fantastic! I really love it.", "positive"),
("The plot was terrible and the actors were bad.", "negative"),
("Great direction and superb performances.", "positive"),
("It was a waste of time, boring and dull.", "negative"),
("The cinematography is stunning and the score is beautiful.", "positive"),
("Poor script, awful dialogue, and weak characters.", "negative"),
("I highly recommend this film, it's a masterpiece.", "positive"),
("I hated every minute of it, completely unoriginal.", "negative"),
("A heartwarming story with brilliant acting.", "positive"),
("The worst movie I’ve ever seen, a total disaster.", "negative"),
("this movie is terrible disaster with awful dialogue","negative")
]

test_cases = [
    ("I love the brilliant acting in this heartwarming story." ),
    ("This movie is a terrible disaster with awful dialogue."),
    ("The plot is boring and the script is poor."),
    ("Stunning cinematography and a beautiful score."),
    ("This is a fantastic masterpiece I highly recommend."),
    ("Completely unoriginal and a waste of time."),
    ("A superb film with great direction."),
    ("I hated the weak characters."),
    ("This is neither good nor bad, quite average."),
    ("")
]
model= fit(training_data)
#print(model)

for sentence  in test_cases:
    print(sentence, predict(sentence,model))
