import random
import math


def calculate_attacks(board):
    attacks = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == j - i:
                attacks += 1
    return attacks


def generate_initial_state(n):
    return [random.randint(0, n - 1) for _ in range(n)]


def display_board(board):
    n = len(board)
    for row in range(n):
        line = "".join("Q " if board[col] == row else ". " for col in range(n))
        print(line)
    print()


def get_neighbors(board):
    neighbors = []
    n = len(board)
    for col in range(n):
        for row in range(n):
            if row != board[col]:  
                new_board = board[:]
                new_board[col] = row
                neighbors.append(new_board)
    return neighbors


def hill_climbing(n):
    
    current_board = generate_initial_state(n)
    current_cost = calculate_attacks(current_board)
    
    print("Initial board (Hill Climbing):")
    display_board(current_board)
    
    
    while current_cost > 0:
        adjacent_states = get_neighbors(current_board)
        best_neighbor = None
        best_cost = current_cost
        
        
        for neighbor in adjacent_states:
            neighbor_cost = calculate_attacks(neighbor)
            if neighbor_cost < best_cost:
                best_neighbor = neighbor
                best_cost = neighbor_cost
        
        
        if best_cost == current_cost:
            break
        
        
        current_board = best_neighbor
        current_cost = best_cost
        
        print(f"Move to new board with {current_cost} attacks:")
        display_board(current_board)
    
    if current_cost == 0:
        print("Solution found!")
    else:
        print("No solution found.")
    
    return current_board, current_cost


def simulated_annealing(n, initial_temperature=1000, cooling_rate=0.95, max_iterations=50):
    current_board = generate_initial_state(n)
    current_cost = calculate_attacks(current_board)
    temperature = initial_temperature

    print("Initial board (Simulated Annealing):")
    display_board(current_board)

    for iteration in range(max_iterations):
        if current_cost == 0:
            print("Solution found!")
            break

        adjacent_states = get_neighbors(current_board)
        
       
        best_neighbor = min(adjacent_states, key=calculate_attacks)
        best_cost = calculate_attacks(best_neighbor)

        delta_cost = best_cost - current_cost
        
        
        if delta_cost < 0 or random.random() < math.exp(-delta_cost / max(temperature, 1e-10)):
            current_board = best_neighbor
            current_cost = best_cost

            print(f"Move to new board with {current_cost} attacks (iteration {iteration + 1}):")
            display_board(current_board)

        temperature *= cooling_rate

    if current_cost != 0:
        print(f"Finished without finding perfect solution. Final attacks: {current_cost}")
    
    return current_board, current_cost



n = 4  


print("\nRunning Hill Climbing...")
hill_solution, hill_attacks = hill_climbing(n)


print("\nRunning Simulated Annealing...")
sa_solution, sa_attacks = simulated_annealing(n)
