import numpy as np

# Set seed for reproducibility
np.random.seed(42)

# Generate synthetic nonlinear dataset: y = sin(2*pi*x) + noise
N = 30
x = np.linspace(0, 1, N)
y = np.sin(2 * np.pi * x) + np.random.normal(0, 0.2, N)

# Train (80%) and Validation (20%) Split
indices = np.arange(N)
np.random.shuffle(indices)
train_idx, val_idx = indices[:24], indices[24:]

x_train, y_train = x[train_idx], y[train_idx]
x_val, y_val = x[val_idx], y[val_idx]

degrees = [1, 2, 3, 5, 10, 20]

print(f"{'Degree':<8} | {'Training MSE':<15} | {'Validation MSE':<15}")
print("-" * 45)

for d in degrees:
    # Fit polynomial coefficients using NumPy
    weights = np.polyfit(x_train, y_train, d)

    # Predictions
    y_train_pred = np.polyval(weights, x_train)
    y_val_pred = np.polyval(weights, x_val)

    # Calculate Mean Squared Error (MSE)
    train_mse = np.mean((y_train - y_train_pred) ** 2)
    val_mse = np.mean((y_val - y_val_pred) ** 2)

    print(f"{d:<8} | {train_mse:<15.5f} | {val_mse:<15.5f}")