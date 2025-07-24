

LINKS:
https://www.geeksforgeeks.org/machine-learning/how-to-prepare-data-before-deploying-a-machine-learning-model/
https://machinelearningmastery.com/train-test-split-for-evaluating-machine-learning-algorithms/
https://www.geeksforgeeks.org/machine-learning/stratified-sampling-in-machine-learning/
https://www.geeksforgeeks.org/data-science/stratified-random-sampling-an-overview/
https://www.geeksforgeeks.org/machine-learning/cross-validation-machine-learning/

https://scikit-learn.org/0.15/modules/generated/sklearn.cross_validation.ShuffleSplit.html
	https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.StratifiedShuffleSplit.html
	https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html
	
	https://www.geeksforgeeks.org/machine-learning/how-to-do-train-test-split-using-sklearn-in-python/
	https://www.w3schools.com/Python/python_ml_train_test.asp
	https://www.geeksforgeeks.org/machine-learning/how-to-split-a-dataset-into-train-and-test-sets-using-python/
	
https://www.geeksforgeeks.org/machine-learning/cross-validation-machine-learning/
	https://www.geeksforgeeks.org/machine-learning/stratified-k-fold-cross-validation/
	


sklearn.model_selection.ShuffleSplit in scikit-learn is a cross-validation strategy that generates random train/test splits. Unlike K-Fold cross-validation, where folds are non-overlapping, ShuffleSplit allows for overlapping splits, meaning the same data point can appear in multiple training or testing sets across different splits.
Here's how ShuffleSplit works and its key parameters:
How it Works:
Random Shuffling: For each split, the entire dataset is randomly shuffled.
Splitting: A specified proportion of the data is then allocated to the training set, and the remaining proportion to the test set. This process is repeated for a specified number of iterations.
Key Parameters:
n_splits:
An integer representing the number of independent random splits to generate.
test_size:
Can be an integer or a float.
If an integer, it represents the absolute number of test samples.
If a float (between 0.0 and 1.0), it represents the proportion of the dataset to include in the test split. 
train_size:
Similar to test_size, but for the training set. If both train_size and test_size are specified, they should sum up to 1 (or the total number of samples). If only one is specified, the other is automatically determined.
random_state:
An integer or None. If an integer, it seeds the random number generator, ensuring reproducible results across multiple runs. If None, the random number generator is re-seeded each time, leading to different splits.
Example Usage:
Python
from sklearn.model_selection import ShuffleSplit
import numpy as np


X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
y = np.array([0, 1, 0, 1, 0, 1])


# Create a ShuffleSplit object with 5 splits, 20% test size
ss = ShuffleSplit(n_splits=5, test_size=0.2, random_state=42)


# Iterate through the splits
for train_index, test_index in ss.split(X):
   X_train, X_test = X[train_index], X[test_index]
   y_train, y_test = y[train_index], y[test_index]
   print(f"Train indices: {train_index}, Test indices: {test_index}")
When to Use ShuffleSplit:
When you need multiple independent train/test splits for evaluating model performance.
When the dataset is large, and a K-Fold cross-validation might be computationally expensive.
When you want to control the exact size or proportion of training and testing sets.
Considerations:
Overlapping Splits:
Unlike K-Fold, ShuffleSplit does not guarantee non-overlapping test sets. This means a data point might be used in the test set of one split and the training set of another.
Reproducibility:
Use random_state for reproducible results if needed for debugging or comparing different model configurations.
Stratification:
For classification problems where maintaining class proportions in splits is important, consider using StratifiedShuffleSplit instead, which is a variation of ShuffleSplit that ensures this.

