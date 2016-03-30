import ast
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.image as image
import cPickle as pickle
from os import listdir
from os.path import isfile, join
from util import hero_names_dict
from sklearn import manifold
from sklearn.decomposition import PCA
from util import hero_names_dict
from sklearn.neighbors import NearestNeighbors
import sys

kComponentNum = 2
kNeiborSize = 5

def computeNearestNeighbor(weights):
    f = open('result/nn_hero.txt', 'w')
    nbrs = NearestNeighbors(n_neighbors=6, algorithm='ball_tree').fit(weights)
    distances, indices = nbrs.kneighbors(weights)
    f.write('| Hero | Nearest Heroes |\n')
    f.write('| ------------- | ------------- |\n')
    for i in xrange(len(weights)):
        if i+1 in hero_names_dict:
            name = hero_names_dict[i+1].lower().replace(' ','')
            picture_file = 'result/heroes/' + name + '.png'
            temp =  '| <img src=%s style="height:30px; width:30px"></img>|' % picture_file
            for j in xrange(1, len(indices[i])):
                if indices[i][j]+1 in hero_names_dict:
                    name = hero_names_dict[indices[i][j]+1].lower().replace(' ','')
                    picture_file = 'result/heroes/' + name + '.png'
                    temp += '<img src=%s style="height:30px; width:30px"></img>&nbsp;&nbsp;' % picture_file
            temp = temp + '|'
            f.write('%s\n' % temp)  

def computeEmbedding(weights, embed_type):
    if embed_type == 'mds':
        mds = manifold.MDS(2, max_iter=100, n_init=1)
        Y = mds.fit_transform(weights)
    elif embed_type == 'tsne':
        tsne = manifold.TSNE(n_components=2, init='pca', random_state=0)
        Y = tsne.fit_transform(weights)
    elif embed_type == 'isomap':
        Y = manifold.Isomap(kNeiborSize, 2).fit_transform(weights)
    elif embed_type == 'spectral':
        se = manifold.SpectralEmbedding(n_components=2,
                                        n_neighbors=kNeiborSize)
        Y = se.fit_transform(weights)
    elif embed_type == 'pca':
        Y = PCA(n_components=2).fit_transform(weights)
    else:
        Y = manifold.Isomap(kNeiborSize, 2).fit_transform(weights)
    pos = zip(Y[:,0], Y[:,1])
    return pos

def generateEmbeddingHTML(pos, height, width, embed_type, image_size=(50,50)):
    # generate html

    result_file = open('result/result_hero_%s.html' % embed_type, 'w')

    posX = [x for (x,y) in pos]
    posY = [y for (x,y) in pos]
    max_absX = max(-min(posX), max(posX))
    max_absY = max(-min(posY), max(posY))

    x_scale = 0.5 * height / max_absX
    y_scale = 0.5 * width / max_absY

    result_file.write('<html><body>\n')
    for i in xrange(len(pos)):
        if (i+1) in hero_names_dict:
            temp_name = hero_names_dict[i+1].lower().replace(' ','')
            picture_file = 'heroes/' + temp_name + '.png'

            result_file.write('<div style="position:absolute; top:%dpx; left:%dpx;"><img src=%s style="height:%dpx; width:%dpx"></img></div>\n' \
                % (0.5 * height + x_scale * posX[i], 0.5 * width + y_scale * posY[i], picture_file, image_size[0], image_size[1]))
    result_file.write('</body></html>\n')

if __name__ == '__main__':
    weights_file = sys.argv[1]
    weights = pickle.load(open('result/%s' % weights_file, 'rb'))
    if sys.argv[2] == 'NN':
        computeNearestNeighbor(weights)
    else:
        embed_types = sys.argv[2].split(',')
        for embed_type in embed_types:
            pos = computeEmbedding(weights, embed_type)
            generateEmbeddingHTML(pos, 4000, 4000, embed_type)
