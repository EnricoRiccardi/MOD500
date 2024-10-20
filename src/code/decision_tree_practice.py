"""
MOD500 tutorial: Decision tree usage

"""
import numpy as np
from matplotlib import pyplot as plt

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier, plot_tree

from entropy import calculate_entropy, create_experiments
from entropy import create_prob_distribution, plotter



def main():
    n_experiments = 10000
    cases = [2, 4, 6, 8, 20, 50]
    data = np.zeros((n_experiments, len(cases)))
    for i, param in enumerate(cases):
        experiments = create_experiments(n_experiments,
                                         shape='gaussian',
                                         param=param)
        data[:, i] = experiments

    yy = create_experiments(n_experiments,
                            shape='poisson',
                            param=16)
    yy = yy*3/np.max(yy)
    label = yy.astype(np.int64)
 
    clf = DecisionTreeClassifier(max_leaf_nodes=10,
                                 criterion='entropy')
    clf.fit(data, label)

    plot_tree(clf, proportion=True, filled=True)
    
    plt.tight_layout() 

    plt.figure(figsize=(22,12))
    plot_tree(clf, proportion=True, filled=True, fontsize=10)
    plt.show()


    plt.show()


if __name__ == "__main__":
    main()

