#generate initial layout
import numpy as np
import preprocessing

al = np.zeros(5,dtype=int)
ah_w = np.zeros(5,dtype=int)
ah_h = np.zeros(5,dtype=int)



a = np.zeros((12,35), dtype=int)

# number = input("input number of article")

i = 0
for i in range (1,5):
    print("input length of article ",+i)
    al[i] = input()
    print("input heigth of headline of article ",+i)
    ah_h[i] = input()
    print("input width of headline of article ",+i)
    ah_w[i] = input()



max_heigth, max_width = preprocessing.max_headline(1,4,ah_w,ah_h)
r, c =  preprocessing.find_initial_point(a,1)

print (max_heigth)
print (max_width)
print (4%2)

# al_1 = input("input length of article 1")
# al_2 = input("input length of article 2")
# al_3 = input("input length of article 3")
# al_4 = input("input length of article 4")

