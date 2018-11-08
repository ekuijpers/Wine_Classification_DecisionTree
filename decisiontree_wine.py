
import numpy as np 
import pandas as pd 
from sklearn.cross_validation import train_test_split 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

#preprocess the data 
##add label to each data set(red and white)
X_red_wine = pd.read_csv('/home/phyllis/Desktop/decision_tree_project/winequality-red.csv', sep = ';')
X_white_wine = pd.read_csv('/home/phyllis/Desktop/decision_tree_project/winequality-white.csv', sep = ';')


n_r = len(X_red_wine)
Y_red = np.ones((n_r, 1)) # label 1 stand for red
n_w = len(X_white_wine)
Y_white = np.zeros((n_w, 1)) # label 0 stand for white

X_frame = [X_red_wine, X_white_wine]
Y_frame = [Y_red, Y_white]
X = pd.concat(X_frame, axis =0, join ='outer')
Y = np.concatenate(Y_frame, axis =0)


#s#plit dataset into test and train
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.3, random_state =100)

#develop a decision classifier 
clf_gini = DecisionTreeClassifier(criterion = 'entropy', splitter = 'best', max_depth = 4, random_state = 100)
clf_gini.fit(X_train, Y_train)

#predict 
Y_prediction = clf_gini.predict(X_test)

#accuracy 
accuracy = accuracy_score(Y_test, Y_prediction)*100
print('Acurracy percentage ='+str(accuracy))
