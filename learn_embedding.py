from keras.models import Sequential
from keras.layers.embeddings import WordContextProduct, Embedding
from keras.layers.core import Dense, Activation, Flatten
from keras.optimizers import SGD, RMSprop, Adagrad
from dota2py import data
from util import hero_names_dict
import numpy as np
import cPickle as pickle
import sys
import ast
from pymongo import MongoClient



class EmbeddingTrainer(object):
    def __init__(self, vocabulary_size):
        # init mongo client
        client = MongoClient()
        self.collection = client.Dota2.matches
        # embedding dimension
        self.embeddingDimension = 40
        # vocabulary size 
        self.vocabulary_size = vocabulary_size
        # model
        self.model = None

    def buildModel(self, embedding_dimension):
        self.model = Sequential()
        self.model.add(WordContextProduct(self.vocabulary_size, proj_dim=embedding_dimension, init="uniform"))
        self.model.compile(loss='binary_crossentropy', optimizer='rmsprop')

    def buildData(self, ids, X_train, y_train):
        for i, hi in enumerate(ids):
            for hj in ids[:i]:
                X_train.append((hi-1, hj-1))
                y_train.append(1)
                # negative samples
                sample_id = np.random.randint(0, self.vocabulary_size)
                X_train.append((hi-1, sample_id))
                y_train.append(0)

    def trainItemModel(self, filter_dict, num_ep):
        games_seen = 0
        losses = []
        for i in xrange(num_ep):
            for match in self.collection.find(filter_dict):
                players = match['players']
                games_seen += 1
                X_train = []
                labels = []
                # we learn item embedding only from winning team
                #if match['radiant_win']:
                #    temp_players = players[:5]
                #else:
                #    temp_players = players[5:]
                for player in players:
                    items = [player['item_%d' % i] for i in xrange(6) if player['item_%d' % i] != 0 and player['item_%d' % i] <= 254]
                    if(len(items) > 1):
                        self.buildData(items, X_train, labels)
                X = np.array(X_train, dtype="int32")
                loss = self.model.train_on_batch(X, labels)
                losses.append(loss)
                if len(losses) % 100 == 0:
                    print 'loss=' + str(np.mean(losses))
                    print '%d games seen' % (games_seen)
                    losses = []
        print("Training completed!")

        weights = self.model.layers[0].get_weights()[0]
        return weights        

    def trainHeroModel(self, filter_dict, num_ep):
        games_seen = 0
        losses = []
        for i in xrange(num_ep):
            for match in self.collection.find(filter_dict):
                players = match['players']
                radient_heroes = [player['hero_id'] for player in players[:5]]
                dire_heroes = [player['hero_id'] for player in players[5:]]

                games_seen += 1
                X_train = []
                labels = []
                self.buildData(radient_heroes, X_train, labels)
                self.buildData(dire_heroes, X_train, labels)
                
                X = np.array(X_train, dtype="int32")
                loss = self.model.train_on_batch(X, labels)
                losses.append(loss)
                if len(losses) % 100 == 0:
                    print 'loss=' + str(np.mean(losses))
                    print '%d games seen' % (games_seen)
                    losses = []
        print("Training completed!")

        weights = self.model.layers[0].get_weights()[0]
        return weights

if __name__ == '__main__':
    # hero for hero embedding; item for item embedding
    model_type = sys.argv[1]
    # matches filter
    filter_dict = ast.literal_eval(sys.argv[2])

    if model_type == 'hero':
        kDotaHeroesNum = 112
        trainer = EmbeddingTrainer(kDotaHeroesNum)
        print 'Build model'
        embedding_dimension = 40
        trainer.buildModel(embedding_dimension)
        print '...Done'
        weights = trainer.trainHeroModel(filter_dict, 2)
        # save weights
        pickle.dump(weights, open('result/embed_weight_hero.pkl', 'wb'))
    elif model_type == 'item':
        kDotaItemNum = 254 
        trainer = EmbeddingTrainer(kDotaItemNum)
        print 'Build model'
        embedding_dimension = 40
        trainer.buildModel(embedding_dimension)
        print '...Done'
        weights = trainer.trainItemModel(filter_dict, 2)
        # save weights
        pickle.dump(weights, open('result/embed_weight_item.pkl', 'wb'))

