# Midterm Exam — Artificial Intelligence

## Kaggle Machine Learning Challenge

The objective of this exam is to solve a **Machine Learning problem with unseen data**.

You will receive a Kaggle competition containing training and test data.

Your goal is to build a Machine Learning solution, evaluate it correctly, generate predictions for the unseen test data, and submit your results to Kaggle.

The objective is **not only to obtain a good Kaggle score**. You must demonstrate that you understand the complete Machine Learning process and the mathematical foundations of the model you use.

---

## Part 1 — Understand the Problem

Before training your models:

- Identify the **input features**.
- Identify the **target variable**.
- Determine whether the problem is classification or regression.
- Identify the evaluation metric used by the Kaggle competition.
- Inspect the dataset and identify potential problems that may affect your model.

Keep this analysis short and focused on information relevant to your solution.

---

## Part 2 — Data Preparation

Prepare the data appropriately for Machine Learning.

Depending on the dataset, consider:

- Missing values
- Categorical variables
- Feature scaling
- Class imbalance
- Irrelevant features
- Possible data leakage

---

## Part 3 — Baseline

Implement a simple **baseline model**.

---

## Part 4 — Model Selection and Experimentation

Experiment with at least **two Machine Learning models**.

You may use any AI model such as:

- K-Nearest Neighbors
- Neural Networks / MLP
- etc.

You are free to select the models you consider appropriate for the problem, even if they were not covered in class.

---

## Part 5 — Final Kaggle Submission

Select your final model and train the solution that you will use to generate predictions for the Kaggle test dataset.

Create the required:

`submission.csv`

Upload it to Kaggle and record your score.

The model reported here must be the same model explained in your video.

---

# Part 6 — Mathematical Explanation Video

Record an **individual video of maximum 3 minutes** explaining the mathematical foundations of the model used for your final Kaggle submission.

The purpose of the video is to demonstrate that you understand **how your selected model works**, not only how to call it from a Python library.

Your explanation must include:

1. **Inputs and outputs**

   Explain what enters the model and what the model produces.

2. **Mathematical formulation**

   Present at least **one important equation** that represents how your model works.

3. **Variables**

   Explain the meaning of the main variables in the equation.

4. **Learning / decision process**

   Explain what the model learns, optimizes, or uses to make its prediction.

5. **Connection with your Kaggle solution**

   Explain how the mathematical formulation relates to the specific problem you solved.

For example, depending on your model, you could explain concepts such as:

- KNN → distance, neighbor-based decision, etc.
- MLP → weighted sums, activation functions, loss,backpropagation, hyperparameter tuning, etc.
- etc.

The important part is to demonstrate that you understand:

**Equation → Variables → Model behavior → Your implementation**

You may use:

- Whiteboard
- Paper
- Tablet
- Screen annotation
- Your own diagrams

Do not simply read definitions, slides, AI-generated explanations, or source code.

Explain the model **in your own words**.

---

# Submission

Submit:

1. **Jupyter Notebook (`.ipynb`)**
2. **Screenshots of your Kaggle submission and score**
3. **Link to your 3-minute video**

The notebook must run from beginning to end and reproduce your reported validation results.

---

# Evaluation

| Component | Weight |
|---|---:|
| Data preparation | 20% |
| Justification of baseline model selection and training | 20% |
| Model results and interpretation | 10% |
| Kaggle performance on unseen data | 25% |
| Mathematical explanation video (correctness, explanation of equations and variables, connection to implementation) | 25% |
| **Total** | **100%** |

### Mathematical Video Evaluation

Video production quality, editing, camera quality, or presentation style will **not** affect the grade.

Your camera should be on, and you should be clearly visible in the video.

---

# Important

A higher Kaggle score does **not automatically mean a higher exam grade**.

You will be evaluated on your ability to:

**Understand the problem → Prepare the data → Validate correctly → Experiment → Generalize to unseen data → Explain the mathematics behind your solution**

A simpler model that is correctly implemented, evaluated, and understood may demonstrate more knowledge than a complex model used without understanding.