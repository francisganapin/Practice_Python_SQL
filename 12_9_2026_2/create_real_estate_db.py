"""
Real Estate Database Creator
Creates a SQLite database with sample real estate data for SQL practice.
"""

import sqlite3
import random
from datetime import datetime, timedelta

# Database connection
conn = sqlite3.connect('real_estate.db')
cursor = conn.cursor()

# ============================================
# DROP EXISTING TABLES (for clean recreation)
# ============================================
cursor.execute("DROP TABLE IF EXISTS Showings")
cursor.execute("DROP TABLE IF EXISTS Transactions")
cursor.execute("DROP TABLE IF EXISTS Properties")
cursor.execute("DROP TABLE IF EXISTS Agents")
cursor.execute("DROP TABLE IF EXISTS Clients")

# ============================================
# CREATE TABLES
# ============================================

# Agents Table
cursor.execute("""
CREATE TABLE Agents (
    agent_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT UNIQUE,
    phone TEXT,
    hire_date DATE,
    commission_rate REAL DEFAULT 0.03
)
""")

# Clients Table
cursor.execute("""
CREATE TABLE Clients (
    client_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT,
    phone TEXT,
    client_type TEXT CHECK(client_type IN ('buyer', 'seller', 'both'))
)
""")

# Properties Table
cursor.execute("""
CREATE TABLE Properties (
    property_id INTEGER PRIMARY KEY,
    address TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    zip_code TEXT,
    price REAL NOT NULL,
    bedrooms INTEGER,
    bathrooms REAL,
    sqft INTEGER,
    year_built INTEGER,
    property_type TEXT CHECK(property_type IN ('house', 'condo', 'townhouse', 'apartment')),
    status TEXT CHECK(status IN ('available', 'pending', 'sold')) DEFAULT 'available',
    listing_date DATE,
    agent_id INTEGER,
    FOREIGN KEY (agent_id) REFERENCES Agents(agent_id)
)
""")

# Transactions Table
cursor.execute("""
CREATE TABLE Transactions (
    transaction_id INTEGER PRIMARY KEY,
    property_id INTEGER,
    agent_id INTEGER,
    buyer_id INTEGER,
    seller_id INTEGER,
    sale_price REAL NOT NULL,
    sale_date DATE,
    commission REAL,
    FOREIGN KEY (property_id) REFERENCES Properties(property_id),
    FOREIGN KEY (agent_id) REFERENCES Agents(agent_id),
    FOREIGN KEY (buyer_id) REFERENCES Clients(client_id),
    FOREIGN KEY (seller_id) REFERENCES Clients(client_id)
)
""")

# Showings Table
cursor.execute("""
CREATE TABLE Showings (
    showing_id INTEGER PRIMARY KEY,
    property_id INTEGER,
    agent_id INTEGER,
    client_id INTEGER,
    showing_date DATE,
    feedback TEXT,
    rating INTEGER CHECK(rating BETWEEN 1 AND 5),
    FOREIGN KEY (property_id) REFERENCES Properties(property_id),
    FOREIGN KEY (agent_id) REFERENCES Agents(agent_id),
    FOREIGN KEY (client_id) REFERENCES Clients(client_id)
)
""")

# ============================================
# SAMPLE DATA
# ============================================

# Sample data lists
first_names = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer', 'Michael', 'Linda', 
               'William', 'Elizabeth', 'David', 'Barbara', 'Richard', 'Susan', 'Joseph', 'Jessica',
               'Thomas', 'Sarah', 'Charles', 'Karen', 'Christopher', 'Nancy', 'Daniel', 'Lisa',
               'Matthew', 'Betty', 'Anthony', 'Margaret', 'Mark', 'Sandra', 'Donald', 'Ashley',
               'Steven', 'Kimberly', 'Paul', 'Emily', 'Andrew', 'Donna', 'Joshua', 'Michelle']

last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis',
              'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson',
              'Thomas', 'Taylor', 'Moore', 'Jackson', 'Martin', 'Lee', 'Perez', 'Thompson',
              'White', 'Harris', 'Sanchez', 'Clark', 'Ramirez', 'Lewis', 'Robinson']

cities = [
    ('Los Angeles', 'CA', '90001'), ('San Francisco', 'CA', '94102'), ('San Diego', 'CA', '92101'),
    ('Phoenix', 'AZ', '85001'), ('Las Vegas', 'NV', '89101'), ('Seattle', 'WA', '98101'),
    ('Portland', 'OR', '97201'), ('Denver', 'CO', '80201'), ('Austin', 'TX', '78701'),
    ('Houston', 'TX', '77001'), ('Miami', 'FL', '33101'), ('Orlando', 'FL', '32801'),
    ('Atlanta', 'GA', '30301'), ('Chicago', 'IL', '60601'), ('New York', 'NY', '10001')
]

streets = ['Main St', 'Oak Ave', 'Maple Dr', 'Cedar Ln', 'Pine Rd', 'Elm St', 'Park Ave',
           'Lake Dr', 'Hill Rd', 'Valley Way', 'Sunset Blvd', 'Ocean Ave', 'Mountain View',
           'River Rd', 'Forest Dr', 'Garden Way', 'Spring St', 'Summit Ave', 'Meadow Ln', 'Vista Dr']

property_types = ['house', 'condo', 'townhouse', 'apartment']
feedback_options = [
    'Loved the kitchen', 'Needs renovation', 'Great location', 'Too small',
    'Perfect for family', 'Nice backyard', 'Good natural light', 'Noisy neighborhood',
    'Modern finishes', 'Overpriced', 'Beautiful view', 'Needs work', 'Move-in ready',
    'Great potential', 'Not interested', 'Very interested', 'Will think about it'
]

# Helper function for random dates
def random_date(start_year=2020, end_year=2025):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    random_days = random.randint(0, delta.days)
    return (start + timedelta(days=random_days)).strftime('%Y-%m-%d')

# Insert Agents (15 agents)
agents_data = []
for i in range(1, 16):
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    email = f"{fname.lower()}.{lname.lower()}@realestate.com"
    phone = f"555-{random.randint(100,999)}-{random.randint(1000,9999)}"
    hire_date = random_date(2015, 2023)
    commission = round(random.uniform(0.02, 0.05), 3)
    agents_data.append((i, fname, lname, email, phone, hire_date, commission))

cursor.executemany("""
    INSERT INTO Agents (agent_id, first_name, last_name, email, phone, hire_date, commission_rate)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", agents_data)

# Insert Clients (50 clients)
clients_data = []
for i in range(1, 51):
    fname = random.choice(first_names)
    lname = random.choice(last_names)
    email = f"{fname.lower()}{i}@email.com"
    phone = f"555-{random.randint(100,999)}-{random.randint(1000,9999)}"
    client_type = random.choice(['buyer', 'seller', 'both'])
    clients_data.append((i, fname, lname, email, phone, client_type))

cursor.executemany("""
    INSERT INTO Clients (client_id, first_name, last_name, email, phone, client_type)
    VALUES (?, ?, ?, ?, ?, ?)
""", clients_data)

# Insert Properties (50 properties)
properties_data = []
for i in range(1, 51):
    address = f"{random.randint(100, 9999)} {random.choice(streets)}"
    city, state, zip_code = random.choice(cities)
    
    prop_type = random.choice(property_types)
    
    # Price based on property type and city
    base_price = {
        'house': random.randint(300000, 1500000),
        'condo': random.randint(150000, 600000),
        'townhouse': random.randint(250000, 800000),
        'apartment': random.randint(100000, 400000)
    }
    price = base_price[prop_type]
    
    bedrooms = random.randint(1, 6)
    bathrooms = random.choice([1, 1.5, 2, 2.5, 3, 3.5, 4])
    sqft = random.randint(800, 5000)
    year_built = random.randint(1960, 2024)
    status = random.choice(['available', 'pending', 'sold'])
    listing_date = random_date(2023, 2025)
    agent_id = random.randint(1, 15)
    
    properties_data.append((i, address, city, state, zip_code, price, bedrooms, 
                           bathrooms, sqft, year_built, prop_type, status, listing_date, agent_id))

cursor.executemany("""
    INSERT INTO Properties (property_id, address, city, state, zip_code, price, bedrooms, 
                           bathrooms, sqft, year_built, property_type, status, listing_date, agent_id)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", properties_data)

# Insert Transactions (30 transactions for sold properties)
sold_properties = [p for p in properties_data if p[11] == 'sold']
transactions_data = []
for i, prop in enumerate(sold_properties[:30], 1):
    property_id = prop[0]
    agent_id = prop[13]
    buyer_id = random.randint(1, 50)
    seller_id = random.randint(1, 50)
    while seller_id == buyer_id:
        seller_id = random.randint(1, 50)
    
    # Sale price is around the listing price (±10%)
    listing_price = prop[5]
    sale_price = round(listing_price * random.uniform(0.90, 1.05), 2)
    sale_date = random_date(2024, 2025)
    
    # Find agent commission rate
    agent_commission = next((a[6] for a in agents_data if a[0] == agent_id), 0.03)
    commission = round(sale_price * agent_commission, 2)
    
    transactions_data.append((i, property_id, agent_id, buyer_id, seller_id, sale_price, sale_date, commission))

cursor.executemany("""
    INSERT INTO Transactions (transaction_id, property_id, agent_id, buyer_id, seller_id, 
                             sale_price, sale_date, commission)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", transactions_data)

# Insert Showings (80 showings)
showings_data = []
for i in range(1, 81):
    property_id = random.randint(1, 50)
    agent_id = random.randint(1, 15)
    client_id = random.randint(1, 50)
    showing_date = random_date(2024, 2025)
    feedback = random.choice(feedback_options)
    rating = random.randint(1, 5)
    
    showings_data.append((i, property_id, agent_id, client_id, showing_date, feedback, rating))

cursor.executemany("""
    INSERT INTO Showings (showing_id, property_id, agent_id, client_id, showing_date, feedback, rating)
    VALUES (?, ?, ?, ?, ?, ?, ?)
""", showings_data)

# Commit and close
conn.commit()
conn.close()

print("✅ Database 'real_estate.db' created successfully!")
print("\n📊 Tables created:")
print("   - Agents (15 records)")
print("   - Clients (50 records)")
print("   - Properties (50 records)")
print("   - Transactions (30 records)")
print("   - Showings (80 records)")
print("\n🎯 You can now practice SQL queries using this database!")
