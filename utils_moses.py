''' ITERATION 1

Module: Quantum Leap - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Process:

We don't write code from top to bottom; instead, we often write it from the outside in.
Here's what a first draft of my utils_case.py might look like:

1. I start with this docstring at the very beginning.
   I use it to clarify the purpose of my Python file and organize my thoughts.
   
2. I'll declare a global variable for my byline string and just set it to some simple text.

3. I'll declare a main() function for my module. When I run this script, I can use main() to test my byline.

4. I'll add the boilerplate conditional execution code so I only run the main() function when 
   this script is executed directly (but not when I import it into another file).

I'll test it in an online interpreter to ensure this version runs correctly before continuing.
'''

#####################################
# Declare a global variable named byline.
#####################################

byline: str = "Quantum Leap: Delivering Professional Insights"



import statistics



has_international_clients: bool = True
years_in_operation: int = 10
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.73]
is_pet_friendly: bool = False
number_of_employees: int = 50
programming_languages: list = ["Python", "R", "SQL"]
recent_scores: list = [95, 88, 92, 90, 97]

# Calculate statistics for client satisfaction scores
min_score = float = min(client_satisfaction_scores)
max_score = float = max(client_satisfaction_scores)
mean_score = float = statistics.mean(client_satisfaction_scores)
stdev_score = float = statistics.stdev(client_satisfaction_scores)

# Calculate statistics for recent scores
min_score = min(recent_scores)
max_score = max(recent_scores)
mean_score = statistics.mean(recent_scores)
stdev_score = statistics.stdev(recent_scores)

byline = f"""
Quantum Leap: Delivering Professional Insights

Has International Clients: {has_international_clients}
Years in Operation: {years_in_operation}
Skills Offered: {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
Is pet friendly: {is_pet_friendly}
Programming Languages: {programming_languages}
Number of employees: {number_of_employees}
Recent Score: {recent_scores}
Minimum Satisfaction Score:    {min_score}
Maximum Satisfaction Score:    {max_score}
Mean Satisfaction Score:       {mean_score:.2f}
Standard Deviation of Satisfaction Scores: {stdev_score:.2f}

Recent Scores Statistics:
Minimum Score: {min_score:.2f}
Maximum Score: {max_score:.2f}
Mean Score: {mean_score:.2f}
Standard Deviation: {stdev_score:.2f}

"""

####################################
# Define the get_byline() Function
###################################

def get_byline() -> str:
    """ Return the byline for my analytics project. """
    return byline 

#####################################
# Define a main() function for this module.
#####################################
    
# Create a function named main.
# A function is a block of code that performs a specific task.
# This function will simply print the byline to the console.
# Add a type hint to indicate that this function doesn't return anything when called 
# (that is, it has a Python type of None).
# It doesn't need any additional information passed in, 
# so there's nothing needed inside the parentheses.
# Everything afer the colon (:) must be indented (usually 4 spaces)

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()