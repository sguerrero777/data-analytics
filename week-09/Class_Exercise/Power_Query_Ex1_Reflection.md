# Power Query Exercise 1 — Reflection Questions
 Week 9 | Retail Sales Q1 2024*

---

## Question 1
**Why is it important to click Transform Data instead of Load when connecting to a data source in Power BI?**

It is important to click Transform Data instead of Load when connecting to a data source in Power BI because Transform Data opens Power Query Editor, allowing you to clean the data, remove unnecessary columns, and assign the correct data types before anything enters the model. Load brings the data in as-is with no opportunity to make any changes first. Correct data types are crucial for analysis — for example, a date column may accidentally be assigned as text, which would prevent proper datetime operations like revenue trends over months or years from being performed.

---

## Question 2
**What is the Applied Steps pane and why is it useful? What would happen if you deleted a step?**

The Applied Steps pane is like a tracker for every transformation made in Power Query Editor, recording each action in the order it was applied. It is very helpful because it lets you review, edit, or remove specific steps without starting over from scratch. If you deleted a step, it would undo whatever that step applied — but it could also break any downstream steps that depended on it. For example, if you deleted the Renamed Columns step, any later step referencing those new column names would throw an error.

---

## Question 3
**You removed the State column in Task 2. Can you think of a situation where keeping State might be valuable? What would you need to change in the exercise?**

Keeping the State column might be valuable if the analysis requires cross-territory performance based on sales revenue. For example, comparing sales across different states or grouping customers by state for regional reporting. To keep it, I would go back to the Applied Steps pane and delete the step where State was removed, which would restore the column for all downstream steps.

---

## Question 4
**In Task 4, what problems could occur in your report if you left Quantity as a Text data type instead of Whole Number?**

If I left Quantity as a Text data type instead of a Whole Number, I would not be able to perform any sales calculations on it since Power BI cannot do math on text values. It would either throw an error or simply refuse to calculate. This would leave a big gap in data knowledge, for example making it impossible to calculate total revenue since Sale Amount depends on Quantity being a number.

---

## Question 5
**In Task 5, you created Sale Amount using a custom column formula. Why is it better to do this calculation in Power Query rather than in Excel before importing?**

It is better to do this calculation in Power Query rather than in Excel before importing because Power Query stores it as a repeatable applied step, meaning if the CSV refreshes with new rows, the Sale Amount and Discount Amount columns automatically recalculate for all new data without any manual work. Doing it in Excel before importing would mean manually recalculating every time the data updates, which is error-prone and breaks the data pipeline workflow.

---

## Question 6
**Look at the Applied Steps pane after completing all tasks. If a colleague sent you the same CSV with 100 new rows, what would you need to do to update the report?**

I would simply click Refresh in Power BI and Power Query would automatically apply all the same Applied Steps to the 100 new rows: the transformations, renamed columns, data types, and calculated columns would all run again on the new data without any manual work. The only thing I might want to do is check for any new anomalies or unexpected values in the new rows by reviewing the data preview in Power Query Editor.
