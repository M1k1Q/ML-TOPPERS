import numpy as np



def main():
    sales_data = np.array([
        [200, 220, 250, 210, 180, 190],  # Day 1
        [230, 240, 260, 200, 195, 205],  # Day 2
        [210, 215, 255, 220, 185, 200],  # Day 3
        [205, 225, 270, 215, 190, 195],  # Day 4
        [215, 230, 265, 225, 200, 210],  # Day 5
        [225, 235, 275, 230, 205, 215],  # Day 6
        [235, 245, 280, 240, 210, 220],  # Day 7
        [245, 255, 290, 250, 215, 225],  # Day 8
        [255, 265, 300, 260, 220, 230],  # Day 9
        [265, 275, 310, 270, 225, 235]   # Day 10
    ])

    print("Question 1 \n")
    #q1
    #a
    total_sale_per_prod = np.sum(sales_data , axis = 0) #sum collumn wise, per product across 10 days , using axis = 0 
    print("total sales per product : " , total_sale_per_prod , "\n") 

    #b
    average_per_prod = np.average(sales_data , axis = 0) #averages collumn wise , per product across 10 days , using axis = 0 
    print("Average sale per product : " ,  average_per_prod , "\n")

    #c
    sales_data_increased = sales_data * 1.05
    print("Increased sale data by 0.05 % : \n" , sales_data_increased , "\n")

    #d
    sales_sqrd = np.sqrt(sales_data)
    print("sales data square rooted : \n " , sales_sqrd , "\n")


    print("Question 2 \n")
    #q2
    #a
    bonus_array = np.array([10 , 20 , 15 , 25 , 30 , 5])
    sales_after_bonus = sales_data + bonus_array
    print("Sales after bonus (via broadcasting) : \n" , sales_after_bonus , "\n")

    #b
    bonus = 50
    sales_after_bonus = sales_data + bonus
    print("Sales after bonus of flat 50 (via broadcasting) : \n" , sales_after_bonus , "\n")

    print("Question 3 \n")
    #q3 
    #a
    mean = np.mean(sales_data)
    print("Mean of entire data set : " , mean , "\n")

    median = np.median(sales_data)
    print("median of entire data set : " , median , "\n")

    variance = np.var(sales_data)
    print("Variance of entire data set : " , variance , "\n")

    standard_dev = np.std(sales_data)
    print("Standard Deviation of entire data set : " , standard_dev , "\n")


    max_val = np.max(sales_data)
    min_val = np.min(sales_data)
    range = max_val - min_val
    print("Maximum : " , max_val  , " \nMinimum : " , min_val , "\nRange : " , range , "\n")
    Q3 = np.percentile(sales_data , 75)
    Q1 = np.percentile(sales_data , 25)
    IQR = Q3 - Q1
    print("Q3 : " , Q3  , " \nQ1 : " , Q1 , "\nIQR : " , IQR , "\n")
    
main()
