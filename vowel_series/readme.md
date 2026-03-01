# 🔢 Vowel Number Representation Function

## 📌 Alphabet Numbering Rule

We assign numbers to English alphabets as:

- A = 1  
- B = 2  
- C = 3  
- ...  
- Z = 26  

So each letter corresponds to its position in the English alphabet.

---

## 🎯 Special Case: Vowel Number Formula

The vowels are:

A, E, I, O, U

Their alphabet positions are:

| Vowel | Position |
|--------|----------|
| A      | 1        |
| E      | 5        |
| I      | 9        |
| O      | 15       |
| U      | 21       |

These values can be generated using the function:

\[
f(n) = 64 + \frac{2n^2 + 8n - 5 + (-1)^n}{4}
\]

---

## 🧮 Function Definition

\[
f(n) = 64 + \frac{2n^2 + 8n - 5 + (-1)^n}{4}
\]

Where:

- `n` represents the vowel index  
- n = 1 → A  
- n = 2 → E  
- n = 3 → I  
- n = 4 → O  
- n = 5 → U  

---

## 📍 Domain

\[
\text{Domain} = \{1, 2, 3, 4, 5\}
\]

---

## 📈 Range

\[
\text{Range} = \{65, 69, 73, 79, 85\}
\]

These correspond to ASCII values of vowels:

| Letter | ASCII |
|--------|--------|
| A      | 65     |
| E      | 69     |
| I      | 73     |
| O      | 79     |
| U      | 85     |

---

## ✅ Summary

- Letters are numbered from **1 to 26**
- Vowel positions follow a specific quadratic pattern
- The function generates ASCII values of uppercase vowels
- The formula works only for `n ∈ {1,2,3,4,5}`

---

✨ Mathematical patterns can beautifully describe language structure!
