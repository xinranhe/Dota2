import cPickle as pickle
from sklearn import svm
from sklearn.ensemble import GradientBoostingClassifier
import matplotlib.pyplot as plt
from sklearn import manifold
import numpy as np
import multiprocessing
import sys

from pymongo import MongoClient

def extractDataFromDB(filter_dict, down_sample_rate):
    client = MongoClient()
    collection = client.Dota2.matches
    X = []
    labels = []
    for match in collection.find(filter_dict):
        if np.random.uniform() > down_sample_rate:
            continue
        players = match['players']
        radient_heroes = [player['hero_id'] for player in players[:5]]
        dire_heroes = [player['hero_id'] for player in players[5:]]
        feature = radient_heroes + dire_heroes
        X.append(feature)
        labels.append(int(match['radiant_win']))
    print 'In total %d matches sampled' % len(X)
    pickle.dump((X, labels), open('data/match_prediction_data.pkl', 'wb'))

# build training data
def buildTrainingData(X, labels, weights, is_embed):
    features = []
    y = []

    for i in xrange(len(X)):
        if i % 100 == 0:
            print i,',',
        feature = []
        radient_heros_embed = []
        dire_heros_embed = []
        radient_heros = [0] * 112
        dire_heros = [0] * 112
        for hi in X[i][:5]:
            radient_heros[hi-1] = 1
            radient_heros_embed.extend(weights[hi-1])
        for hi in X[i][5:]:
            dire_heros[hi-1] = 1
            dire_heros_embed.extend(weights[hi-1])

        feature.extend(radient_heros)
        feature.extend(dire_heros)
        # add embed features
        if is_embed:
            feature.extend(radient_heros_embed)
            feature.extend(dire_heros_embed)

        features.append(feature)
        y.append(labels[i])
    print ''
    return features, y

def trainAndPredict(num_trees, train_num):
    train_X = X[:train_num]
    train_y = y[:train_num]  

    test_X = X[train_num:]
    test_y = y[train_num:]

    #clf = svm.SVC()
    clf = GradientBoostingClassifier(n_estimators=num_trees, learning_rate=0.5, max_depth=2, random_state=0)
    clf.fit(train_X, train_y) 
    return (clf.score(train_X, train_y), clf.score(test_X, test_y))

if __name__ == '__main__':
    method = sys.argv[1]
    if method == 'data':
        down_sample_rate = float(sys.argv[2])
        extractDataFromDB({'$or': [{'game_mode': 1}, {'game_mode': 22}], 'duration': {'$gt': 1500}}, down_sample_rate)
    elif method == 'train':
        num_tree = int(sys.argv[2])
        is_embed = int(sys.argv[3]) == 1

        np.random.seed(42)

        # load weights
        weights = pickle.load(open('result/embed_weight_hero.pkl', 'rb'))
        rX, ry = pickle.load(open('data/match_prediction_data.pkl', 'rb'))

        train_num = int(len(rX) * 0.8)
        print "train samples: %d, test samples: %d" % (train_num, len(rX) - train_num)

        X, y = buildTrainingData(rX, ry, weights, is_embed)

        data = zip(X, y)
        np.random.shuffle(data)
        X = [x for (x,y) in data]
        y = [y for (x,y) in data]

        print 'training model'
        result = trainAndPredict(num_tree, train_num)
        
        result_file = open('result/match-prec_%d_%d.txt' % (num_tree, is_embed), 'w')
        result_file.write('%d, %d, %f, %f\n' % (num_tree, is_embed, result[0], result[1]))
        result_file.close()
