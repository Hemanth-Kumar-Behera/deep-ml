import math

PI = 3.14159

def power_grid_forecast(consumption_data):
    # 1) Subtract the daily fluctuation (10 * sin(2π * i / 10)) from each data point.
    # 2) Perform linear regression on the detrended data.
    # 3) Predict day 15's base consumption.
    # 4) Add the day 15 fluctuation back.
    # 5) Round, then add a 5% safety margin (rounded up).
    # 6) Return the final integer.
    
    x=list(range(1,11))
    n=len(consumption_data)
    #Removing the fluctuation
    y=[]
    for i in range(len(consumption_data)):
        f=10*math.sin(2*PI*i/10)
        y.append(consumption_data[i]-f)
   
    #calculate average for linear regression
    #m=sum(x[i]-xmean)*(y[i]-ymean i in range(len))/(x[i]-xmean)**2
    #b=ymean-mxmean
    x_mean=sum(x)/n
    y_mean=sum(y)/n
    num=sum((x[i]-x_mean)*(y[i]-y_mean) for i in range(n))
    den=sum((x[i]-x_mean)**2 for i in range(n))
    m=num/den
    b=y_mean-x_mean*m
    prediction=m*(15)+b
    fluctuation_15=10*math.sin(2*PI*15/10)
    prediction+=fluctuation_15
    prediction=round(prediction)
    answer=math.ceil(prediction*1.05)
    return answer
    pass