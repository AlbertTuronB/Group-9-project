from matplotlib import pyplot as plt

def main_function():
    
    S = 0
    I = 0
    Ro = 0
    R = [0]
    T = 0
    days = 0
    
    while S == 0:
        try:
            S = [int(input('Enter the number of individuals susceptible to the virus '))]
        except:
            print('Enter a whole number')
            continue
   
    while I == 0:
       try:
           I = [int(input('Enter the number of infected individuals at the start '))]
       except:
           print('Enter a whole number')
           continue

    while Ro == 0:
         try:
             Ro = float(input('Enter the R value of the virus '))
         except:
             print('Enter a number')
             continue
    
    while T == 0:
        try:
            T = float(input('Enter the average recovery time of the virus  '))
        except:
            print('Enter a number')
            continue 
        
    while  days == 0: 
        try:
            days = float(input('Enter how many days to simulate for '))
        except:
            print('Enter a number')
            continue
        
    print(S,I,Ro,R,T,days)
    
    ActVac = 0.01

    Simulation_without_vaccine(S, I, R, Ro, T, days)
    Simulation_with_active_vaccinating(S, I, R, Ro, T, days, ActVac)
    Restart()    
    
def Simulation_without_vaccine(S, I, R, Ro, T, days):
    for n in range(1, days):
        if S[n - 1] / I[n - 1] >= 1:
            S.append(S[n - 1] - Ro * I[n - 1])
            R.append(R[n - 1] + I[n - 1] / T)
            I.append(I[n - 1] + Ro * I[n - 1] - I[n - 1] / T)
        else:
            S.append(S[n - 1] - Ro * S[n - 1] * S[n - 1] / I[n - 1])
            R.append(R[n - 1] + I[n - 1] / T)
            I.append(I[n - 1] + Ro * S[n - 1] * S[n - 1] / I[n - 1] - I[n - 1] / T)
    print(list(map(round, I)))

    plt.plot(S, label="Susceptible")
    plt.plot(I, label="Infected")
    plt.plot(R, label="Recovered")
    plt.xlabel("Days")
    plt.ylabel("Number of individuals")
    plt.title("Virus simulation")
    plt.legend(loc="best")
    plt.show()


def Simulation_with_active_vaccinating(S, I, R, Ro, T, days, ActVac):
    for n in range(1, days):
        if S[n - 1] / I[n - 1] >= 1:
            S.append(S[n - 1] - Ro * I[n - 1] - ActVac * S[n - 1])
            R.append(R[n - 1] + I[n - 1] / T)
            I.append(I[n - 1] + Ro * I[n - 1] - I[n - 1] / T)
        else:
            S.append(S[n - 1] - Ro * S[n - 1] * S[n - 1] / I[n - 1] - ActVac * S[n - 1])
            R.append(R[n - 1] + I[n - 1] / T)
            I.append(I[n - 1] + Ro * S[n - 1] * S[n - 1] / I[n - 1] - I[n - 1] / T)
    print(list(map(round, I)))

    plt.plot(S, label="Susceptible")
    plt.plot(I, label="Infected")
    plt.plot(R, label="Recovered")
    plt.xlabel("Days")
    plt.ylabel("Number of individuals")
    plt.title("Virus simulation")
    plt.legend(loc="best")
    plt.show()


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
