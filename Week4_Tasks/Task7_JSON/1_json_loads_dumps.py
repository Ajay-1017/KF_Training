import json

json_string = '''
{
  "company": {
    "name": "TechNova",
    "founded": 2018,
    "is_active": true,
    "headquarters": {
      "city": "Chennai",
      "country": "India",
      "address": {
        "street": "OMR Road",
        "zip_code": 600119
      }
    }
  },
  "employees": [
    {
      "id": 101,
      "name": "Ajay",
      "age": 22,
      "department": "Data Engineering",
      "skills": ["Python", "SQL", "Pandas", "ETL"],
      "salary": 650000,
      "manager": null
    },
    {
      "id": 102,
      "name": "Rahul",
      "age": 25,
      "department": "Backend",
      "skills": ["Python", "FastAPI", "Docker"],
      "salary": 850000,
      "manager": 101
    },
    {
      "id": 103,
      "name": "Priya",
      "age": 24,
      "department": "QA",
      "skills": ["Selenium", "Python"],
      "salary": 550000,
      "manager": 101
    }
  ],
  "projects": [
    {
      "project_id": "P001",
      "name": "ETL Pipeline",
      "status": "Completed",
      "technologies": ["Python", "SQL", "Airflow"]
    },
    {
      "project_id": "P002",
      "name": "Movie Recommendation",
      "status": "In Progress",
      "technologies": ["Python", "Machine Learning", "FastAPI"]
    }
  ],
  "benefits": {
    "health_insurance": true,
    "work_from_home": false,
    "leave_days": 24
  }
}
'''

# loads method -> loads JSON string into python object 

data = json.loads(json_string)
print(type(data)) # <class 'dict'>
print(type(data["employees"])) # <class 'list'>

for emp in data["employees"]:
    if emp['age'] > 23:
        print(emp['name'])
    


# dumps method -> dumps a python object into JSON string 

del[data['benefits']]
new_json_string = json.dumps(data,indent=2,sort_keys=True)

# indent ->  Pretty-print the JSON with 2 spaces of indentation
# sort_key -> Sort dictionary keys alphabetically in the output

print(new_json_string)
                

