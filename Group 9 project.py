import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def DictionaryChoiceFunction():

    RValueDictionary = {
        'Virus':'R0 value',
        '1: Measles':15,
        '2: Chicken Pox':11,
        '3: Mumps':11,
        '4: Rubella':6.5,
        '5: Covid-19 (Delta Variant)':6.5,
        '6: Polio':6,
        '7: Smallpox':4.75,
        '8: COVID-19(Alpha Variant)':4.5,
        '9: HIV/AIDS':3.5,
        '10: SARS':3,
        '11: Common Cold':2.5,
        '12: Ebola':1.8,
        '13: Seasonal Influenza':1.3,
        '14: Andes Hantavirus':1.2,
        '15: Nipah Virus':0.5,
        '16: MERS':0.5,
        }

    DictChoice = ''

    for virus,value in RValueDictionary.items():
        print(virus,':',value)

    while DictChoice.lower() != 'yes' or DictChoice.lower() != 'no':
        

        DictChoice = input('Would you like to use one of these R0 values?\nType "yes" if so or "no" to input your own\n')
            
        if DictChoice.lower() == 'yes':
            UsingDict = 1
            break
        elif DictChoice.lower() == 'no':
            UsingDict = 0
            break
        else:
            print('Enter yes or no')
            continue
       
    print(UsingDict)

    if UsingDict == 1:
        VirusChoice = 0
        LoopTest = 0
        RValues = RValueDictionary.values()
        RValueList = list(RValues)
        while LoopTest == 0:
            try:
                VirusChoice = int(input('Input the number of the virus you want to use '))
                if VirusChoice <= 0:
                    print('Enter a number listed')
                    continue
                elif VirusChoice >= 17:
                    print('Enter a number listed')
                    continue
                else:
                    LoopTest = 1
            except:
                print('Enter a number listed')
                continue
        R0 = RValueList[VirusChoice]    
        print('Your R0 is',R0)
    else:
        R0 = 0
        while R0 == 0:
            try:
                R0 = float(input('Enter the R0 you want to use '))
            except:
                print('The R0 must be a number')
                continue
        print('Your R0 is',R0)

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
    
    Restart()

def Restart():
    again = input("Would you like to make another simulation? ")
    if again == "yes" or again == "y":
        print("\n")
        main_function()
    elif again == "no" or again == "n":
        print("\nSee ya!")
    else:
        print("Invalid input")
        Restart()

main_function()
