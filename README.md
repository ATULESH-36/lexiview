# 📊 Lexical Complexity Analysis using TTR Variants

##  Overview

This project analyzes the **lexical complexity of text** using multiple variants of the **Type-Token Ratio (TTR)** and provides **interpretable explanations** instead of rigid classifications.

Unlike traditional approaches that assign labels like *low/medium/high*, this system focuses on **understanding and explaining** the richness and consistency of vocabulary in a given text.

---

## Key Features

* ✅ Text preprocessing (cleaning, tokenization, stopword removal)
* ✅ Multiple lexical metrics:

  * TTR (Type-Token Ratio)
  * MATTR (Moving Average TTR)
  * Rare Word TTR
* ✅ Custom **Lexical Richness Index (LRI)**
* ✅ **Explainable output** instead of black-box classification
* ✅ Handles short text edge cases

---

## 📐 Metrics Used

### 1. TTR (Type-Token Ratio)

Measures lexical diversity:

```
TTR = unique_words / total_words
```

---

### 2. MATTR (Moving Average TTR)

Provides a more stable measure of vocabulary richness using a sliding window.

---

### 3. Rare Word TTR

Captures the presence of less frequent (informative) words.

---

### 4. LRI (Lexical Richness Index)

A weighted combination of all metrics:

```
LRI = 0.6 * MATTR + 0.25 * TTR + 0.15 * RW-TTR
```

---

## 🧾 Example Output

```
Lexical Complexity Analysis:

- TTR: 0.41 → low lexical diversity (repetition present)
- MATTR: 0.61 → moderate consistency in vocabulary usage
- RW-TTR: 0.80 → strong presence of rare words

Overall Interpretation:
The text exhibits repetition, but maintains a degree of consistency in vocabulary usage.
```

---

## ⚙️ Installation

```bash
git clone https://github.com/ATULESH-36/TTR_NLP.git
cd TTR_NLP
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the main script:

```bash
python main.py
```

Enter any custom text and get a full lexical analysis.

---

## 📂 Project Structure

* `src/` → Core logic (preprocessing, metrics, analysis)
* `notebooks/` → Exploratory analysis & visualization
* `data/` → Raw and cleaned datasets
* `results/` → Plots and outputs

---

## 💡 Key Insight

Instead of forcing classification, this project focuses on:

> **“Explaining lexical complexity rather than labeling it.”**

---

## 🚀 Future Improvements

* Add visualization dashboard (Streamlit)
* Improve rare word detection using frequency corpus
* Add readability metrics (Flesch, etc.)
* Deploy as a web app

---

## 👨‍💻 Author

Atulesh Sahoo
