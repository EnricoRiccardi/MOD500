"""
MOD500 tutorial: Decision tree learning usage

"""
import numpy as np
from matplotlib import pyplot as plt

from sklearn.tree import DecisionTreeClassifier, plot_tree

from entropy import create_experiments


def generate_data(n_experiments, shape='gaussian', params=(16,)):
    """Generate experiments"""
    data = np.zeros((n_experiments, len(params)))
    for i, param in enumerate(params):
        experiments = create_experiments(n_experiments,
                                         shape=shape,
                                         param=param)
        data[:, i] = experiments
    return data


def make_categorical(distr, n_cat=3):
    """Make a categorical distribution from a discrete one"""
    label = distr*n_cat/np.max(distr)
    label = label.astype(np.int64)
    return label


def main():
    """Plant a tree"""
    n_experiments = 100000

    # Data generation
    cases = [2, 4, 6, 8, 20, 50]
    data = generate_data(n_experiments, params=cases)

    # Categorical Label
    y_tmp = create_experiments(n_experiments,
                               shape='poisson',
                               param=16)
    label = make_categorical(y_tmp)

    # Make a tree
    clf = DecisionTreeClassifier(max_leaf_nodes=10,
                                 criterion='entropy')
    clf.fit(data, label)

    # Plot
    plt.figure(figsize=(22,12))
    plot_tree(clf, proportion=True, filled=True, fontsize=10)
    plt.show()


if __name__ == "__main__":
    main()
