import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def main_function():
    N = 0
    I0 = 0
    R0 = 0
    beta = 0
    gamma = 0
    days = 0

    while N == 0:
        try:
            N = int(input('Enter the population number '))
        except:
            print('Enter a whole number')
            continue

    while I0 == 0:
        try:
            I0 = int(input('Enter the number of infected individuals at the start '))
        except:
            print('Enter a whole number')
            continue

    while beta == 0:
        try:
            beta = float(input('Enter effective contact rate beta (The number of cases caused '
                               'by one infected individual, effectively, in a unit time) (0.0 - 1.0) '))
        except:
            print('Enter a number')
            continue

    while gamma == 0:
        try:
            gamma = float(input('Rate of removal (0.0 - 1.0) '))
        except:
            print('Enter a number')
            continue

    while days == 0:
        try:
            days = float(input('Enter how many days to simulate for '))
        except:
            print('Enter a number')
            continue

    S0 = N - I0 - R0

    Virus_simulation(N, S0, I0, R0, beta, gamma, days)


def Virus_simulation(N, S0, I0, R0, beta, gamma, days):
    # A grid of time points (in days)
    t = np.linspace(0, days, num=int(days))

    # The SIR model differential equations.
    def model(y, t, N, beta, gamma):
        S, I, R = y
        dSdt = -beta * S * I / N
        dIdt = beta * S * I / N - gamma * I
        dRdt = gamma * I
        return dSdt, dIdt, dRdt

    # Initial conditions vector
    y0 = S0, I0, R0
    # Integrate the SIR equations over the time grid, t.
    # The array "result" is a two dimensional array of the shape [number of days, 3] where
    # 3 corresponds to three initialization conditions
    result = odeint(model, y0, t, args=(N, beta, gamma))
    S, I, R = result.T


    # Calculate R0 of the virus
    R_0_virus = beta * 1/gamma
    print(f"Ro of this virus is {str(R_0_virus)}")
    print("Note that although the curve may not look this big the final amount of people infected by the virus "
            "is significant proportion from the population")

    # Plot the data on three separate curves for S(t), I(t) and R(t)
    fig = plt.figure(facecolor='w')
    ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
    ax.plot(t, S, 'b', label='Susceptible')
    ax.plot(t, I, 'r', label='Infected')
    ax.plot(t, R, 'g', label='Recovered with immunity')
    ax.set_xlabel('Time (days)')
    ax.set_ylabel('Number')
    ax.set_ylim(0, N+200)
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    for spine in ('top', 'right', 'bottom', 'left'):
        ax.spines[spine].set_visible(False)
    plt.show()

    #Asks user if it wants to know a certain value of the variables
    while True:
        try:
            Search = input("Do you want to search for a certain value? (y/n)")
            if Search == "y":
                value = input("In which variable are you interested: I (infected), S (susceptible) or R (recovered)? ")
                day = input("In which day would you like to know the value of the variable? (if 0 is day 1)")
                if value == "S":
                    print(result[int(day)][0])
                elif value == "I":
                    print(result[int(day)][1])
                elif value == "R":
                    print(result[int(day)][2])
                continue
            if Search == "n":
                break
        except ValueError:
            print("Invalid")
            continue


main_function()
