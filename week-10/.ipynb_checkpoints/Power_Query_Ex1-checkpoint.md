# Power Query EX 1 — Reflections
### Sharleen Guerrero | June 11, 2026

---

## Section A | Data Quality Observations

**Question 1: What data quality issues did you identify during the profiling step (Task 2)?**  

OrderDate shows 0 errors and 100% valid. The dates appear clean in the preview. This is likely because Power Query's "Changed column type" step was auto-applied when the file loaded, which resolved the mixed formats before profiling even ran.

---

**Question 2: Which column(s) show duplicate values in the top rows of the preview?**

The column showing a data quality duplicate is **OrderID** — 51 rows but only 50 distinct values means one OrderID appears twice, which is a problem since every order should have a unique identifier. The other columns (CustomerName, Product, Category, Region, Quantity, UnitPrice, Discount, SalesRep) show repeated values, but that is expected for categorical columns in a sales dataset — one sales rep handles many orders, one product can sell many times. Those are normal one-to-many patterns, not data quality issues.

---

**Question 3: What percentage of rows are valid in the OrderID column?**

OrderID shows **100% valid** in Column Quality. However, valid does not mean unique — Power Query does not flag duplicates as errors. The duplicate was only visible by comparing the Count (51) against Distinct (50) in the Column Statistics pane, which showed one OrderID appearing twice.

---

## Section B | Power Query Transformations

**Question 4: What is the difference between Change Type and Change Type Using Locale?**  
Why was the 'Using Locale' option necessary for the OrderDate column in this exercise?

**Change Type** applies the data type using the machine's default locale settings. **Change Type Using Locale** lets you specify the origin locale, which determines how ambiguous formats are parsed. The key rule is to match the locale to where the data came from, not where you are. In this dataset, formats like "January 18 2024" mixed with "YYYY-MM-DD" and "MM/DD/YYYY" cannot be resolved without knowing the language and regional format, so the en-US locale is required. This also means if data came from a UK system, you would set en-GB, and "01/05/2024" would correctly parse as May 1st instead of January 5th.

---

**Question 5: What would happen if you skipped the Trim step on CustomerName?**  
Consider a scenario where a report groups sales by customer. How would extra spaces affect the grouping results?

Power BI would treat " TechZone Inc" and "TechZone Inc" as two different customers. Any visual, table, or measure that groups or filters by customer would split that customer's sales across two separate rows, producing incorrect totals and a misleading customer list.

---

## Section C | Advanced Editor & M Language

**Question 6: What is the purpose of the let…in structure in M code?**  
Explain in your own words how each step builds on the previous one.

The `let` block is all the steps you want M to execute. Each step is a named variable that holds the result of a transformation, and each step can reference the one before it by name. M goes through each step in order until it reaches the end. The `in` keyword points to whichever step's result you want as the final output that gets loaded into the model. It is like a pandas pipeline where each variable builds on the last, and `in` is like saying "return this step."

---

**Question 7: In Task 7, you used Date.Year() to extract the year. How would you modify the code to extract the month number instead?**

    #"Added Month" = Table.AddColumn(
        #"Added Revenue",
        "OrderMonth",
        each Date.Month([OrderDate]),
        Int64.Type
    )

---

**Question 8 (Challenge): Why is it important to reference the correct previous step name in M code?**  
What would happen if you referenced a step name that does not exist, or referenced an earlier step rather than the most recent one?

M code is sequential — each step must reference an existing step name. If you reference a step that does not exist, Power Query throws an expression error at that line. If you reference an earlier step instead of the most recent one, your new column gets added to the table as it existed at that earlier point, bypassing all transformations applied after it. You would silently lose work without any error message to warn you. This is also why `in` matters — if you forget to update `in` to point at your new last step, your new column gets added but never makes it to the output.

---

## Key Takeaways

- Power Query runs **before** the data enters the model — all cleaning, shaping, and column additions happen here in M language
- `let` defines the steps, `in` defines the output — M executes every step in order
- `each` is required in M to establish row context; DAX calculated columns have row context automatically
- **Valid ≠ Unique** — Column Quality only checks for errors and nulls, not duplicates. Always check Distinct vs Count in Column Statistics
- Locale matching matters for dates — always match to the data's origin, not your machine's setting
- Fixed Decimal Number is the better choice over Decimal Number for currency and financial columns
- Leaving year as `Int64` is correct — a year extracted from a date is an integer, not a date value