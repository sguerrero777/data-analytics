# Week 10 - Exercise 2.A: DAX Function Reference Reflection
### Sharleen Guerrero

## What is DAX?

**DAX (Data Analysis Expressions)** runs *after* data is already in the model. It is used for measures, calculated columns, and analysis (totals, percentages, averages, ratios).

 M is for cleaning, shaping, and loading. DAX is for measures, calculations, and analysis.

---

## Reflection Questions

### 1. What aggregation functions have I used in SQL or Python? What equivalents appear in DAX?

> I have used SUM, AVG, COUNT, COUNTA, MIN, and MAX with pandas and SQL.

DAX uses the exact same names: `SUM()`, `AVERAGE()`, `COUNT()`, `COUNTA()`, `MIN()`, `MAX()`. The only quirk is DAX uses `AVERAGE()` instead of `AVG()`.

---

### 2. What text functions have I used in SQL or Python? What equivalents appear in DAX?

> UPPER, PROPER, TRIM

DAX has those exact same functions: `UPPER()`, `PROPER()`, `TRIM()`. Same names, same behavior. DAX text functions are almost identical to Excel's because that is who Microsoft designed for.

---

### 3. What can I do with "information functions"? How about "logical functions"?

**Information functions** ask "what is this value?" Examples: `ISERROR()`, `ISBLANK()`, `ISNUMBER()`, `ISTEXT()`.

**Logical functions** ask "is this condition true or false, and what should I do about it?" Examples: `IF()`, `AND()`, `OR()`, `SWITCH()`.

---

##  Clarifty: Information vs Logical Functions

At first I thought information and logical functions were similar because both looked like boolean indexing.

The difference:
- **Information functions** check *what* a value is (diagnostic)
- **Logical functions** decide *what to do* about it (decision-maker)

In practice, information functions are used **inside** logical functions:

`IF(ISBLANK([Discount]), 0, [Discount])`

> My interpretation: if discount is blank, put a 0 in the discount column.

`ISBLANK` checks if Discount is blank, and `IF` decides what to return based on that check. They work together.

---

## Key Takeaways

- M runs before the model, DAX runs inside the model
- DAX aggregation and text function names match SQL/pandas almost exactly
- Information functions check what a value is, logical functions decide what to do about it
- They are commonly nested together