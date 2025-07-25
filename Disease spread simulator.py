import matplotlib.pyplot as plt

# SIR Model parameters
total_population = 1000
initial_infected = 1
initial_recovered = 0
days = 100

# Infection and recovery rates
beta = 0.3   # Infection rate (probability of transmission)
gamma = 0.1   # Recovery rate (1/duration of infection)

# Initial conditions
S = [total_population - initial_infected - initial_recovered]  # Susceptible
I = [initial_infected]   # Infected
R = [initial_recovered]  # Recovered

# Simulation loop
for day in range(1, days):
    new_infected = beta * S[-1] * I[-1] / total_population
    new_recovered = gamma * I[-1]

    S_next = S[-1] - new_infected
    I_next = I[-1] + new_infected - new_recovered
    R_next = R[-1] + new_recovered

    S.append(S_next)
    I.append(I_next)
    R.append(R_next)

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(S, label='Susceptible', color='blue')
plt.plot(I, label='Infected', color='red')
plt.plot(R, label='Recovered', color='green')
plt.title("🦠 Disease Spread Simulation (SIR Model)")
plt.xlabel("Days")
plt.ylabel("Population")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

