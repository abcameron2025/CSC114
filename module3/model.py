"""2
CSC-114 Module 3 — Option 2: Build a Small Model with Keras

A small regression model on the scikit-learn Diabetes dataset.

What we're predicting: a quantitative measure of disease progression one
year after baseline. That target is a continuous NUMBER, which is what makes
this a REGRESSION problem (as opposed to classification, which predicts a
category). Because the answer is a number, we use:
  - a single output neuron with NO activation (so it can output any value), and
  - mean-squared-error (MSE) loss, which punishes being far from the true value.
"""

# ---------------------------------------------------------------------------
# Step 1 — Imports
# ---------------------------------------------------------------------------
# scikit-learn gives us the dataset and an easy train/test split.
# TensorFlow/Keras gives us the model-building tools.
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers

# Make the run repeatable: the same random seed -> the same split and the same
# starting weights every time, so your printed loss is reproducible.
keras.utils.set_random_seed(42)

# ---------------------------------------------------------------------------
# Step 2 — Load the data
# ---------------------------------------------------------------------------
# X holds the 10 input features per patient (age, sex, BMI, blood pressure,
# and six blood-serum measurements). y holds the disease-progression number
# we want to predict. as_frame=False just keeps everything as NumPy arrays.
X, y = load_diabetes(return_X_y=True, as_frame=False)

print(f"Data shape: {X.shape[0]} patients, {X.shape[1]} features each")

# ---------------------------------------------------------------------------
# Step 3 — Split into training and test sets
# ---------------------------------------------------------------------------
# We train the model on 80% of the patients and hold back 20% it never sees
# during training. The test set is how we honestly measure whether the model
# generalizes instead of just memorizing.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------------------------------------------------------
# Step 4 — Put scaling INSIDE the model with a Normalization layer
# ---------------------------------------------------------------------------
# Neural networks train best when each input feature is on a similar scale.
# A Normalization layer learns each feature's mean and standard deviation, then
# subtracts the mean and divides by the std. Putting it inside the model means
# the model accepts RAW inputs at prediction time -- you don't have to remember
# to scale new data yourself later.
#
# .adapt() is how the layer LEARNS those statistics. We show it only the
# TRAINING data, so no information from the test set leaks into the model.
normalizer = layers.Normalization(axis=-1)
normalizer.adapt(X_train)

# ---------------------------------------------------------------------------
# Step 5 — Build the model
# ---------------------------------------------------------------------------
# A simple feed-forward network:
#   - the Normalization layer (scales raw inputs),
#   - two hidden layers with ReLU so the model can learn non-linear patterns,
#   - one output neuron with no activation -> predicts a single number.
model = keras.Sequential([
    keras.Input(shape=(X_train.shape[1],)),  # 10 input features
    normalizer,
    layers.Dense(64, activation="relu"),
    layers.Dense(64, activation="relu"),
    layers.Dense(1),  # single number out = the regression prediction
])

# ---------------------------------------------------------------------------
# Step 6 — Compile: choose how the model learns
# ---------------------------------------------------------------------------
# optimizer="adam": Adam is a popular, well-behaved optimizer that adapts the
#   learning rate as it goes -- a safe default that usually "just works."
# loss="mse": mean squared error is the standard regression loss. It measures
#   the average squared gap between predictions and true values; smaller is
#   better. We also track MAE (mean absolute error) because it's in the same
#   units as the target, so it's easier to interpret.
model.compile(optimizer="adam", loss="mse", metrics=["mae"])

model.summary()

# ---------------------------------------------------------------------------
# Step 7 — Train (up to 200 epochs, with early stopping)
# ---------------------------------------------------------------------------
# One epoch = one full pass over the training data. Over many passes the model
# repeatedly adjusts its weights to shrink the loss. validation_split=0.2 sets
# aside a slice of the TRAINING data to watch for overfitting as we go.
#
# We allow up to 200 epochs, but EarlyStopping (below) will halt training once
# the model stops improving -- so we don't waste epochs or overfit.
#
# EarlyStopping watches the validation loss. If it doesn't improve for
# `patience` epochs in a row, training stops. restore_best_weights=True rewinds
# the model to its BEST epoch, not the last one -- so the saved model is the
# best version we saw, not an overfit later one.
early_stopping = keras.callbacks.EarlyStopping(
    monitor="val_loss",
    patience=20,
    restore_best_weights=True,
)

history = model.fit(
    X_train, y_train,
    epochs=200,
    validation_split=0.2,
    callbacks=[early_stopping],
    verbose=1,
)

# Find the BEST epoch: the one with the lowest validation loss. This answers
# the writeup question "about how many epochs to reach the best result?" --
# which is NOT the number you set (200), but where the model actually stopped
# improving on the held-out validation slice. After this point, training loss
# may keep dropping while val_loss flattens or rises (that's overfitting).
val_losses = history.history["val_loss"]
best_val = min(val_losses)
best_epoch = val_losses.index(best_val) + 1  # +1 because epochs count from 1
print(f"\nBest epoch (lowest val_loss): epoch {best_epoch} of {len(val_losses)}")
print(f"Best validation loss (MSE): {best_val:.2f}")

# ---------------------------------------------------------------------------
# Step 8 — Evaluate on the held-out test set
# ---------------------------------------------------------------------------
# This is the honest score: how the model does on patients it never trained on.
test_loss, test_mae = model.evaluate(X_test, y_test, verbose=0)
print(f"\nTest loss (MSE): {test_loss:.2f}")
print(f"Test MAE:        {test_mae:.2f}  (avg error in target units)")

# ---------------------------------------------------------------------------
# Step 9 — Save the trained model
# ---------------------------------------------------------------------------
# The .keras format saves the architecture AND the learned weights AND the
# Normalization stats together, so you can reload it later and predict from
# raw inputs without rebuilding or rescaling anything.
model.save("diabetes_model.keras")
print("\nSaved model to diabetes_model.keras")

# ---------------------------------------------------------------------------
# Step 10 — Prediction demo: predict from RAW inputs
# ---------------------------------------------------------------------------
# This shows the payoff of putting the Normalization layer inside the model.
# We reload the saved model and hand it RAW patient rows from the test set --
# no manual scaling needed, because the model scales them internally. Then we
# compare each prediction to the patient's true progression number.
reloaded = keras.models.load_model("diabetes_model.keras")

# Take the first 5 test patients (raw, unscaled feature rows).
sample_X = X_test[:5]
sample_y = y_test[:5]

# .predict returns a column of predicted numbers; .flatten() makes it 1-D so
# it lines up with the true values for easy printing.
predictions = reloaded.predict(sample_X, verbose=0).flatten()

print("\n--- Prediction demo (5 held-out patients) ---")
print(f"{'Predicted':>12} {'Actual':>10} {'Error':>10}")
for pred, actual in zip(predictions, sample_y):
    print(f"{pred:>12.1f} {actual:>10.1f} {abs(pred - actual):>10.1f}")
