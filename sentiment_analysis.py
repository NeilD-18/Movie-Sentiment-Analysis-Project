#Neil Daterao

#Program that performs sentiment analysis over movie reviews given in text files 

## Evaluation
#Function to evaluate if the prediction is correct or not and prints the percentage of correctness for all the predictions 
def evaluate(word_sentiment_dict, filename):
    f = open(filename, "r")
    correct = 0
    incorrect = 0
    for line in f:
        line = line.strip()
        score = int(line[0])
        words = line[2:]
        predicted_positive = is_positive(words, word_sentiment_dict)
        if score > 2 and predicted_positive:
            correct += 1
        elif score <= 2 and not predicted_positive:
            correct += 1
        else:
            incorrect += 1
    f.close()
    print("predicted correctly:", correct, "("+str(correct/(correct+incorrect))+")")
    print("predicted incorrectly:", incorrect, "("+str(incorrect/(correct+incorrect))+")")

#Function that makes the dictionary of word sentiments given a file
def make_word_sentiment_dictionary(filename): 
    
    file = open(filename, "r")
    word_sentiment_dictionary = {}
    
    for line in file: 
        line = line.strip()
        words = line.split(" ")
        
        #Look at all the words from the first index onwards, since index 0 contains the score of the review 
        for word in words[1:]: 
            #We want all the words in the dictionary to be lowercase 
            word = word.lower()
            
            #Initialize the word in the dictionary if it's not already there
            if word not in word_sentiment_dictionary.keys():
                word_sentiment_dictionary[word] = {'total score': int(words[0]), 'count': 1, 'average score': int(words[0]) / 1 }
            
            #Dictionary doesn't update instantaneously so you need to update the average score given the new "total score" and "count"    
            elif word in word_sentiment_dictionary.keys():
                word_sentiment_dictionary[word] = {'total score': word_sentiment_dictionary[word]['total score'] + int(words[0]), 'count': word_sentiment_dictionary[word]['count'] + 1 , 'average score': (word_sentiment_dictionary[word]['total score'] + int(words[0])) / (word_sentiment_dictionary[word]['count'] + 1)  }
                    
    file.close()
    
    return word_sentiment_dictionary
    
#Function to predict the sentiment score of a movie review based on a provided dictionary   
def predict_sentiment_score(movie_review, movie_review_dict):
    movie_review = str(movie_review.strip())
    movie_review = movie_review.split()
    total_score = 0 
    
    #Get the average sentiment of each word in the review, add that to a total, and then return the average of review
    for word in movie_review:
        word = word.lower()
        if word in movie_review_dict.keys():
            total_score += movie_review_dict[word]['average score']
    
    #If the word is not in the dictionary, assume a neutral score (2)
        else:
            total_score += 2
    
    return total_score / len(movie_review) #This is the average


#Function to test if the movie review is positive or not, returns True if positive and False if negative. 
def is_positive(movie_review, movie_review_dict): 
    prediction = predict_sentiment_score(movie_review, movie_review_dict)
    
    #Adjust this value for percentage correctness. This value makes the program 75.875% accurate 
    if prediction >= 2.133: 
        return True
    else:
        return False 
    

### DO NOT DELETE THIS LINE: beg testing
    
word_sentiment_dictionary = make_word_sentiment_dictionary("/Users/neil/Desktop/School Coding Projects/CSC-106/Project 4/movie_reviews_training.txt")

#pretty_print(word_sentiment_dictionary)
#print("nice", word_sentiment_dictionary["nice"])
#print("story", word_sentiment_dictionary["story"])
#print("process", word_sentiment_dictionary["process"])
print(predict_sentiment_score("Devoid of any of the qualities that made the first film so special .", word_sentiment_dictionary))

evaluate(word_sentiment_dictionary, "/Users/neil/Desktop/School Coding Projects/CSC-106/Project 4/movie_reviews_dev.txt")
