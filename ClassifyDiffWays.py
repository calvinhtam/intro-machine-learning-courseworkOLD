from sklearn.naive_bayes import GaussianNB


def classify(features_train, labels_train):
    clf = GaussianNB()
    return clf.fit(features_train, labels_train)
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier

