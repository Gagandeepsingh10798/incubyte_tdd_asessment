# 🧮 String Calculator – TDD Kata (Python)

This project is a solution to the **String Calculator TDD Assignment**, implemented in **Python** using **Object-Oriented Programming** principles and a strict **Test-Driven Development (TDD)** workflow.

---

## 🧠 About the Project

The goal of this kata is to demonstrate mastery in:

- ✅ Writing clean and maintainable object-oriented code  
- ✅ Practicing TDD (Red → Green → Refactor)  
- ✅ Making incremental, test-driven commits  
- ✅ Covering a wide range of edge cases and specifications  

---

## 🚀 Features Implemented

| Step | Feature                                                                 | Status |
|------|-------------------------------------------------------------------------|--------|
| 1    | Return `0` for an empty string                                          | ✅     |
| 2    | Return number for a single value (`"1"` → `1`)                          | ✅     |
| 3    | Add two comma-separated numbers (`"1,2"` → `3`)                         | ✅     |
| 4    | Handle multiple numbers (`"1,2,3"` → `6`)                               | ✅     |
| 5    | Allow newline `\n` as a delimiter (`"1\n2,3"` → `6`)                    | ✅     |
| 6    | Allow custom delimiter (`"//;\n1;2"` → `3`)                             | ✅     |
| 7    | Raise exception on negative numbers with full list of negatives        | ✅     |
| 8    | Ignore numbers > 1000 (`"2,1001"` → `2`)                                | ✅     |
| 9    | Support delimiters of any length (`"//[***]\n1***2***3"` → `6`)        | ✅     |
| 10   | Support multiple single-char delimiters (`"//[*][%]\n1*2%3"` → `6`)    | ✅     |
| 11   | Support multi-length delimiters (`"//[***][%%]\n1***2%%3"` → `6`)      | ✅     |
