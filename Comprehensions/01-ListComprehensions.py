import time

# even = []
#
# start = time.time()
#
# for i in range(10000000):
#     if i % 2 == 0:
#         even.append(i)
#
# end = time.time()
#
# print("Total Time", end-start)

start = time.time()

even = [i for i in range(10000000) if i % 2 == 0]

end = time.time()

print("Total Time",end-start)
