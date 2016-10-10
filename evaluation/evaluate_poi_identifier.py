#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier as DecisionTree
from sklearn.metrics import recall_score, precision_score

features_train, features_test, labels_train, labels_test = train_test_split(
        features, labels, test_size=0.30, random_state=42)

clf = DecisionTree()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print "---Score---"
print clf.score(features_test, labels_test)
print "---Number of POIs---"
print len(filter(lambda x: x==1.0, labels_test))
print "---Comparing prediction with true values---"
print pred
print labels_test
print "---Recall and Precision---"
print "Recall", recall_score(labels_test, pred)
print "Precision", precision_score(labels_test, pred)
