'''
@Author: Shreyash More

@Date: 2023-06-04 18:34:30

@Last Modified by: Shreyash More

@Last Modified time: 2023-06-05 12:34:30

@Title : 2D Array

'''
def twodimensionalarr(m,n):
    """
    Description:
        It creates a two dimensional array of m x n size
    Parameter:
        Takes an m & n as input for m rows and n colummn
    Return:
       Returns a 2D array
    """
    arr=[]
    # Creating a array of size m 
    for i in range(m):
            a=[]
            print(f"Enter Value for {i} row ")
            # Creating a subarray of  n size
            for j in range (n):  
                num=int(input("Enter Value for "))
                a.append(num)
            arr.append(a)
    return arr

def main():
    # Taking rows and colummn as input
    m_rows=int(input("Enter number of rows"))
    n_cols=int(input("Enter number of coloumns"))
    ary=twodimensionalarr(m_rows,n_cols)
    # printing the array
    for i in ary:
        print(i)

if __name__ == "__main__":
    main()