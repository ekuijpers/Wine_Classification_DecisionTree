# Wine_Classification_DecisionTree
The goal of this project is to explore a decision tree to classify the type of wine (red or white).This is a kaggle project from: https://www.kaggle.com/c/wine-quality-decision-tree/leaderboard

## Background
Decision tree is an supervised machine algorithm which can devide the dataset into sub-dataset according to data's feature. Compare to dataset, sub-dataset has higher homogeneous (label we need to classify).Decision Tree algorithms are referred to as CART or Classification and Regression Trees.In this project, we only use Decision tree for Classification. 
This is a very nice explaination of decision tree: https://towardsdatascience.com/decision-trees-in-machine-learning-641b9c4e8052

## Dataset: wine-quality
This dataset is public available for research. The details are described in:
  P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. 
  Modeling wine preferences by data mining from physicochemical properties.
  In Decision Support Systems, Elsevier, 47(4):547-553. ISSN: 0167-9236.

Available at: https://www.sciencedirect.com/science/article/pii/S0167923609001377?via%3Dihub

## Package
In this project, we used package of Numpy, Pandas, Scikit-learn. 

## Pseudo code: 
1. Preprocess data.     
(a)Add lable to dataset: The dataset including two files (winequality-red.csv and winequality-white.csv) which has 12 features but dont have label we need to classify(red and white). Hence, We need to create a label array        
(b)Split dataset into train dataset and test dataset. the split rate set to 7/3

2. Build a Decision tree classifier using scikit-learn
3. Predict the Test dataset
4. Calculate accuracy of prediction: The final result of accuracy percentage is 98.21%
