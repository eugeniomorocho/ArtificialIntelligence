# Artificial Intelligence
This repository is designed to provide you with hands-on experience and in-depth understanding of fundamental AI topics. The repository includes both coding exercises and project-based activities, and were created using Python 3.x as the interpreter.

## Getting Started
1. Clone this repository to your local machine:  

   ```
   git clone https://github.com/eugeniomorocho/ArtificialIntelligence.git
   ```

2. Navigate to the specific Notebook's directory:  

   ```
   cd ArtificialIntelligence/<folder>/<notebook.ipynb>/
   ```
   
3. Follow the instructions in the file for each week's lab.

4. To update your local fork to the newest commit, execute:

   ```
   git fetch 
   ```

## Requirements

- `Python 3.x` as the interpreter
- Additional dependencies specified in each week's lab instructions
- Create a [GitHub](https://github.com) repository for submitting your assignments and add `@eugeniomorocho` as collaborator.

## Minimum Contents

- Intelligent agents, problem solving via search, adversarial search, first-order logic, first-order inference, knowledge representation, probabilistic reasoning, machine learning.

## Learning Outcomes

- Describe the process of artificial intelligence.

## Course Contents

### **Unit 1: Intelligent Agents, Graph Search, and Route Planning**

**Topics:**

1.1 Agents and environments  
1.2 State-space modeling  
1.3 Graph search algorithms  
1.4 Heuristic search with A* 

**Libraries:** `NetworkX`, `OSMnx`, `heapq`, `matplotlib`

**Datasets:** OpenStreetMap, campus transportation networks

**Slides:** 
[Intelligent Agents, Graph Search, and Route Planning](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%201.%20Intelligent%20Agents%2C%20Graph%20Search%2C%20and%20Route%20Planning/lecture0.key)

**Source Code:**
[Maze solving with BFS and DFS](https://github.com/eugeniomorocho/ArtificialIntelligence/tree/main/Unit%201.%20Intelligent%20Agents%2C%20Graph%20Search%2C%20and%20Route%20Planning/src0)

**Assignment:**
[Writing the Python code for A*](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%201.%20Intelligent%20Agents%2C%20Graph%20Search%2C%20and%20Route%20Planning/campus_route_planner_CHALLENGE.md)

---

### **Unit 2: Constraint Programming, Optimization, and Decision Support**

**Topics:**

Variables, domains, and constraints  
Backtracking and pruning  
Constraint propagation  
Scheduling and resource allocation  

**Libraries (optional):** `Google OR-Tools`

**Datasets:** University timetables, workforce scheduling datasets

**Notebooks:**

- [Constraint Programming and Scheduling](./Unit%202.%20Constraint%20Programming%2C%20Optimization%2C%20and%20Decision%20Support/Constraint%20Programming%20and%20Scheduling.ipynb)

---

### **Unit 3: Sequential Decision-Making and Reinforcement Learning**

**Topics:**

Markov decision processes  
Policies and value functions  
Exploration versus exploitation  
Q-learning  

**Libraries:** `NumPy`, `Gymnasium`, `Stable-Baselines3`

**Datasets:** Custom GridWorld environments, inventory-control simulations

**Notebooks:**

- [GridWorld and Q-Learning](./Unit%203.%20Sequential%20Decision-Making%20and%20Reinforcement%20Learning/GridWorld%20and%20Q-Learning.ipynb)

**Slides:**

- [Lecture 4 slides](./Unit%203.%20Sequential%20Decision-Making%20and%20Reinforcement%20Learning/lecture4.key), slides 67-96, from Harvard's CS50 course.

The remaining material and activity are self-contained in the notebook.

**References:**

- Harvard University, [CS50's Introduction to Artificial Intelligence with Python](https://cs50.harvard.edu/ai/), Lecture 4, slides 67-96.
- DeepLizard, [Reinforcement Learning Series Intro - Syllabus Overview](https://deeplizard.com/learn/video/nyjbcRQ-uQ8).
- Russell and Norvig, *Artificial Intelligence: A Modern Approach*, 4th edition, Chapters 17 (Sections 17.1 and 17.2.1) and 22 (Sections 22.1, 22.2.3, 22.3.1, and 22.3.3).

---

### **Unit 4: Probabilistic Reasoning and Bayesian Decision-Making**

**Topics:**

Conditional probability  
Bayes theorem  
Bayesian networks  
Inference under uncertainty  

**Libraries:** `pgmpy`, `scikit-learn`, `pandas`

**Datasets:** Medical-risk datasets, spam-classification datasets

**Notebooks:**

- [Bayes and Spam Decisions](./Unit%204.%20Probabilistic%20Reasoning%20and%20Bayesian%20Decision-Making/Bayes%20and%20Spam%20Decisions.ipynb)

The Unit 2–4 notebooks use only the Python standard library so students can focus on the AI ideas without setup. The libraries listed above are optional extensions for later work.

---

### **Unit 5: Machine Learning as an AI Component**

**Topics:**

Feature engineering  
Regression and classification   
Validation and leakage  
Explainability and error analysis  

**Libraries:** `scikit-learn`, `statsmodels`

**Datasets:** Medical Cost Personal Dataset, Housing datasets, Titanic, California Housing, Palmer Penguins, mall customers

**Notebooks:**

#### 5.1. Exploratory data analysis (EDA)

   ##### *Titanic*  
   [![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](./Unit%205.%20Machine%20Learning%20as%20an%20AI%20Component/5.1%20Exploratory%20data%20analysis/Test%20-%20An%C3%A1lisis%20exploratorio%20de%20datos%20del%20Titanic.ipynb)
   [![View on Canva](https://img.shields.io/badge/View%20on-Canva-7D2AE8?logo=canva&logoColor=white)](https://canva.link/bp75s8ta3pcf9mz)  

   - **Assignment 5.1**: Hipotesis testing and EDA on the Titanic dataset.

   ##### *California Housing Prices*  
   [![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](./Unit%205.%20Machine%20Learning%20as%20an%20AI%20Component/5.1%20Exploratory%20data%20analysis/Test%20-%20An%C3%A1lisis%20exploratorio%20con%20los%20datos%20de%20California%20Housing%20Prices.ipynb)

   - **Assignment 5.2**: EDA on the California Housing Prices dataset with Profile Report and quiz.
   
#### 5.2. Feature engineering

   *Handling outliers and group-wise operations (e-commerce)*  
   [![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](./Unit%205.%20Machine%20Learning%20as%20an%20AI%20Component/5.2%20Feature%20engineering/Test%20-%20Manejo%20de%20outliers%20y%20operaciones%20por%20grupo%20para%20transacciones%20e-commerce.ipynb)
   [![View on Canva](https://img.shields.io/badge/View%20on-Canva-7D2AE8?logo=canva&logoColor=white)](https://canva.link/e9he403kigpezsd) 

   *Feature scaling and normalization*  
   [![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](./Unit%205.%20Machine%20Learning%20as%20an%20AI%20Component/5.2%20Feature%20engineering/The%20importance%20of%20scaling%20and%20balancing%20data.ipynb)
   **Dataset:**  [UCI ML Wine Data Set](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_wine.html)

   - **Assignment 5.3**: Handling outliers and group-wise operations on e-commerce dataset. 

#### 5.3. Unsupervised learning

   $k$-Means customer segmentation  
   [![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](./Unit%205.%20Machine%20Learning%20as%20an%20AI%20Component/5.3%20Unsupervised%20learning/5.3.1%20k-Means/Unsupervised%20Learning%20-%20Agrupamiento%20de%20clientes%20de%20un%20centro%20comercial%20con%20KMeans.ipynb)
   [![View on Canva](https://img.shields.io/badge/View%20on-Canva-7D2AE8?logo=canva&logoColor=white)](https://canva.link/vlp33mhb137mnkl)  

   - **Assignment 5.4**: Search the optimal value of $k$ for $k$-Means clustering on a new dataset. Pick any database from [here](https://www.datosabiertos.gob.ec) (***presentation required***).

#### 5.4. Supervised learning

   *Classification*

   $k$-NN on the Iris dataset  
   [![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](./Unit%205.%20Machine%20Learning%20as%20an%20AI%20Component/5.4%20Supervised%20learning/5.4.1%20k-NN/IRIS%20Classification%20with%20k-NN.ipynb)
   [![View on Canva](https://img.shields.io/badge/View%20on-Canva-7D2AE8?logo=canva&logoColor=white)](https://canva.link/9rmsg0i4fiocn1d)  
   **Dataset:** [Iris](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html)  
   **Model:** [`KNeighborsClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html)

   - **Assignment 5.5**: $k$-NN on your database with the best hyperparameter value $k$ (***presentation required***).

Error analysis — evaluation metrics  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](./resources/miscellaneous/Metrics.ipynb)

Regression — linear regression to predict medical charges  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](./Unit%205.%20Machine%20Learning%20as%20an%20AI%20Component/5.4%20Supervised%20learning/5.4.2%20Linear%20Regressor/Supervised%20Learning%20-%20Regresi%C3%B3n%20lineal%20para%20predecir%20cargos%20m%C3%A9dicos.ipynb)

Classification — tree-based models  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](./resources/miscellaneous/Tree-based%20models.ipynb)

Classification — ensemble models  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](./resources/miscellaneous/Ensemble%20Models.ipynb)

Explainability — SHAP and LIME  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](./resources/miscellaneous/Explainable%20AI%20(SHAP%20and%20LIME).ipynb)

Assignment 5.1 (Titanic): 1pt  
Assignment 5.2 (California + quiz): 2pt  
Assignment 5.3 (e-commerce): 1pt  
Assignment 5.4 (k-Means presentation): 3pts  
Assignment 5.5 (k-NN presentation): 3pts

---

### **Unit 6: Neural Models, Vision, and Foundation Models**

**Topics:**

Perceptrons and neural networks  
CNN fundamentals  
Transfer learning  
Foundation-model overview  

**Libraries:** `TensorFlow`, `Keras`, `OpenCV`

**Datasets:** CIFAR-10, custom image datasets, Breast Cancer Wisconsin, Palmer Penguins, diabetes dataset

**Notebooks:**  

#### 6.1. Predicting penguin species with an MLP + MS Excel inference  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%206.%20Neural%20Models%2C%20Vision%2C%20and%20Foundation%20Models/6.1%20Multi-layer%20Perceptron%20(MLP)/MLP_Classification_Pipeline_and_Excel.ipynb)
[![View on Canva](https://img.shields.io/badge/View%20on-Canva-7D2AE8?logo=canva&logoColor=white)](https://canva.link/ae2wihvl91llh5k)  
**Dataset:**  [Palmer Penguins](https://github.com/allisonhorst/palmerpenguins)  
**Model:** [`MLPClassifier`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html)

#### 6.2. Predicting diabetes with a Keras' sequential Neural Network + TensorBoard  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](./Unit%206.%20Neural%20Models%2C%20Vision%2C%20and%20Foundation%20Models/6.2%20The%20Sequential%20Model%20(Neural%20Network)/Predicting%20diabetes%20with%20a%20Keras%20NN.ipynb)
[![View on Canva](https://img.shields.io/badge/View%20on-Canva-7D2AE8?logo=canva&logoColor=white)](https://canva.link/3rm32wsg6q369no)  
**Dataset:**  [Pima Indians Diabetes](https://github.com/allisonhorst/palmerpenguins)  
**Model, Callbacks and Optimizers:** [`The Sequential model (Keras)`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html), [`TensorBoard`](https://www.tensorflow.org/tensorboard), [`EarlyStopping`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/EarlyStopping), [`Keras Tuner`](https://keras.io/keras_tuner/)

#### 6.3. Classifying Cats and Dogs images with a CNN + Transfer learning  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%206.%20Neural%20Models%2C%20Vision%2C%20and%20Foundation%20Models/6.3%20Convolutional%20Neural%20Networks%20(CNN)/6.3.1%20Image%20classification/Dogs%20vs.%20Cats%20Image%20Classification%20with%20VGG16.ipynb) 
[![View on Canva](https://img.shields.io/badge/View%20on-Canva-7D2AE8?logo=canva&logoColor=white)](https://canva.link/vwl4ht1uqlcpv64)  
**Dataset:**  [Microsoft Cats and Dogs](https://www.microsoft.com/en-us/download/details.aspx?id=54765)  
**Model, Callbacks and Optimizers:** [`The Sequential model (Keras)`](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html), [`VGG16 function`](https://keras.io/api/applications/vgg/#vgg16-function), [`EarlyStopping`](https://www.tensorflow.org/api_docs/python/tf/keras/callbacks/EarlyStopping), [Dropout Layer](https://keras.io/api/layers/regularization_layers/dropout/)


Assignment 6.1 (MLP + Excel): 4pt    
Assignment 6.3 (CNN + Transfer learning): 6pts  

---

### **Unit 7: LLMs, Retrieval, and AI Safety**

**Topics:**

Embeddings  
Semantic search  
Retrieval-Augmented Generation (RAG)  
AI safety and hallucinations  

**Libraries:** `Sentence Transformers`, `FAISS`, `Streamlit`

**Datasets:** Course notebooks, technical-document repositories

**Notebooks:**

*Coming soon.*

---

### **Unit 8: Market-Ready AI Prototype and Final Project**

**Topics:**

Problem formulation  
Dataset and model selection  
Reproducible experimentation  
Deployment and technical communication  

**Libraries:** `Streamlit`, `FastAPI`, `MLflow`, `Gradio`

**Datasets:** Student-selected project datasets

**Notebooks:**

*Coming soon.*

---

## Support and Feedback

If you encounter any issues or have suggestions for improvement, please [open an issue](https://github.com/eugeniomorocho/ArtificialIntelligence/issues). We appreciate your feedback!

---

## Bibliography

### Primary Books

[1] Russell, S., & Norvig, P. (2022). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson. https://aima.cs.berkeley.edu/

[2] Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning* (1st ed.). The MIT Press. https://www.deeplearningbook.org

[3] Géron, A. (2023). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O'Reilly Media. https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/

### Complementary Books

[4] Sutton, R. S., & Barto, A. G. (2018). *Reinforcement Learning: An Introduction* (2nd ed.). The MIT Press. http://incompleteideas.net/book/the-book-2nd.html

[5] Koller, D., & Friedman, N. (2009). *Probabilistic Graphical Models: Principles and Techniques*. The MIT Press. https://mitpress.mit.edu/9780262013192/probabilistic-graphical-models/

### Online Resources

[6] [AIMA Python code repository](https://github.com/aimacode/aima-python)

[7] [Gymnasium Documentation](https://gymnasium.farama.org)

[8] [Google OR-Tools Documentation](https://developers.google.com/optimization)

[9] [pgmpy Documentation](https://pgmpy.org)

Wed 7, 2026 - Unit 4
Fri 9, 2026 - Holiday
Wed 14, 2026 - Midterm Exam
Fri 16, 2026 - TICEC2026
Wed 21, 2026 - Project Proposal Presentation 1
Fri 23, 2026 - Project Proposal Presentation 2

---
<br>
<p style="text-align: right; font-size:14px; color:gray;">
<b>Prepared by:</b><br>
Manuel Eugenio Morocho-Cayamcela, Ph.D.
</p>