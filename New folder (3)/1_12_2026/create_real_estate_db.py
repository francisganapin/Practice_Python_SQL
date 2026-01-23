"""
Real Estate Pricing Database with Agents
Run this first to create the database!
"""

import sqlite3

def create_database():
    conn = sqlite3.connect('real_estate.db')
    cursor = conn.cursor()
    
    # Drop existing tables
    cursor.execute("DROP TABLE IF EXISTS transactions")
    cursor.execute("DROP TABLE IF EXISTS properties")
    cursor.execute("DROP TABLE IF EXISTS agents")
    cursor.execute("DROP TABLE IF EXISTS offices")
    
    # Create offices table
    cursor.execute('''
        CREATE TABLE offices (
            office_id INTEGER PRIMARY KEY,
            office_name TEXT NOT NULL,
            city TEXT NOT NULL,
            state TEXT NOT NULL
        )
    ''')
    
    # Create agents table
    cursor.execute('''
        CREATE TABLE agents (
            agent_id INTEGER PRIMARY KEY,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT,
            hire_date DATE,
            commission_rate DECIMAL(4,2),
            office_id INTEGER,
            is_active INTEGER DEFAULT 1,
            FOREIGN KEY (office_id) REFERENCES offices(office_id)
        )
    ''')
    
    # Create properties table
    cursor.execute('''
        CREATE TABLE properties (
            property_id INTEGER PRIMARY KEY,
            address TEXT NOT NULL,
            city TEXT NOT NULL,
            bedrooms INTEGER,
            bathrooms DECIMAL(3,1),
            square_feet INTEGER,
            list_price DECIMAL(12,2),
            listing_date DATE,
            status TEXT,
            agent_id INTEGER,
            FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
        )
    ''')
    
    # Create transactions table
    cursor.execute('''
        CREATE TABLE transactions (
            transaction_id INTEGER PRIMARY KEY,
            property_id INTEGER,
            agent_id INTEGER,
            sale_price DECIMAL(12,2),
            sale_date DATE,
            days_on_market INTEGER,
            FOREIGN KEY (property_id) REFERENCES properties(property_id),
            FOREIGN KEY (agent_id) REFERENCES agents(agent_id)
        )
    ''')
    
    # Insert offices
    offices = [
        (1, 'Downtown Realty', 'Los Angeles', 'CA'),
        (2, 'Coastal Properties', 'San Diego', 'CA'),
        (3, 'Metro Real Estate', 'San Francisco', 'CA'),
        (4, 'Valley Homes', 'Phoenix', 'AZ')
    ]
    cursor.executemany('INSERT INTO offices VALUES (?,?,?,?)', offices)
    
    # Insert agents
    agents = [
        (1, 'John', 'Smith', 'john@realty.com', '2019-03-15', 3.0, 1, 1),
        (2, 'Sarah', 'Johnson', 'sarah@realty.com', '2018-07-20', 3.5, 1, 1),
        (3, 'Michael', 'Williams', 'mike@realty.com', '2020-01-10', 2.5, 2, 1),
        (4, 'Emily', 'Brown', 'emily@realty.com', '2017-05-25', 4.0, 2, 1),
        (5, 'David', 'Garcia', 'david@realty.com', '2016-09-12', 3.5, 3, 1),
        (6, 'Jessica', 'Martinez', 'jess@realty.com', '2021-02-28', 2.0, 3, 0),
        (7, 'Robert', 'Anderson', 'rob@realty.com', '2019-11-30', 3.0, 4, 1),
        (8, 'Amanda', 'Taylor', 'amanda@realty.com', '2022-01-05', 2.5, 4, 1)
    ]
    cursor.executemany('INSERT INTO agents VALUES (?,?,?,?,?,?,?,?)', agents)
    
    # Insert properties
    properties = [
        (1, '123 Main St', 'Los Angeles', 4, 2.5, 2200, 850000, '2024-01-15', 'Sold', 1),
        (2, '456 Oak Ave', 'Los Angeles', 2, 2.0, 1100, 525000, '2024-02-20', 'Sold', 2),
        (3, '789 Palm Dr', 'San Diego', 3, 2.0, 1800, 725000, '2024-01-05', 'Sold', 3),
        (4, '321 Beach Blvd', 'San Diego', 3, 2.5, 1600, 615000, '2024-03-10', 'Active', 4),
        (5, '555 Market St', 'San Francisco', 1, 1.0, 750, 495000, '2024-02-28', 'Sold', 5),
        (6, '777 Hill Rd', 'San Francisco', 5, 3.5, 3200, 1450000, '2024-01-20', 'Sold', 5),
        (7, '888 Desert Way', 'Phoenix', 4, 3.0, 2800, 485000, '2024-03-01', 'Pending', 7),
        (8, '999 Cactus Ln', 'Phoenix', 3, 2.0, 1900, 365000, '2024-02-15', 'Sold', 7),
        (9, '111 Mountain Ave', 'Los Angeles', 4, 2.5, 2400, 920000, '2024-01-25', 'Sold', 1),
        (10, '222 Peak St', 'San Diego', 2, 2.0, 1400, 545000, '2024-03-05', 'Active', 3)
    ]
    cursor.executemany('INSERT INTO properties VALUES (?,?,?,?,?,?,?,?,?,?)', properties)
    
    # Insert transactions
    transactions = [
        (1, 1, 1, 835000, '2024-03-20', 64),
        (2, 2, 2, 515000, '2024-04-15', 54),
        (3, 3, 3, 710000, '2024-03-10', 64),
        (4, 5, 5, 485000, '2024-04-25', 56),
        (5, 6, 5, 1400000, '2024-04-01', 71),
        (6, 8, 7, 358000, '2024-04-10', 54),
        (7, 9, 1, 905000, '2024-04-05', 70)
    ]
    cursor.executemany('INSERT INTO transactions VALUES (?,?,?,?,?,?)', transactions)
    
    conn.commit()
    conn.close()
    print("✅ Database 'real_estate.db' created!")
    print("\nTables: offices(4), agents(8), properties(10), transactions(7)")

if __name__ == '__main__':
    create_database()
