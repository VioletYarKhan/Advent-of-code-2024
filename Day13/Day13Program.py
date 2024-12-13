from math import gcd
from itertools import product
import regex as re
import time
import numpy as np


D13I = open("/Users/nicholas/Desktop/Advent of Code 2024/Day13/Day13Input.txt", "r").read()

start_time = time.time()

machines = []
machine_data = []
lines = D13I.splitlines()
for i in range(len(lines)):
    machine_data.append(re.findall('\d{1,10}', lines[i]))
    if i%4 == 3:
        machines.append({'A': {'X': int(machine_data[0][0]), 'Y': int(machine_data[0][1])}, 'B': {'X': int(machine_data[1][0]), 'Y': int(machine_data[1][1])}, 'Prize': {'X': int(machine_data[2][0])+10000000000000, 'Y': int(machine_data[2][1])+10000000000000}})
        machine_data = []
machines.append({'A': {'X': int(machine_data[0][0]), 'Y': int(machine_data[0][1])}, 'B': {'X': int(machine_data[1][0]), 'Y': int(machine_data[1][1])}, 'Prize': {'X': int(machine_data[2][0])+10000000000000, 'Y': int(machine_data[2][1])+10000000000000}})

def solve_system(a1, b1, c1, a2, b2, c2):
    # a1*a + b1*b = c1
    # a2*a + b2*b = c2

    button_vectors = np.array([[a1, b1], [a2, b2]])
    prize_pos = np.array([c1, c2])
    
    sol = np.linalg.solve(button_vectors, prize_pos)
    solutions = []
    if all(round(item, 0) == round(item, 3) for item in sol):
        solutions.append((int(round(sol[0], 0)), int(round(sol[1], 0))))
    

    return solutions

def claw_machine_solver(machines):
    total_prizes = 0
    total_cost = 0
    m = 1
    for machine in machines:
        machine_start_time = time.time()
        a_x, b_x, p_x = machine['A']['X'], machine['B']['X'], machine['Prize']['X']
        a_y, b_y, p_y = machine['A']['Y'], machine['B']['Y'], machine['Prize']['Y']

        solutions = solve_system(a_x, b_x, p_x, a_y, b_y, p_y)
        if(len(solutions) > 1):
            print(solutions)
            print(min((3 * a + b, a, b) for a, b in solutions)[0])
        if solutions:
            cost = min((3 * a + b, a, b) for a, b in solutions)[0]
            total_prizes += 1
            total_cost += cost
        print(f'Machine: {m}/{len(machines)} \n Time: {time.time()-machine_start_time} \n Total Time: {time.time()-start_time}')
        m += 1
        
    return total_prizes, total_cost


prizes, cost = claw_machine_solver(machines)
print(f"Prizes won: {prizes}")
print(f"Minimum cost: {cost}")
print(str(time.time()-start_time) + " seconds")