survey_results = [
    {"name": "Amit", "Q1": "Yes", "Q2": "Yes", "Q3": "Yes"},
    {"name": "Priya", "Q1": "Yes", "Q2": "Yes", "Q3": "Yes"},
    {"name": "Rahul", "Q1": "Yes", "Q2": "No", "Q3": "Yes"},
    {"name": "Sneha", "Q1": "Yes", "Q2": "Yes", "Q3": "Yes"},
]

# List how many answered "Yes" to all questions
yes_to_all = [
    person["name"]
    for person in survey_results
    if all(answer == "Yes" for q, answer in person.items() if q != "name")
]
print(f"People who answered 'Yes' to all questions: {yes_to_all}")
print(f"Total: {len(yes_to_all)}")

# List who answered "No" to any question
no_to_any = [
    person["name"]
    for person in survey_results
    if any(answer == "No" for q, answer in person.items() if q != "name")
]
print(f"People who answered 'No' to any question: {no_to_any}")
print(f"Total: {len(no_to_any)}") 


