# Wine_Classification_DecisionTree
This project is aiming to exploit a popular machine learning method: decision tree to classify wine into two type (red or white).This project can be found at: https://www.kaggle.com/c/wine-quality-decision-tree/leaderboard

## Introduction
Decision tree is an supervised machine algorithm which can devide the dataset into sub-dataset according to data's feature. Compare to dataset, sub-dataset has higher homogeneous (label we need to classify).Decision Tree algorithms are referred to as CART or Classification and Regression Trees.In this project, we only use Decision tree for Classification. 
For more detail of decision tree: https://towardsdatascience.com/decision-trees-in-machine-learning-641b9c4e8052

## Dataset: wine-quality
This dataset is public available for research. It includes 5097(training) + 1400(testing) samples. The details are described in the paper:
  P. Cortez, A. Cerdeira, F. Almeida, T. Matos and J. Reis. 
  Modeling wine preferences by data mining from physicochemical properties.
  In Decision Support Systems, Elsevier, 47(4):547-553. ISSN: 0167-9236.

Available at: https://www.sciencedirect.com/science/article/pii/S0167923609001377?via%3Dihub

The data including 11 features of wine that might related to wine type: 

1. Fixed acidity   
2. Volatile acidity    
3. Citric acid    
4. Residual sugar   
5. Chlorides    
6. Free sulfur dioxide   
7. Total sulfur dioxide         
8. Density    
9. pH   
10. Sulphates    
11. Alcohol   

## Result 
Decision tree are able to achieve testing accuracy of 98.21%
