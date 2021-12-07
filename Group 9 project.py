from matplotlib import pyplot as plt


def main_function():
    # number of individuals susceptible to virus
    S = [999]
    # number of individuals infected to virus
    I = [1]
    # number of individuals not able to contract virus due to having been infected and developed an immunity or
    # died due to infection
    R = [0]
    # how many infected on average stem from one infected
    Ro = 0.5
    # average recovery time
    T = 12
    # period of time over which the simulation is played
    days = 100
    # % of susceptible individuals getting vaccinated every day
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
