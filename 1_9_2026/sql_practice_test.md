# SQL Practice Test - Real Estate Rentals 🏢

## Your Challenge

Solve these 10 problems **on your own** without looking at solutions. This will test what you've learned!

---

## Database Setup

Run this code to create your rental properties database:

```sql
-- Create rental properties table
CREATE TABLE rentals (
    rental_id INTEGER PRIMARY KEY,
    property_name TEXT,
    location TEXT,
    monthly_rent REAL,
    bedrooms INTEGER,
    furnished TEXT,
    available TEXT
);

-- Create tenants table
CREATE TABLE tenants (
    tenant_id INTEGER PRIMARY KEY,
    name TEXT,
    rental_id INTEGER,
    move_in_date TEXT,
    lease_months INTEGER
);

-- Insert rental properties
INSERT INTO rentals VALUES
(1, 'Sunset Apartments', 'Downtown', 1200, 1, 'Yes', 'No'),
(2, 'Green Valley Condo', 'Suburbs', 1800, 2, 'No', 'Yes'),
(3, 'Ocean View Studio', 'Beach', 950, 1, 'Yes', 'Yes'),
(4, 'Mountain Lodge', 'Mountains', 2500, 3, 'Yes', 'No'),
(5, 'City Center Loft', 'Downtown', 2200, 2, 'No', 'Yes'),
(6, 'Riverside Cottage', 'Riverside', 1500, 2, 'Yes', 'No'),
(7, 'Park Place Apartment', 'Midtown', 1100, 1, 'No', 'Yes'),
(8, 'Lakeside Villa', 'Lakeside', 3000, 4, 'Yes', 'Yes'),
(9, 'Urban Studio', 'Downtown', 900, 1, 'No', 'Yes'),
(10, 'Garden Terrace', 'Suburbs', 1600, 2, 'Yes', 'Yes');

-- Insert tenants
INSERT INTO tenants VALUES
(1, 'Alice Johnson', 1, '2025-01-15', 12),
(2, 'Bob Smith', 4, '2024-11-01', 24),
(3, 'Carol White', 6, '2025-02-01', 12),
(4, 'David Brown', 3, '2024-12-15', 6),
(5, 'Emma Davis', 5, '2025-03-01', 18);
```

---

## 📝 Your 10 Problems

### Problem 1: Show All Rentals ⭐
Display all information from the rentals table.

---

### Problem 2: Available Properties ⭐
Show the property name and monthly rent for all available properties (where available = 'Yes').

---

### Problem 3: Downtown Properties ⭐⭐
Find all properties located in Downtown. Show property name, location, and monthly rent.

---

### Problem 4: Affordable Rentals ⭐⭐
Show properties with monthly rent less than $1500. Display property name, monthly rent, and bedrooms.

---

### Problem 5: Sort by Rent ⭐⭐
List all properties sorted by monthly rent from highest to lowest. Show property name and monthly rent.

---

### Problem 6: Count by Location ⭐⭐⭐
How many rental properties are in each location? Show location and count.

---

### Problem 7: Average Rent ⭐⭐
Calculate the average monthly rent across all properties.

---

### Problem 8: Furnished and Available ⭐⭐⭐
Find properties that are BOTH furnished (furnished = 'Yes') AND available (available = 'Yes'). Show property name, location, and monthly rent.

---

### Problem 9: Expensive Rentals ⭐⭐⭐
Find properties with rent above $2000. Show property name, monthly rent, and bedrooms, sorted by rent.

---

### Problem 10: Properties with 2 Bedrooms ⭐⭐
Show all 2-bedroom properties. Display property name, location, monthly rent, and whether they're furnished.

---

## 🎯 Bonus Challenges (Optional)

### Bonus 1: Total Rental Income ⭐⭐⭐
Calculate the total monthly income if ALL properties were rented out.

---

### Bonus 2: Highest Rent by Location ⭐⭐⭐⭐
Show the highest monthly rent in each location.

---

### Bonus 3: Current Tenants ⭐⭐⭐⭐
Show all tenant names along with their property name and monthly rent. (Hint: You'll need to JOIN the two tables)

---

## ✅ How to Check Your Work

After solving each problem:
1. ✅ Does your query run without errors?
2. ✅ Does the result make sense?
3. ✅ Did you get the expected number of rows?

### Expected Row Counts:
- Problem 2: Should return 6 rows
- Problem 3: Should return 3 rows
- Problem 4: Should return 5 rows
- Problem 6: Should return 6 different locations
- Problem 8: Should return 4 rows
- Problem 10: Should return 4 rows

---

## 💡 Hints (Only look if you're stuck!)

<details>
<summary>Hint for Problem 6</summary>
Use GROUP BY with COUNT(*)
</details>

<details>
<summary>Hint for Problem 8</summary>
Use WHERE with AND to combine two conditions
</details>

<details>
<summary>Hint for Bonus 2</summary>
Use GROUP BY location with MAX(monthly_rent)
</details>

<details>
<summary>Hint for Bonus 3</summary>
Use INNER JOIN to connect tenants and rentals tables using rental_id
</details>

---

## 📊 Scoring Guide

- **1-4 problems:** Keep practicing! Review the easy tutorial.
- **5-7 problems:** Good progress! You're getting the hang of it.
- **8-10 problems:** Excellent! You understand SQL basics well.
- **All 10 + Bonuses:** Outstanding! You're ready for more advanced topics.

---

**Good luck! You've got this! 💪**

*Remember: It's okay to struggle. That's how you learn. Try your best before looking at any hints!*
