# 🧮 Expression Calculator

---

## 📌 Overview
The **Expression Calculator** is a Python program that evaluates mathematical expressions.  
It uses the **Shunting Yard Algorithm** to convert expressions from **infix notation** (e.g., `3 + 4 * 2`) to **postfix notation (RPN)**, and then evaluates the postfix using a **stack**.  

This project demonstrates **stack operations, parsing, operator precedence, and associativity**.

---

## 🛠️ Features
- Convert **Infix ➜ Postfix** expressions
- Evaluate **Postfix (RPN)** expressions
- Supports operators: `+  -  *  /  ^`
- Correctly handles **parentheses** and **operator precedence**
- Works with both integers and floating-point numbers
- Error handling for:
  - Invalid tokens  
  - Mismatched parentheses  
  - Insufficient operands  
  - Division by zero  

---

## 📂 Data Structures & Concepts Used
- **Stack (list as stack)**  
  - For operators (in infix ➜ postfix conversion)  
  - For operands (in postfix evaluation)  
- **Array (list)** → Store tokens & postfix output  
- **Dictionary (map)** → Operator metadata (precedence, associativity, evaluation function)  
- **String parsing** → Tokenizer for numbers, operators, parentheses  

---

## 🧠 Core Algorithms
1. **Tokenization**  
   - Breaks input expression into tokens (numbers, operators, parentheses).  

2. **Infix ➜ Postfix (Shunting Yard Algorithm)**  
   - Uses precedence & associativity to arrange operators.  
   - Handles parentheses correctly.  

3. **Postfix Evaluation**  
   - Traverse postfix expression.  
   - Push numbers to stack.  
   - On operator, pop operands, apply operation, push result.  
   - Final stack value = result.  

---

## ➕ Operator Precedence & Associativity
- `^` → Precedence 4, **Right-Associative**  
- `* /` → Precedence 3, Left-Associative  
- `+ -` → Precedence 2, Left-Associative  
- `( )` → Grouping only  

---

## ✅ Example Runs
**Input:**  
`3 + 4 * 2 / (1 - 5) ^ 2 ^ 3`  

**Postfix:**  
`3 4 2 * 1 5 - 2 3 ^ ^ / +`  

**Result:**  
`3.0001220703125`  

---

## ⚠️ Error Handling
- Mismatched parentheses → `ValueError("Mismatched parentheses")`  
- Invalid tokens → `ValueError("Invalid token: ?")`  
- Division by zero → `ZeroDivisionError`  
- Insufficient operands → `ValueError("Insufficient values")`  

---

## 🧩 Technology Requirements
- **Python 3**  
- **Stack-based infix-to-postfix conversion**  
- **Postfix evaluation using stack**  
- **Math module (for power function)**  

---

