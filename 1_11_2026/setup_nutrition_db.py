"""
Nutrition Database Setup
Run this script to create and populate the nutrition practice database.
"""

import sqlite3
import os

def create_database():
    """Create the nutrition practice database with sample data."""
    
    db_path = os.path.join(os.path.dirname(__file__), 'nutrition.db')
    
    if os.path.exists(db_path):
        os.remove(db_path)
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # ==========================================
    # CREATE TABLES
    # ==========================================
    
    # Foods table
    cursor.execute('''
        CREATE TABLE foods (
            food_id INTEGER PRIMARY KEY,
            food_name TEXT NOT NULL,
            category TEXT,
            calories INTEGER,
            protein_g DECIMAL(5,2),
            carbs_g DECIMAL(5,2),
            fat_g DECIMAL(5,2),
            fiber_g DECIMAL(5,2),
            serving_size TEXT
        )
    ''')
    
    # Users table
    cursor.execute('''
        CREATE TABLE users (
            user_id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            age INTEGER,
            gender TEXT,
            weight_kg DECIMAL(5,2),
            height_cm INTEGER,
            activity_level TEXT,
            goal TEXT,
            registration_date DATE
        )
    ''')
    
    # Meals table
    cursor.execute('''
        CREATE TABLE meals (
            meal_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            meal_type TEXT,
            meal_date DATE,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    ''')
    
    # Meal_Items table
    cursor.execute('''
        CREATE TABLE meal_items (
            item_id INTEGER PRIMARY KEY,
            meal_id INTEGER,
            food_id INTEGER,
            quantity DECIMAL(5,2),
            FOREIGN KEY (meal_id) REFERENCES meals(meal_id),
            FOREIGN KEY (food_id) REFERENCES foods(food_id)
        )
    ''')
    
    # Daily_Goals table
    cursor.execute('''
        CREATE TABLE daily_goals (
            goal_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            target_calories INTEGER,
            target_protein_g INTEGER,
            target_carbs_g INTEGER,
            target_fat_g INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    ''')
    
    # ==========================================
    # INSERT SAMPLE DATA
    # ==========================================
    
    # Foods (various nutrition items)
    foods = [
        (1, 'Grilled Chicken Breast', 'Protein', 165, 31.0, 0.0, 3.6, 0.0, '100g'),
        (2, 'Brown Rice', 'Grains', 216, 5.0, 45.0, 1.8, 3.5, '1 cup cooked'),
        (3, 'Broccoli', 'Vegetables', 55, 3.7, 11.0, 0.6, 5.1, '1 cup'),
        (4, 'Salmon Fillet', 'Protein', 208, 20.0, 0.0, 13.0, 0.0, '100g'),
        (5, 'Sweet Potato', 'Vegetables', 103, 2.3, 24.0, 0.1, 3.8, '1 medium'),
        (6, 'Greek Yogurt', 'Dairy', 100, 17.0, 6.0, 0.7, 0.0, '170g'),
        (7, 'Almonds', 'Nuts', 164, 6.0, 6.0, 14.0, 3.5, '28g'),
        (8, 'Banana', 'Fruits', 105, 1.3, 27.0, 0.4, 3.1, '1 medium'),
        (9, 'Eggs', 'Protein', 78, 6.0, 0.6, 5.0, 0.0, '1 large'),
        (10, 'Spinach', 'Vegetables', 23, 2.9, 3.6, 0.4, 2.2, '100g'),
        (11, 'Oatmeal', 'Grains', 154, 5.0, 27.0, 2.6, 4.0, '1 cup cooked'),
        (12, 'Avocado', 'Fruits', 160, 2.0, 9.0, 15.0, 7.0, '1/2 avocado'),
        (13, 'Quinoa', 'Grains', 222, 8.0, 39.0, 3.5, 5.0, '1 cup cooked'),
        (14, 'Tuna', 'Protein', 132, 28.0, 0.0, 1.0, 0.0, '100g'),
        (15, 'Apple', 'Fruits', 95, 0.5, 25.0, 0.3, 4.4, '1 medium'),
        (16, 'Cottage Cheese', 'Dairy', 206, 28.0, 6.0, 9.0, 0.0, '1 cup'),
        (17, 'Black Beans', 'Legumes', 227, 15.0, 41.0, 0.9, 15.0, '1 cup'),
        (18, 'Olive Oil', 'Fats', 119, 0.0, 0.0, 13.5, 0.0, '1 tbsp'),
        (19, 'Whole Wheat Bread', 'Grains', 81, 4.0, 14.0, 1.0, 2.0, '1 slice'),
        (20, 'Blueberries', 'Fruits', 84, 1.1, 21.0, 0.5, 3.6, '1 cup')
    ]
    cursor.executemany('INSERT INTO foods VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', foods)
    
    # Users
    users = [
        (1, 'john_fitness', 28, 'Male', 82.5, 180, 'High', 'Muscle Gain', '2024-01-15'),
        (2, 'sarah_health', 32, 'Female', 65.0, 165, 'Moderate', 'Weight Loss', '2024-02-20'),
        (3, 'mike_runner', 25, 'Male', 70.0, 175, 'Very High', 'Maintenance', '2024-01-10'),
        (4, 'emma_yoga', 29, 'Female', 58.0, 160, 'Moderate', 'Maintenance', '2024-03-05'),
        (5, 'david_bulk', 35, 'Male', 90.0, 185, 'High', 'Muscle Gain', '2024-02-01'),
        (6, 'lisa_slim', 27, 'Female', 72.0, 168, 'Low', 'Weight Loss', '2024-03-15'),
        (7, 'tom_active', 31, 'Male', 78.0, 178, 'Moderate', 'Maintenance', '2024-01-25'),
        (8, 'anna_clean', 24, 'Female', 55.0, 158, 'Moderate', 'Weight Loss', '2024-04-01')
    ]
    cursor.executemany('INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', users)
    
    # Daily Goals
    daily_goals = [
        (1, 1, 2800, 180, 300, 90),
        (2, 2, 1600, 100, 150, 55),
        (3, 3, 2500, 120, 320, 75),
        (4, 4, 1800, 90, 200, 60),
        (5, 5, 3200, 200, 350, 100),
        (6, 6, 1400, 80, 130, 50),
        (7, 7, 2200, 110, 250, 70),
        (8, 8, 1500, 90, 140, 50)
    ]
    cursor.executemany('INSERT INTO daily_goals VALUES (?, ?, ?, ?, ?, ?)', daily_goals)
    
    # Meals (spanning multiple days)
    meals = [
        (1, 1, 'Breakfast', '2024-10-01'),
        (2, 1, 'Lunch', '2024-10-01'),
        (3, 1, 'Dinner', '2024-10-01'),
        (4, 2, 'Breakfast', '2024-10-01'),
        (5, 2, 'Lunch', '2024-10-01'),
        (6, 2, 'Dinner', '2024-10-01'),
        (7, 3, 'Breakfast', '2024-10-01'),
        (8, 3, 'Lunch', '2024-10-01'),
        (9, 1, 'Breakfast', '2024-10-02'),
        (10, 1, 'Lunch', '2024-10-02'),
        (11, 1, 'Dinner', '2024-10-02'),
        (12, 4, 'Breakfast', '2024-10-01'),
        (13, 4, 'Lunch', '2024-10-01'),
        (14, 5, 'Breakfast', '2024-10-01'),
        (15, 5, 'Lunch', '2024-10-01'),
        (16, 5, 'Dinner', '2024-10-01'),
        (17, 6, 'Breakfast', '2024-10-01'),
        (18, 6, 'Lunch', '2024-10-01'),
        (19, 7, 'Breakfast', '2024-10-02'),
        (20, 7, 'Lunch', '2024-10-02')
    ]
    cursor.executemany('INSERT INTO meals VALUES (?, ?, ?, ?)', meals)
    
    # Meal Items
    meal_items = [
        (1, 1, 9, 3),      # john breakfast: 3 eggs
        (2, 1, 11, 1),     # john breakfast: oatmeal
        (3, 1, 8, 1),      # john breakfast: banana
        (4, 2, 1, 1.5),    # john lunch: 150g chicken
        (5, 2, 2, 1),      # john lunch: brown rice
        (6, 2, 3, 1),      # john lunch: broccoli
        (7, 3, 4, 1.5),    # john dinner: 150g salmon
        (8, 3, 5, 1),      # john dinner: sweet potato
        (9, 3, 10, 1),     # john dinner: spinach
        (10, 4, 6, 1),     # sarah breakfast: greek yogurt
        (11, 4, 20, 1),    # sarah breakfast: blueberries
        (12, 5, 14, 1),    # sarah lunch: tuna
        (13, 5, 10, 1),    # sarah lunch: spinach
        (14, 6, 1, 1),     # sarah dinner: chicken
        (15, 6, 3, 1.5),   # sarah dinner: broccoli
        (16, 7, 11, 1.5),  # mike breakfast: oatmeal
        (17, 7, 8, 2),     # mike breakfast: 2 bananas
        (18, 8, 1, 2),     # mike lunch: 200g chicken
        (19, 8, 13, 1),    # mike lunch: quinoa
        (20, 9, 9, 4),     # john day2 breakfast: 4 eggs
        (21, 9, 19, 2),    # john day2 breakfast: bread
        (22, 10, 4, 1),    # john day2 lunch: salmon
        (23, 10, 2, 1),    # john day2 lunch: rice
        (24, 11, 1, 2),    # john day2 dinner: 200g chicken
        (25, 11, 5, 1),    # john day2 dinner: sweet potato
        (26, 12, 6, 1),    # emma breakfast: yogurt
        (27, 12, 7, 1),    # emma breakfast: almonds
        (28, 13, 1, 1),    # emma lunch: chicken
        (29, 13, 10, 1.5), # emma lunch: spinach
        (30, 14, 9, 4),    # david breakfast: 4 eggs
        (31, 14, 11, 2),   # david breakfast: 2 cups oatmeal
        (32, 15, 1, 2),    # david lunch: 200g chicken
        (33, 15, 2, 2),    # david lunch: 2 cups rice
        (34, 16, 4, 2),    # david dinner: 200g salmon
        (35, 16, 17, 1),   # david dinner: black beans
        (36, 17, 6, 0.5),  # lisa breakfast: half yogurt
        (37, 17, 15, 1),   # lisa breakfast: apple
        (38, 18, 14, 0.5), # lisa lunch: 50g tuna
        (39, 18, 10, 2),   # lisa lunch: lots of spinach
        (40, 19, 9, 2),    # tom breakfast: 2 eggs
        (41, 19, 19, 2),   # tom breakfast: bread
        (42, 20, 1, 1.5),  # tom lunch: 150g chicken
        (43, 20, 13, 1)    # tom lunch: quinoa
    ]
    cursor.executemany('INSERT INTO meal_items VALUES (?, ?, ?, ?)', meal_items)
    
    conn.commit()
    conn.close()
    
    print(f"✅ Database created successfully at: {db_path}")
    print("\n📊 Tables created:")
    print("   - foods (20 items)")
    print("   - users (8 users)")
    print("   - meals (20 meals)")
    print("   - meal_items (43 records)")
    print("   - daily_goals (8 goals)")
    print("\n🥗 Ready to practice nutrition SQL queries!")

if __name__ == "__main__":
    create_database()
