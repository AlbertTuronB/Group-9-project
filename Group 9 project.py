from matplotlib import pyplot as plt

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
days = 365

for n in range(1, days):
    if S[n-1]/I[n-1]>= 1:
        S.append(S[n-1]-Ro*I[n-1])
        R.append(R[n-1]+I[n-1]/T)
        I.append(I[n-1]+Ro*I[n-1]-I[n-1]/T)
    else:
        S.append(S[n - 1] - Ro * S[n - 1] * S[n - 1]/I[n - 1])
        R.append(R[n - 1] + I[n - 1] / T)
        I.append(I[n - 1] + Ro * S[n - 1] * S[n - 1]/I[n - 1] - I[n - 1] / T)
print(list(map(round,I)))

plt.plot(S, label="Susceptible")
plt.plot(I, label="Infected")
plt.plot(R, label="Recovered")
plt.xlabel("Days")
plt.ylabel("Number of individuals")
plt.title("Virus simulation")
plt.legend(loc="best")
plt.show()
