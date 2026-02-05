#mean() function. It takes an array o numbers and calculates the mean value of them, the output is returned as a float rounded to 2 decimal points
class methods:
    @staticmethod
    def mean_f(data):
        n = len(data)
        total=sum(data)
        try:
            if n==0:
                print("Error: mean() requires at least one number")
        except:
            if type(data)==str:
                return True
        if n < 1:
            print('mean requires at least one data point')
        mean_v=total/n
        return (round(mean_v,2))
    #median function. It takes an array and finds it's median number
    @staticmethod
    def median_f(data):
        n = sorted(data)
        n_len = len(n)
        s=sum(data)
        try:
            if isinstance(data, int) or isinstance(data, float)==True:
                if n_len==0:
                    print("Median requires at least 1 number")
                return 0
        except False:
            print("TypeError: median_f() requires data to be either int or float") 

        if (n_len % 2==0):
            return round(sum(data)/n_len, 2)
        else:
            index = (n_len - 1) // 2
            median=n[index]
            return median
    #standard deviation function. It takes an array and calculates it's standard deviation value 
    @staticmethod  
    def std_deviationf(data):
        median=methods.median_f(data)
        

    #standard deviation function. It takes an array and calculates it's standard deviation value   
    @staticmethod
    def std_deviationf(data):
        pass



    

    def variancef(data):
        pass