# Module 3 — Explanation

> ✍️ This is the graded part. Replace every "Write:" prompt below with your OWN
> words. The numbers are filled in from the latest run as reference — confirm
> they still match if you re-run. Delete these note lines before submitting.

**What I built:** _Write: 2–3 sentences — a small Keras regression model on the
scikit-learn Diabetes dataset, and what it predicts._

---

## Q1 — What are the features and the target?

_Write: list the 10 features (age, sex, BMI, average blood pressure, and six
blood-serum measurements) and say what the target is (disease progression one
year after baseline). Mention the dataset has 442 patients._

## Q2 — Is it regression or classification? How do you know?

_Write: state regression, then explain HOW you know — the target is a continuous
number, not a category. Back it up from the code: the final layer is `Dense(1)`
with no activation, and the loss is MSE. (Optional: what would classification
have looked like instead?)_

## Q3 — What optimizer trained your model, and why?

_Write: name Adam. Explain what an optimizer actually does (adjusts the model's
weights to reduce the loss), then why Adam is a good default (adapts the step
size per weight, so it's forgiving of the starting learning rate)._

## Q4 — About how many epochs to reach the best result?

_Write: I set up to 200 epochs with early stopping. Explain the difference
between the number I set and where the model actually stopped improving._

- Best epoch (lowest validation loss): **73**
- Training stopped at epoch **93** (early stopping, patience 20)
- _Write: note that training loss kept dropping while validation loss plateaued —
  i.e. overfitting after ~epoch 73 — which is why early stopping helps._

## Q5 — What was the lowest loss your model reached?

_Write: report your real numbers and say what they mean._

- Best validation loss (MSE): **2854.19**
- Test loss (MSE): **3001.63**
- Test MAE: **43.85** — _Write: one line on what MAE means in plain units
  (average prediction is off by ~44 progression points)._

## Q6 — Can you save the model, send it inputs, and get a prediction? Show it.

_Write: yes — describe the steps: `model.save(...keras)` → `keras.models.load_model(...)`
→ `.predict(...)` on raw (unscaled) patient rows. Then explain what the table shows._

| Predicted | Actual | Error |
|----------:|-------:|------:|
| 169.2 | 219.0 | 49.8 |
| 192.2 | 70.0 | 122.2 |
| 145.7 | 202.0 | 56.3 |
| 330.8 | 230.0 | 100.8 |
| 88.5 | 111.0 | 22.5 |

_Write: one observation — some predictions are close, others far off, so the
model works but isn't precise on this hard dataset._

## What I'd improve (optional, but a strong finish)

_Write: 1–2 ideas, e.g. more training data, or regularization. Note that I
already added early stopping to fight the overfitting I observed._
