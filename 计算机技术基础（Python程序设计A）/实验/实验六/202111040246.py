from re import I
import matplotlib.pyplot as plt
import numpy as np

def mcpic(i):
    responce = eval('mcpic' + str(i))
    return responce
mcpic1 = plt.imread('yanda.jpg')
mcpic2 = 255 - mcpic1
mcpic3 = 0.5*mcpic1 + (256*0.25-1)
mcpic4 = 0.25*mcpic1
mcpic5 = (100/255) * mcpic1 + 150
mcpic6 = 255*(mcpic1/255)**2
mcpic7 = np.flip(mcpic1,0)
mcpic8 = np.flip(mcpic1,1)

plt.figure(figsize=(12,12))
for i in range(1,9):
    plt.subplot(4,2,i)
    plt.imshow(mcpic(i).astype('uint8'))
plt.show()