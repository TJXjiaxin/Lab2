
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average_temperature(num_list)
    calc_min_max_temperature(num_list)
    calc_median_temperature(num_list)
    
    

def display_main_menu():
    print("Enter temperatures")


def get_user_input():
    user_input = input("Enter numbers: ")
    number = user_input.split(",")
    num =[]
    for i in number:
        num.append(float(i))
    return num

def calc_average_temperature(num_list) :
    a = sum(num_list) / len(num_list)
    print(a)

def calc_min_max_temperature(num_list):
   mini=min(num_list)
   maxi=max(num_list)
   print ("min ="+str(mini))
   print ("max ="+str(maxi))


def calc_median_temperature (num_list):
    orderlist=sorted(num_list)
    i=len(orderlist)
    if i%2 ==0:
        median=(orderlist[i//2]+ orderlist[i//2-1])/2
    else:
        median=orderlist[i//2]
    print("median =" + str(median))
   
if __name__ == "__main__":
 main()


