# ============================================================
# RETAIL SALES DATASET — EXPLORATORY DATA ANALYSIS (EDA)
# ============================================================

# Importing required libraries
import numpy as n
import pandas as p
import matplotlib.pyplot as m
import seaborn as s


# ============================================================
# 1. LOADING DATA AND CHECKING DATA QUALITY
# ============================================================

# Loading the retail sales CSV file into a DataFrame
data = p.read_csv("retail_sales_dataset.csv")

# Checking the number of missing values in each column
s1 = data.isna().sum()

# Counting the number of duplicate rows
d = data.duplicated().sum()

# Counting transactions belonging to each product category
c = data["Product Category"].value_counts()

# Counting transactions belonging to each gender
gender = data["Gender"].value_counts()


# ============================================================
# 2. PRODUCT CATEGORY ANALYSIS
# ============================================================

# Calculating the average transaction amount for each category
amount = data.groupby("Product Category")["Total Amount"].mean()

# Calculating the total sales amount for each category
category_total_sales = data.groupby("Product Category")["Total Amount"].sum()

# Calculating the average price per unit for each category
price = data.groupby("Product Category")["Price per Unit"].mean()

# Finding the maximum transaction amount in each category
maximum = data.groupby("Product Category")["Total Amount"].max()

# Finding the minimum transaction amount in each category
minimum = data.groupby("Product Category")["Total Amount"].min()

# Finding the category with the highest individual transaction amount
max_transaction_category = (
    data.groupby("Product Category")["Total Amount"].max().idxmax()
)

# Finding the category with the lowest individual transaction amount
min_transaction_category = (
    data.groupby("Product Category")["Total Amount"].min().idxmin()
)

# Finding the category with the highest total sales
highest_sales_category = category_total_sales.idxmax()

# Finding the category with the lowest total sales
lowest_sales_category = category_total_sales.idxmin()


# ============================================================
# 3. GENDER AND CUSTOMER ANALYSIS
# ============================================================

# Calculating the average customer age for each gender
avg = data.groupby("Gender")["Age"].mean()

# Counting transactions made by each gender
g = data.groupby("Gender")["Transaction ID"].count()

# Creating a pivot table showing average spending by gender
# across each product category
check = p.pivot_table(
    data,
    values="Total Amount",
    index="Gender",
    columns="Product Category",
    aggfunc="mean"
)


# ============================================================
# 4. DATE FILTERING AND PERIOD ANALYSIS
# ============================================================

# Converting Date from string format into datetime format
data["Date"] = p.to_datetime(data["Date"])

# Calculating total spending by gender between December 21 and 30, 2023
de = data[
    (data["Date"] >= "2023-12-21") &
    (data["Date"] <= "2023-12-30")
].groupby("Gender")["Total Amount"].sum()

# Calculating total spending by product category from March through
# May 2023, including both March 1 and May 31
dev = data[
    (data["Date"] >= "2023-03-01") &
    (data["Date"] <= "2023-05-31")
].groupby("Product Category")["Total Amount"].sum()

# Calculating the average age of customers by gender during
# December 21–30, 2023
ds = data[
    (data["Date"] >= "2023-12-21") &
    (data["Date"] <= "2023-12-30")
].groupby("Gender")["Age"].mean()


# ============================================================
# 5. MONTH-WISE ANALYSIS
# ============================================================

# Extracting the month number from each transaction date
data["Month"] = data["Date"].dt.month

# Calculating total sales for each month
monthly_sales = data.groupby("Month")["Total Amount"].sum()

# Calculating the average transaction amount for each month
monthly_average = data.groupby("Month")["Total Amount"].mean()

# Finding the month with the highest total sales
highest_sales_month = monthly_sales.idxmax()

# Finding the month with the highest average transaction amount
highest_average_month = monthly_average.idxmax()


# ============================================================
# 6. GENDER-WISE MONTHLY PIVOT TABLES
# ============================================================

# Total spending by gender for each month
gender_month = p.pivot_table(
    data,
    values="Total Amount",
    index="Gender",
    columns="Month",
    aggfunc="sum"
)

# Total spending by product category for each month
mon = p.pivot_table(
    data,
    values="Total Amount",
    index="Product Category",
    columns="Month",
    aggfunc="sum"
)

# Counting transactions made by each gender in each month
counto = p.pivot_table(
    data,
    values="Transaction ID",
    index="Gender",
    columns="Month",
    aggfunc="count"
)

# Counting transaction records for each product category in each month
cunto = p.pivot_table(
    data,
    values="Transaction ID",
    index="Product Category",
    columns="Month",
    aggfunc="count"
)


# ============================================================
# 7. AGE GROUP ANALYSIS
# ============================================================

# Dividing customer ages into groups
# Intervals: 18–25, 26–35, 36–45, 46–55, and 56+
data["Age Group"] = p.cut(
    data["Age"],
    bins=[17, 25, 35, 45, 55, float("inf")],
    labels=["18-25", "26-35", "36-45", "46-55", "56+"]
)

# Finding the age group with the highest total sales
age1 = data.groupby(
    "Age Group", observed=False
)["Total Amount"].sum().idxmax()

# Finding the age group with the highest average transaction amount
age2 = data.groupby(
    "Age Group", observed=False
)["Total Amount"].mean().idxmax()

# Total spending by age group across product categories
age3 = p.pivot_table(
    data,
    values="Total Amount",
    index="Age Group",
    columns="Product Category",
    aggfunc="sum"
)

# Total spending by age group and gender
age4 = p.pivot_table(
    data,
    values="Total Amount",
    index="Age Group",
    columns="Gender",
    aggfunc="sum"
)


# ============================================================
# 8. WEEKDAY ANALYSIS
# ============================================================

# Extracting weekday number: Monday = 0, Sunday = 6
data["Weekday"] = data["Date"].dt.day_of_week

# Total spending by weekday and product category
day = p.pivot_table(
    data,
    values="Total Amount",
    index="Weekday",
    columns="Product Category",
    aggfunc="sum"
)

# Average transaction amount by weekday and product category
day1 = p.pivot_table(
    data,
    values="Total Amount",
    index="Weekday",
    columns="Product Category",
    aggfunc="mean"
)

# Total spending by weekday and gender
day2 = p.pivot_table(
    data,
    values="Total Amount",
    index="Weekday",
    columns="Gender",
    aggfunc="sum"
)

# Average transaction amount by weekday and gender
day3 = p.pivot_table(
    data,
    values="Total Amount",
    index="Weekday",
    columns="Gender",
    aggfunc="mean"
)


# ============================================================
# 9. QUANTITY ANALYSIS
# ============================================================

# Total spending by quantity and product category
q = p.pivot_table(
    data,
    values="Total Amount",
    index="Quantity",
    columns="Product Category",
    aggfunc="sum"
)

# Average transaction amount by quantity and product category
q1 = p.pivot_table(
    data,
    values="Total Amount",
    index="Quantity",
    columns="Product Category",
    aggfunc="mean"
)

# Total spending by quantity and gender
q2 = p.pivot_table(
    data,
    values="Total Amount",
    index="Quantity",
    columns="Gender",
    aggfunc="sum"
)

# Counting transaction records by quantity and gender
q3 = p.pivot_table(
    data,
    values="Total Amount",
    index="Quantity",
    columns="Gender",
    aggfunc="count"
)

# Finding the maximum transaction amount by quantity and category
q4 = p.pivot_table(
    data,
    values="Total Amount",
    index="Quantity",
    columns="Product Category",
    aggfunc="max"
)

# Finding the minimum transaction amount by quantity and category
q5 = p.pivot_table(
    data,
    values="Total Amount",
    index="Quantity",
    columns="Product Category",
    aggfunc="min"
)

# Total spending for each quantity across different weekdays
q6 = p.pivot_table(
    data,
    values="Total Amount",
    index="Quantity",
    columns="Weekday",
    aggfunc="sum"
)


# ============================================================
# 10. VISUALIZATIONS
# ============================================================

# Plot 1: Joint plot showing Month versus Total Amount
s.jointplot(
    x="Month",
    y="Total Amount",
    data=data
)

# Plot 2: Bar plot showing average transaction amount by gender
s.barplot(
    x="Gender",
    y="Total Amount",
    data=data,
    hue="Gender"
)

# Plot 3: Strip plot showing individual transaction amounts
# across product categories
s.stripplot(
    x="Product Category",
    y="Total Amount",
    data=data
)

# Plot 4: Bar plot showing average transaction amount by gender
s.barplot(
    y="Total Amount",
    x="Gender",
    data=data,
    hue="Gender"
)

# Plot 5: Strip plot comparing transaction amounts by category and gender
s.stripplot(
    x="Product Category",
    y="Total Amount",
    hue="Gender",
    data=data
)

# Plot 6: Bar plot comparing average transaction amounts
# across categories and genders
s.barplot(
    x="Product Category",
    y="Total Amount",
    hue="Gender",
    data=data
)

# Plot 7: Bar plot comparing average transaction amounts
# across weekdays and genders
s.barplot(
    x="Weekday",
    y="Total Amount",
    hue="Gender",
    data=data
)

# Plot 8: Box plot comparing transaction amount distributions
# across weekdays and genders
s.boxplot(
    x="Weekday",
    y="Total Amount",
    hue="Gender",
    data=data
)

# Plot 9: Swarm plot showing transaction amounts by category and gender
s.swarmplot(
    x="Product Category",
    y="Total Amount",
    data=data,
    hue="Gender"
)

# Plot 10: Swarm plot showing quantities purchased by category and gender
s.swarmplot(
    x="Product Category",
    y="Quantity",
    data=data,
    hue="Gender"
)

# Plot 11: Regression plot showing Quantity versus Total Amount
# with separate trend lines by gender
s.lmplot(
    x="Quantity",
    y="Total Amount",
    hue="Gender",
    data=data
)

# Plot 12: Heatmap showing total sales by product category and month
s.heatmap(
    mon,
    annot=True,
    fmt=".1f"
)

# Plot 13: Heatmap showing total sales by age group and category
s.heatmap(
    age3,
    annot=True,
    fmt=".1f"
)

# Plot 14: Heatmap showing total spending by age group and gender
s.heatmap(
    age4,
    annot=True,
    fmt=".1f"
)

# Plot 15: Heatmap showing total sales by quantity and weekday
s.heatmap(
    q6,
    annot=True,
    fmt=".1f"
)


# ============================================================
# 11. DISPLAY ALL PLOTS
# ============================================================

# Display the generated plots
m.show()



#Project Findings
#Product category: Electronics generated the highest total sales, while Beauty generated the lowest.



#Gender: Female customers accounted for 510 transactions and male customers for 490. Female customers also had higher total sales and a higher average transaction amount in this dataset.



#Monthly sales: May had the highest total sales and the highest transaction count.



#Average transaction value: February had the highest average transaction amount.



#Age groups: The 46–55 age group had the highest total spending, while the 18–25 age group had the highest average transaction amount.



#Category preferences: Female customers had their highest average transaction amount in Clothing, while male customers had theirs in Beauty.