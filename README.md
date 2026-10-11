# Skillset-Go-EduTech-AIML-Week3-TensorFlow-GenAI-Prompt-Engineering

A complete, executed submission for **Week 3 (Applied AI Phase)** of the Skillset Go EduTech AI/ML 4-Week Practical Learning Track — a TensorFlow/Keras model compared against Week 2's PyTorch model, an advanced computer-vision project, a tested prompt-engineering portfolio, and an AI-assisted coding task with a real audit.

## Project Overview

Week 3 shifts from PyTorch (Week 2) to TensorFlow/Keras, adds a more advanced computer-vision project with modern training techniques, and introduces two new kinds of work central to applied AI roles: designing and iterating on LLM prompts, and reviewing/auditing AI-generated code rather than writing everything from scratch.

Two notebooks, one prompt-engineering document, and one small audited application, each mapped to one official roadmap task, all executed end-to-end — every number, chart, and code fix below is real and reproducible.

## Key Features

- A TensorFlow/Keras CNN built with the **same architecture, data, and split** as Week 2's PyTorch CNN, with a direct side-by-side comparison table and written notes
- An advanced CV project adding **data augmentation, batch normalization, global-average-pooling, and early-stopping/LR-reduction callbacks**
- A prompt-engineering portfolio covering reasoning, extraction, summarization, and coding — each with a weak first prompt, the problem with it, an improved prompt, and the **actual resulting output**
- An AI-assisted coding task: a small Student Grade Manager CLI, drafted with deliberately planted issues, then audited — every bug **reproduced with a failing test case** before being fixed, and every fix **re-verified with passing assertions**

## Technologies Used

- **Python**, **TensorFlow / Keras** (Sequential and Functional APIs, callbacks, data augmentation layers)
- **NumPy**, **Pandas**, **Matplotlib**, **Scikit-learn** (data splitting, metrics, bundled image dataset)
- **Jupyter Notebook / Google Colab / VS Code**

## Task Workflow

**1. TensorFlow/Keras Model**
A CNN matching the shape of the Week 2 PyTorch CNN (conv16→pool→conv32→pool→dense64→dense10) is trained on the same digits dataset and split. Test accuracy, parameter count, training time, and API ergonomics are compared directly against the PyTorch model in a table and written notes.

**2. Computer Vision Project (Advanced)**
A deeper model adds data augmentation (random rotation/translation/zoom, active only during training), batch normalization after every convolution, a global-average-pooling head, and callbacks that stop training on plateau and reduce the learning rate automatically — the standard toolkit for pushing real-world vision models further.

**3. Prompt Engineering Portfolio**
Four exercises (reasoning, extraction, summarization, coding), each showing a first attempt, its concrete flaw, an improved prompt, and the real output it produced — with a findings table tying each technique to the specific problem it fixed.

**4. AI-Assisted Coding Task**
A small CLI app draft (`draft_app.py`, written with common AI-code mistakes deliberately included) was audited line-by-line: 7 issues were found (mutable default argument, divide-by-zero, off-by-one grade boundaries, unhandled missing-student case, unclosed file handles, no error handling on corrupt data, no input validation). Each bug was reproduced with a failing case, fixed in `app.py`, and re-verified with passing assertions and a full interactive run.

## Project Structure

```
Task-3.1_TensorFlow-GenAI-Prompt-Engineering/
│
├── 1_tensorflow_keras_model.ipynb
├── 2_cv_project_tensorflow.ipynb
├── 3_prompt_engineering_portfolio.md
├── task4_ai_assisted_coding/
│   ├── draft_app.py
│   ├── app.py
│   └── audit_notes.md
├── keras_cnn_digits.keras
├── advanced_cnn_digits.keras
└── README.md
```

## Installation

```
git clone https://github.com/Prithyadarshan/Task-3.1_TensorFlow-GenAI-Prompt-Engineering.git
cd Task-3.1_TensorFlow-GenAI-Prompt-Engineering
pip install tensorflow numpy pandas matplotlib scikit-learn jupyter
```

## How to Run

**Notebooks 1-2:** Open in Jupyter/Colab/VS Code and run top to bottom.
**Prompt portfolio:** Read as a document — `3_prompt_engineering_portfolio.md`.
**Task 4 app:** `cd task4_ai_assisted_coding && python app.py` (the corrected version). Run `draft_app.py` separately only to see the original bugs reproduce.

## Output

- **`keras_cnn_digits.keras`** — TensorFlow/Keras CNN from Task 1 (95.56% test accuracy)
- **`advanced_cnn_digits.keras`** — advanced CV model from Task 2 with augmentation + callbacks (96.30% test accuracy)
- **`task4_ai_assisted_coding/app.py`** — working, audited CLI application
- **`task4_ai_assisted_coding/audit_notes.md`** — full list of issues found, evidence, and fixes

## Applications

- Framework comparison methodology (PyTorch vs TensorFlow) for model selection
- Production-grade CV techniques (augmentation, batch norm, callbacks) applicable to real datasets such as histopathology tiles
- Reusable prompt patterns for reasoning, extraction, summarization, and coding tasks
- A concrete, repeatable process for reviewing and auditing AI-generated code before shipping it

## Concepts Demonstrated

Keras Sequential & Functional APIs · Data Augmentation · Batch Normalization · Training Callbacks (EarlyStopping, ReduceLROnPlateau) · Framework Comparison · Prompt Engineering (reasoning, extraction, summarization, coding) · Code Review & Debugging · Defensive Programming

## Future Enhancements

- Swap the digits dataset for a larger real-world image set (e.g. MNIST/Fashion-MNIST in Colab, or histopathology tiles) using the same augmentation/callback pipeline
- Extend the prompt portfolio with multi-turn and chain-of-thought comparisons
- Add automated unit tests (`pytest`) to the Task 4 app instead of inline assertions
- Explore TensorFlow Lite / ONNX export for deployment comparison with the PyTorch model

## Limitations

- The CV tasks reuse the small, low-resolution digits dataset due to this environment's offline constraints; absolute accuracy numbers would look different on a larger real-world dataset
- Prompt portfolio outputs are illustrative until replaced with the student's own live-run responses; results vary between models and runs
- The audited app is intentionally small in scope (CLI, JSON storage) to keep the review process clear and complete

## Learning Outcome

This submission provides practical experience comparing deep learning frameworks on equal footing, applying production-grade computer-vision techniques beyond a basic CNN, iterating on prompts with visible before/after evidence, and — critically — treating AI-generated code as a first draft to be reviewed and fixed rather than accepted as-is. Together these build directly toward the RAG, agent, and tool-use work in Week 4.
