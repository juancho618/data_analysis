import numpy as np

x = [i for i in range(2001)]
x = np.asanyarray(x, dtype=int)
np.savetxt("tweetsList.csv", x, fmt='%i',delimiter=",")