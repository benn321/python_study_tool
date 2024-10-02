

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 12:32:16 2024

@author: benshea
"""

import io
import random
import sys

with open("/Users/benshea/Desktop/Python/Python Automatic Practice/Python_Practice_Problems.py", "r") as f:
    problems = f.read()
    problem_set = []
    start_of_prob = -1
    target = "#"
    is_end = False
    
    for i, char in enumerate(problems):
        if char == target and is_end:
           problem = problems[start_of_prob: i]
           problem_set.append(problem)
           start_of_prob = i
           
        elif char == target:
               start_of_prob = i
               is_end = True
           
         
               
         
    while True:
        question_amount = input("How many problems would you like to attempt (1-100).\n")
        
        try:
            question_amount = int(question_amount)
        except ValueError:
           print("The string does not contain a valid integer..\n")
           continue
       
        if  1 <= int(question_amount) <= 100:
            
            break
        else:
            print("Not in valid range.\n")

        
    random.shuffle(problem_set)
    problem_set = problem_set[0: question_amount]
    total_correct = 0
    total_questions = len(problem_set)
    

    count = 1
    for prob in problem_set:
        print("\n")
        print("Problem ", count)
        count += 1
        old_stdout = sys.stdout
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        # Compile and execute the code snippet
        code_obj = compile(prob, '<string>', 'exec')
        local_context = {}
        exec(code_obj, {}, local_context)

        # Reset stdout
        sys.stdout = old_stdout
        output = str(new_stdout.getvalue()).strip()
        response = str(input(prob)).strip()
        
        if response.replace(" ", "") == output.replace(" ", ""):
            print("Correct!.\n")
            total_correct += 1
        else:
            print("Sorry, the correct answer is:", output)
            print(".\n")



print(f"\nYou got {total_correct} out of {total_questions} correct!")