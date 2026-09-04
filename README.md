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

**Libraries:** `Google OR-Tools`

**Datasets:** University timetables, workforce scheduling datasets

**Notebooks:**

*Coming soon.*

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

*Coming soon.*

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

*Coming soon.*

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

1. Exploratory Data Analysis

   *Titanic*  
   [![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/1.%20Exploratory%20data%20analysis%20(EDA)/Test%20-%20Análisis%20exploratorio%20de%20datos%20del%20Titanic.ipynb)
   [![View on Canva](https://img.shields.io/badge/View%20on-Canva-7D2AE8?logo=canva&logoColor=white)](https://canva.link/bp75s8ta3pcf9mz) 

   - **Assignment 5.1**: Hipotesis testing and EDA on the Titanic dataset.

   *California Housing Prices*  
   [![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/1.%20Exploratory%20data%20analysis%20(EDA)/Test%20-%20Análisis%20exploratorio%20con%20los%20datos%20de%20California%20Housing%20Prices.ipynb)

   - **Assignment 5.2**: EDA on the California Housing Prices dataset with Profile Report and solved [quiz](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/1.%20Exploratory%20data%20analysis%20(EDA)/Quiz%20(Data%20Profiler).docx).

2. Feature engineering

   *Handling outliers and group-wise operations (e-commerce)*  
   [![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/2.%20Data%20pre-processing/Test%20-%20Manejo%20de%20outliers%20y%20operaciones%20por%20grupo%20para%20transacciones%20e-commerce.ipynb)
   [![View on Canva](https://img.shields.io/badge/View%20on-Canva-7D2AE8?logo=canva&logoColor=white)](https://canva.link/e9he403kigpezsd) 

   - **Assignment 5.3**: Handling outliers and group-wise operations on e-commerce dataset. (***presentation required***)

3. Unsupervised Learning

   $k$-Means customer segmentation  
   [![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%205.%20Machine%20Learning%20as%20an%20AI%20Component/5.3%20Unsupervised%20Learning/Clustering%20Mall%20Customers%20with%20KMeans.ipynb)
   [![View on Canva](https://img.shields.io/badge/View%20on-Canva-7D2AE8?logo=canva&logoColor=white)](https://canva.link/vlp33mhb137mnkl)  

   - **Assignment 5.4**: Search the optimal value of $k$ for $k$-Means clustering on a new dataset. (***presentation required***)

4. Supervised Learning

   *Classification*

   $k$-NN on the Iris dataset  
   [![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%205.%20Machine%20Learning%20as%20an%20AI%20Component/5.4%20Supervised%20Learning/IRIS%20Classification%20with%20kNN.ipynb)
   [![View on Canva](https://img.shields.io/badge/View%20on-Canva-7D2AE8?logo=canva&logoColor=white)](https://canva.link/9rmsg0i4fiocn1d) 

   - **Assignment 5.5**: $k$-NN on your database with the best hyperparameter value $k$.

5. Feature engineering — scaling, balancing, and normalizing data  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%205.%20Machine%20Learning%20as%20an%20AI%20Component/Lecture%20-%20The%20importance%20of%20scaling%2C%20balancing%2C%20and%20normalizing%20data.ipynb)

- **Assignment 5.6**: Optimal sampling strategy on a new database.

6. Regression — linear regression to predict medical charges  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%205.%20Machine%20Learning%20as%20an%20AI%20Component/Supervised%20Learning%20-%20Regresi%C3%B3n%20lineal%20para%20predecir%20cargos%20m%C3%A9dicos.ipynb)

7. Classification — tree-based models  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%205.%20Machine%20Learning%20as%20an%20AI%20Component/Tree-based%20models.ipynb)

8. Classification — ensemble models  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%205.%20Machine%20Learning%20as%20an%20AI%20Component/Ensemble%20Models.ipynb)

9. Validation — hyperparameter search (grid and random search)  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%205.%20Machine%20Learning%20as%20an%20AI%20Component/Hyperparameter%20search%20(grid%20and%20random%20search).ipynb)

10. Error analysis — evaluation metrics  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%205.%20Machine%20Learning%20as%20an%20AI%20Component/Metrics.ipynb)

11. Explainability — SHAP and LIME  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%205.%20Machine%20Learning%20as%20an%20AI%20Component/Explainable%20AI%20(SHAP%20and%20LIME).ipynb)

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

1. MLP classifier fundamentals  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%206.%20Neural%20Models%2C%20Vision%2C%20and%20Foundation%20Models/MLPClassifier.ipynb)

2. MLP classifier — Breast Cancer Wisconsin  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%206.%20Neural%20Models%2C%20Vision%2C%20and%20Foundation%20Models/MLPClassifier%20-%20Breast%20Cancer%20Wisconsin.ipynb)

3. Neural network — diabetes prediction  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%206.%20Neural%20Models%2C%20Vision%2C%20and%20Foundation%20Models/Lectura%20-%20Predicci%C3%B3n%20de%20diabetes%20con%20una%20red%20neuronal.ipynb)

4. Activation functions  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%206.%20Neural%20Models%2C%20Vision%2C%20and%20Foundation%20Models/Activation%20Functions.ipynb)

5. Test — Palmer Penguins classification with an MLP  
[![Open in GitHub](https://img.shields.io/badge/Open%20in-GitHub-181717?logo=github)](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%206.%20Neural%20Models%2C%20Vision%2C%20and%20Foundation%20Models/Test%20-%20Clasificaci%C3%B3n%20de%20pinguinos%20de%20la%20Isla%20Palmer%20con%20un%20MLP.ipynb) · [Solution](https://github.com/eugeniomorocho/ArtificialIntelligence/blob/main/Unit%206.%20Neural%20Models%2C%20Vision%2C%20and%20Foundation%20Models/Test%20solution%20-%20Clasificaci%C3%B3n%20de%20pinguinos%20de%20la%20Isla%20Palmer%20con%20un%20MLP.ipynb)

*CNN fundamentals, transfer learning, and foundation-model labs coming soon.*

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

---
<br>
<p style="text-align: right; font-size:14px; color:gray;">
<b>Prepared by:</b><br>
Manuel Eugenio Morocho-Cayamcela, Ph.D.
</p>