import numpy as np


consensus = np.loadtxt(open("conse.csv", "rb"), delimiter=",", skiprows=0)
consensus[consensus == 1] = 0

def get_average(matrix):
    sum = 0
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[0]):
            if i != j:
                sum += matrix[i][j]
                count += 1
    return (sum/count)
            

print(consensus[0,:])
#print(get_average(consensus)) #6.882

def get_noise_list(matrix):
    noise_list=[]
    for i in range(matrix.shape[0]):
        row = consensus[i,:]
        sumatory = sum(row)
        avg = (sumatory - 11)/2000
        if avg < 6.882:
            noise_list.append(i)
    return noise_list

res = get_noise_list(consensus)
print(len(res))
np.savetxt("noise.csv", res, fmt='%i',delimiter=",")
         