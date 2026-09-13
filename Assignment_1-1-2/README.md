# Polynomial Regression Capacity Comparison

This project generates a nonlinear synthetic dataset and compares polynomial regression models of different capacities.

## Dataset

The dataset is generated as:

```python
np.random.seed(42)
N = 30
x = np.linspace(0, 1, N)
y = np.sin(2 * np.pi * x) + np.random.normal(0, 0.2, N)
```

The data is then split into train and validation sets with an 80/20 split.

## Models

The following polynomial degrees are compared:

- 1
- 2
- 3
- 5
- 10
- 20

## Observed Results

The script prints the following table:

| Degree | Training MSE | Validation MSE |
|--------|--------------|-----------------|
| 1      | 0.21982      | 0.40329         |
| 2      | 0.21894      | 0.39945         |
| 3      | 0.02102      | 0.06194         |
| 5      | 0.01936      | 0.04798         |
| 10     | 0.01329      | 0.07985         |
| 20     | 0.00799      | 0.25738         |

## Answers to the Questions

1. Which model underfits?

   The degree-1 and degree-2 models clearly underfit because they have very high training and validation MSE values. They are too simple to represent the nonlinear sine pattern in the data.

2. Which model gives the best validation performance?

   The degree-5 model gives the best validation MSE, with a validation error of about 0.04798. It balances flexibility and generalization better than the other models.

3. At what point does overfitting begin?

   Overfitting begins around degree 10. The training MSE keeps decreasing as capacity grows, but the validation MSE starts to rise sharply after degree 5, especially at degree 10 and degree 20.

4. How does increasing capacity affect training error?

   Increasing polynomial degree lowers training error continuously. More flexible models are able to fit the training points more closely, so the training MSE decreases.

5. Why does validation error eventually increase?

   Validation error rises because the model starts memorizing the training data rather than learning the true underlying function. This makes the model less able to generalize to unseen data, increasing validation MSE.

6. Explain the experiment using the bias-variance tradeoff.

   Low-degree models have high bias and low variance: they are too simple and cannot model the nonlinear data well. As the degree increases, the model becomes more flexible and bias decreases, but variance increases because the model fits noise in the training data. The best model is the one with the lowest validation error, which is the point where bias and variance are balanced. After that point, the extra flexibility increases variance more than it decreases bias, causing validation error to rise.
