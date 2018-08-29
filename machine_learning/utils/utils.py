import matplotlib.pyplot as plt


#Scatter with line
#line values are passed within the array "pred"
def scatter_data(x, y, pred = None):
    plt.scatter(x,y)
    if not pred==None:
        #prediction line
        plt.plot(pred[0], pred[1], color="red")
    plt.show()