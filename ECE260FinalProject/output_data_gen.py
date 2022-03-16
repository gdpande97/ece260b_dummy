q_file = open('qdata.txt', 'r')
k_file = open('kdata.txt', 'r')

q_file.readline()
k_file.readline()
q_file.readline()
k_file.readline()
q_file.readline()
k_file.readline()
q_file.readline()
k_file.readline()

q_lines = q_file.readlines()
k_lines = k_file.readlines()
q_data = []
k_data = []
count = 0
for line in q_lines:
    q_temp = line.split()
    q_data.append(q_temp)
    count = count + 1

count = 0
for line in k_lines:
    k_temp = line.split()
    k_data.append(k_temp)
    count = count + 1


# print("q_data\n \n \n")
# for x in range(len(q_data)):
#     print(q_data[x])

# print("\n \n \n k_data\n \n \n")
# for x in range(len(k_data)):
#     print(k_data[x])


p_data = []

for i in range(8):
    for x in range(len(q_data[i])):
        p_temp = p_temp + q_data[i][x] * k_data[i][x]