# Midterm Project Proposal — Research Project

The final project of this course will be developed as a **research paper**. The goal of this proposal is to define the research problem, review the existing literature, design the methodology, and demonstrate that the proposed project is feasible before developing the complete study.

Your project may use **any Artificial Intelligence topic**, including topics that we have not covered in class yet.

You may also combine this project with a problem or topic from **another course you are currently taking**. In this case:

- Clearly identify the other course and instructor.
- Explain the connection between both courses.
- Obtain permission from the other instructor.
- The work submitted to this course must clearly address an **Artificial Intelligence research question**.

If you do not have a project idea, you may select **Project 1, 2, or 4** from:

https://www.deeparcresearch.com/open-projects

---

## 1. Research Problem

Clearly define:

- The problem you want to solve.
- Why the problem is relevant.
- The main **research question**.
- The objective of the study.
- The expected contribution.

The problem should be specific enough to be experimentally evaluated.

---

## 2. Type of Research

Choose one of the following:

### Applied Research

Apply and evaluate AI methods to solve a specific real-world problem.

You must identify an appropriate **benchmark or baseline** and experimentally compare your proposed solution against it.

### Fundamental Research

Investigate or improve an AI method, algorithm, architecture, representation, or methodology.

You must clearly identify the **new contribution** and experimentally evaluate whether it provides an improvement or new insight.

---

## 3. Literature Review

Review relevant scientific literature related to your problem.

Your literature review must identify:

- What has already been done.
- What AI methods have been used.
- How previous studies evaluated their solutions.
- What results have been reported.
- What limitations or open problems remain.
- Which previous method/result will be used as your **benchmark or baseline**.

Include a comparison table similar to:

| Reference | Main Idea / Problem | Model / Algorithm | Dataset | Metric(s) | Main Result(s) | Limitation(s) |
|---|---|---|---|---|---|---|
| [1] | ... | ... | ... | ... | ... | ... |
| [2] | ... | ... | ... | ... | ... | ... |

The literature review should justify your research problem and the experimental decisions you make later.

Use **scientific publications** as the main sources. Do not use blogs, tutorials, or AI-generated text as substitutes for the scientific literature. Your submission will be checked with plagiarism detection tools and AI generated content detectors; so you must properly cite all sources.

---

## 4. Proposed Methodology

Describe the complete methodology you plan to implement.

Include:

- Dataset / data source.
- Inputs and outputs.
- Data preprocessing.
- AI model(s) or algorithm(s).
- Training or optimization procedure, when applicable.
- Baseline / benchmark.
- Experimental setup.
- Evaluation metric(s).
- Validation or testing strategy.
- Software, libraries, or tools you expect to use.

### System Diagram

Include a diagram showing the complete proposed system.

The diagram should make clear:

**Input → Processing / AI Method → Evaluation → Output**

Include the main data flows, models, algorithms, and evaluation stages.

**The system diagram must be designed by you and must NOT be generated using AI.**

You may use tools such as draw.io, PowerPoint, Canva, Figma, or similar tools to create it.

You must be able to explain every component of the diagram.

---

## 5. Benchmark and Evaluation

Clearly identify what your proposed method will be compared against.

The benchmark may come from:

- A method reported in the literature.
- A standard baseline algorithm.
- An existing implementation.
- A simpler model implemented by you.

Define the metric(s) that will be used for the comparison.

Examples include:

- Accuracy
- Precision / Recall / F1-score
- MAE / RMSE
- IoU / mAP
- BLEU / ROUGE
- Reward / cumulative reward
- Runtime / computational cost
- Other metrics appropriate to the research problem

The selected metric must be appropriate for the problem and justified using the literature.

---

## 6. Preliminary Results

The proposal must contain **real preliminary experimental results**.

The purpose is to demonstrate that:

1. The dataset can be obtained and processed.
2. The proposed implementation is technically feasible.
3. At least one baseline or initial model can run.
4. The selected evaluation metric can be calculated.

These do **not** need to be your final results.

Examples:

- A baseline model successfully trained and evaluated.
- An initial classification or regression result.
- A working reinforcement-learning environment.
- A first optimization result.
- A working retrieval pipeline.
- A preliminary computer-vision model.
- A small experiment on a subset of the final dataset.

Include at least one result as a **table, figure, or quantitative metric** and briefly interpret it.

Do not report expected or invented values as preliminary results.

---

## 7. Reproducibility

Create a **GitHub repository** for the project.

The repository should progressively contain:

- `README.md`
- Source code / notebooks
- `requirements.txt` or equivalent environment specification
- Instructions to reproduce the experiments
- Dataset or instructions/links to obtain it
- Experimental configuration
- Results and figures

Another person should eventually be able to reproduce the reported results using the repository.

Do not upload private, restricted, or confidential datasets to a public repository.

---

## 8. Paper Format

Write the proposal using the **MDPI research article format**.

At this stage, the document should contain at least:

1. **Title**
2. **Abstract**
3. **Keywords**
4. **Introduction**
5. **Related Work / Literature Review**
6. **Materials and Methods**
7. **Preliminary Results**
8. **Discussion / Expected Research Direction**
9. **References**

The proposal will later evolve into the **Final Project research paper**, so write it as the first version of the paper rather than as a separate report.

---

## 9. Submission

Submit:

- Research proposal in **MDPI format**.
- Link to the corresponding **GitHub repository**.

**No slides are required for the presentation.**

The repository and paper must correspond to each other, and the preliminary results reported in the paper must be reproducible from the submitted code.

---

## 10. Final Project

After receiving feedback on the proposal, you will continue the experiments and transform the proposal into the final research paper.

For the final version you will be expected to:

- Complete the proposed methodology.
- Perform the complete experimental evaluation.
- Compare the results with the selected benchmark(s).
- Analyze the results and failure cases.
- Discuss limitations.
- Document the complete reproducible implementation.
- Clearly identify your contribution.

Selected papers may undergo **external peer review** and may be prepared for submission to an appropriate scientific journal or conference.

Therefore, treat the project as a **real research study**, not only as a course assignment.

---

## Important

A complex model is **not** automatically a good research project.

A good project has:

**A clear problem + relevant literature + a justified baseline + a reproducible methodology + appropriate metrics + experimental evidence + a clear contribution.**

You must understand and be able to explain every component of your project, including the code, methodology, diagram, experiments, and results.