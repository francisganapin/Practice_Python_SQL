import json
import random
from datetime import datetime, timedelta

def generate_mongo_data():
    first_names = ['John', 'Jane', 'Michael', 'Emily', 'David', 'Sarah', 'Robert', 'Jessica', 'William', 'Ashley', 'James', 'Mary', 'Christopher', 'Amanda', 'Joseph', 'Jennifer']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez', 'Hernandez', 'Lopez', 'Gonzalez', 'Wilson', 'Anderson', 'Thomas']
    departments = ['Engineering', 'HR', 'Sales', 'Marketing', 'Finance']
    skills_pool = ['Python', 'Java', 'C++', 'SQL', 'MongoDB', 'React', 'Node.js', 'AWS', 'Docker', 'Kubernetes', 'Excel', 'PowerBI', 'Communication', 'Management']
    cities = ['New York', 'San Francisco', 'Chicago', 'Los Angeles', 'Boston', 'Austin', 'Seattle']
    
    employees = []
    
    for i in range(1, 101): # 100 employees
        first = random.choice(first_names)
        last = random.choice(last_names)
        
        # Embedded Address
        address = {
            "street": f"{random.randint(100, 999)} {random.choice(['Main', 'Broadway', 'Park', 'Oak', 'Pine'])} St",
            "city": random.choice(cities),
            "zip": f"{random.randint(10000, 99999)}"
        }
        
        # Array of Skills
        num_skills = random.randint(1, 5)
        skills = random.sample(skills_pool, num_skills)
        
        # Array of Embedded Documents (Experience)
        experience = []
        num_jobs = random.randint(0, 3)
        for _ in range(num_jobs):
            exp = {
                "company": f"Company {random.choice(['A', 'B', 'C', 'D', 'E'])}",
                "role": random.choice(['Junior Dev', 'Senior Dev', 'Manager', 'Analyst']),
                "years": random.randint(1, 5)
            }
            experience.append(exp)
            
        employee = {
            "_id": i,
            "name": f"{first} {last}",
            "age": random.randint(22, 60),
            "email": f"{first.lower()}.{last.lower()}@example.com",
            "department": random.choice(departments),
            "salary": random.randint(50000, 180000),
            "address": address,
            "skills": skills,
            "experience": experience,
            "isActive": random.choice([True, True, True, False]), # Mostly active
            "joinDate": (datetime.now() - timedelta(days=random.randint(0, 365*5))).isoformat()
        }
        employees.append(employee)

    with open('employees.json', 'w') as f:
        json.dump(employees, f, indent=4)
    
    print(f"Successfully generated {len(employees)} employee records in 'employees.json'.")

if __name__ == '__main__':
    generate_mongo_data()
