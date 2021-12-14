import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import time
import sys

def main_function():

    Inroduction_1()
    Introduction_to_simulation()
    RValueDictionary = {
        'Virus': 'R0 value',
        '1: Measles': 15,
        '2: Chicken Pox': 11,
        '3: Mumps': 11,
        '4: Rubella': 6.5,
        '5: Covid-19 (Delta Variant)': 6.5,
        '6: Polio': 6,
        '7: Smallpox': 4.75,
        '8: COVID-19(Alpha Variant)': 4.5,
        '9: HIV/AIDS': 3.5,
        '10: SARS': 3,
        '11: Common Cold': 2.5,
        '12: Ebola': 1.8,
        '13: Seasonal Influenza': 1.3,
        '14: Andes Hantavirus': 1.2,
        '15: Nipah Virus': 0.5,
        '16: MERS': 0.5,
    }

    DictChoice = ''

    for virus, value in RValueDictionary.items():
        print(virus, ':', value)

    while DictChoice.lower() != 'yes' or DictChoice.lower() != 'no':

        DictChoice = input(
            'Would you like to use one of these R0 values?\nType "yes" if so or "no" to input your own\n')

        if DictChoice.lower() == 'yes':
            UsingDict = 1
            break
        elif DictChoice.lower() == 'no':
            UsingDict = 0
            break
        else:
            print('Enter yes or no')
            continue

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
        R_0_virus = RValueList[VirusChoice]
        print('Your R0 is', R_0_virus)
    else:
        R_0_virus = 0
        while R_0_virus == 0:
            try:
                R_0_virus = float(input('Enter the R0 you want to use '))
            except:
                print('The R0 must be a number')
                continue
        print('Your R0 is', R_0_virus)

    N = 0
    I0 = 0
    R0 = -1
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

    while R0 < 0:
        try:
            R0 = int(input('Enter the number of individuals who are not susceptible to the virus at the start '))
        except:
            print('Enter a whole number')
            continue

    while gamma == 0:
        try:
            gamma_user = float(input('Period of days it takes an individual to recover from the virus '
                                     '(e.g for covid the nr is 14 days)'))
            gamma = 1 / gamma_user
        except:
            print('Enter a number')
            continue

    while days == 0:
        try:
            days = float(input('Enter how many days to simulate for '))
        except:
            print('Enter a number')
            continue

    beta = R_0_virus * gamma
    S0 = N - I0 - R0

    Virus_simulation(N, S0, I0, R0, beta, gamma, days)
    Restart()

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
    ax.set_ylim(0, N + 200)
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    for spine in ('top', 'right', 'bottom', 'left'):
        ax.spines[spine].set_visible(False)
    plt.show()

    # Asks user if it wants to know a certain value of the variables
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

def Introduction_to_simulation():
    print("Now that you have learned about the colourful facts and history about the viruses,")
    print("it is time to start simulating")
    print("")
    time.sleep(1)
    print("We will be using Kermack-McKendrick SIR model, that was developed in the early twentieth century.")
    print("The SIR stem from susceptible, infected, removed")
    print("In our initial simulation the number of susceptible is equal to # of population - # of infected")
    print("The removed are all the individuals, who cannot be affected due to immunity developed during the infection,")
    print(", immune due to vaccination, have died due to disease - ")
    print("all in all they do not play part in the spreading of the virus")
    print("")
    time.sleep(3)
    print("The model explains the rapid rise and fall in the number of infected patients observed in epidemics")
    print("It assumes that the population size is fixed (i.e., no births or deaths by other causes),")
    print("and incubation period of the infectious agent is instantaneous,")
    print("and duration of infectivity is same as length of the disease")
    print("It also assumes a completely homogeneous population with no age, spatial, or social structure.")
    time.sleep(5)
    print("Although SIR model makes some very big assumptions, it still works quite well in virus simulation.")
    print("Modern models also use the basis of SIR equations with added weigths to count for age and social structure")
    print("To see the equations we use for this simulation and further resources feel free to visit this website:")
    print("https://www.maa.org/press/periodicals/loci/joma/the-sir-model-for-spread-of-disease-the-differential-equation-model")
    time.sleep(3)
    print("")
    sim_introduction_continue = ""
    while sim_introduction_continue.lower() != 'yes' or sim_introduction_continue.lower() != 'no':
        sim_introduction_continue = input("Are you ready to start simulating now?\nType 'yes' or 'no'\n")
        if sim_introduction_continue.lower() == 'yes':
            break
        elif sim_introduction_continue.lower() == 'no':
            sys.exit(0)
        else:
            print('Enter yes or no')
            continue
    print("")

def Inroduction_1():
    print("Hi!")
    time.sleep(0.5)
    print("The last years have been defined by the outbreak of the coronavirus.")
    time.sleep(1)
    print("But viruses are nothing new, they existed 3.5 billion years before humans evolved on Earth.")
    time.sleep(1)
    print("They have played an important role in our evolution as close to 10% of the human genome")
    print("is their genetic material embedded in our own DNA.")
    time.sleep(1)
    print("Thanks to our current technology, we can easily simulate a spread of a virus in homologous environment.")
    print("")
    print("Today you'll learn about:")
    print("1) History and fun facts about different viruses.")
    print("2) What are the fundamental equations used to predict virus spread in today's world")
    print("3) What factors play key role in the spread of virus and how the curve can be flattened")
    time.sleep(3)

    introduction_continue = ""
    while introduction_continue.lower() != 'yes' or introduction_continue.lower() != 'no':
        introduction_continue = input("Are you ready to continue into the world of viruses?\nType 'yes' or 'no'\n")
        if introduction_continue.lower() == 'yes':
            break
        elif introduction_continue.lower() == 'no':
            sys.exit(0)
        else:
            print('Enter yes or no')
            continue

main_function()
