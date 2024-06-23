import time
start_time = time.time()
a = 0

while a<100000:
    a+=1
    print(a)

end_time = time.time()


elapsed_time = end_time - start_time
print(f"Temps écoulé : {elapsed_time} secondes")