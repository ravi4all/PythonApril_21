dataset = {
    "action" : ["matrix","batman","superman","dabang","avengers","thor",
                "hulk","krrish","ironman",'kgf'],
    "comedy" : ["the mask","dhamaal","bala","housefull","golmaal",
                "hera pheri","golmaal 2","dhamaal 2","hera pheri 2"],
    "drama" : ["dabang","krrish","hera pheri","bala","kahani","batla house",
               "kgf","zero","sultan"],
    "thriller" : ["kahani","kgf","batla house","madras cafe","uri",
                  "raw","lucy","the ring","oculus"],
    "horror" : ["oculus","the ring","it","the ring 2","evil dead",
                "conjuring","conjuring 2","bhootnath","aatma"]
}

user_1 = {'hulk','dabang','thor', 'lucy', 'it', 'golmaal', 'kgf', 'bala',
          'ironman', 'matrix'}
user_2 = {'hulk','kahani','raw', 'lucy', 'evil dead', 'thor', 'kgf', 'it',
          'sultan', 'oculus'}

common_movies = user_1.intersection(user_2)

scores = {}
for item in dataset:
    movies = set(dataset[item])
    numer = common_movies.intersection(movies)
    denom = common_movies.union(movies)
    score = len(numer) / len(denom)
    scores[item] = round(score,2)

print(scores)
cat = max(scores, key=scores.get)

movies = set(dataset[cat]).intersection(user_1) - user_2
print("Rec movies are",movies)




