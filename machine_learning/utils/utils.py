import matplotlib.pyplot as plt


#Scatter with line
#line values are passed within the array "pred"
def scatter_data(x, y, pred = None, test_data = None):
    plt.scatter(x,y)
    if not pred==None:
        #prediction line
        plt.plot(pred[0], pred[1], color="red")
    if not test_data == None:
        plt.scatter(test_data[0], test_data[1], color="red")
    plt.show()