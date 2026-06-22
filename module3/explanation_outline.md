# Module 3 — Explanation (OUTLINE / fill-in template)

> This is a skeleton to guide your writeup. Replace each prompt with your OWN
> words. The graded part is YOUR explanation — if the wording is the agent's,
> it doesn't count. Delete these note lines and the checkboxes before you submit.

## Intro (2–3 sentences)
- What you built: a small Keras regression model on the scikit-learn Diabetes dataset.
- What it predicts, in one line.

## Q1 — Features and target
- [ ] List the 10 features (age, sex, BMI, avg blood pressure, 6 blood-serum measures).
- [ ] State the target: disease progression one year after baseline (a number).
- [ ] One line on dataset size (442 patients).

## Q2 — Regression or classification, and how you know
- [ ] State: regression.
- [ ] Reason 1 — the target is a continuous number, not a category.
- [ ] Reason 2 — point to the code: `Dense(1)`, no activation, MSE loss.
- [ ] (Optional) one line on what classification would have looked like instead.

## Q3 — Optimizer and why
- [ ] Name it: Adam.
- [ ] Say what an optimizer *does* (adjusts weights to reduce the loss).
- [ ] Why Adam specifically (adapts step size per weight -> forgiving default).

## Q4 — Epochs to best result
- [ ] What you set: 200.
- [ ] What actually happened: training loss kept dropping, val_loss plateaued
      around ~2886 well before epoch 200.
- [ ] Your conclusion: roughly which epoch improvement stopped + the word *overfitting*.

## Q5 — Lowest loss (use YOUR real numbers)
- [ ] Test MSE: ______ (this is "the loss").
- [ ] Test MAE: ______ (one line on what that means in plain units).
- [ ] (Optional) before/after: 50 epochs gave MSE ~____, 200 gave ~____.

## Q6 — Save -> reload -> predict (show it)
- [ ] Name the steps: `model.save` -> `load_model` -> `.predict` on raw rows.
- [ ] Paste your Predicted/Actual/Error table as evidence:

      Predicted     Actual      Error
      ______        ______      ______
      ...

- [ ] One observation (close on some, off on others -> works but not precise).

## Closing — what you'd improve (optional but strong)
- [ ] 1–2 ideas: more data, regularization / early stopping to fight the
      overfitting you saw.
