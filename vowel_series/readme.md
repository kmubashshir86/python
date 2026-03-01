# 🔢 Vowel Number Representation Function

## 📌 Alphabet Numbering Rule

We assign numbers to English alphabets as:

A = 1  
B = 2  
C = 3  
...  
Z = 26  

---

## 🎯 Vowel Generating Function

The vowels (A, E, I, O, U) can be generated using the function:

f(n) = 64 + (2n² + 8n − 5 + (−1)ⁿ) / 4

Where:

n represents the vowel index.

n = 1 → A  
n = 2 → E  
n = 3 → I  
n = 4 → O  
n = 5 → U  

---

## 📍 Domain

The function is defined only for:

Domain = {1, 2, 3, 4, 5}

---

## 📈 Range

For the above domain values, the function produces:

Range = {65, 69, 73, 79, 85}

These are the ASCII values of uppercase vowels:

65 → A  
69 → E  
73 → I  
79 → O  
85 → U  

---

## ✅ Final Summary

• Alphabet numbering: A = 1 to Z = 26  
• The function generates ASCII values of vowels  
• Domain: finite set {1,2,3,4,5}  
• Range: {65,69,73,79,85}  

Now it looks clean and readable in GitHub markdown 😎
