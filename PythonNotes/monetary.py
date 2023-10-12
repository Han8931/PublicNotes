def to_dollars(amount:int)->str:
    return f"${amount/100:.2f}"

def main()->None:
    int_balance = 10_000
    int_withdrawl = 4237
    int_deposit = 10

    int_result = int_balance-int_withdrawl+int_deposit
    print(f"Using integers: {to_dollars(int_result)}") 

if __name__ =="__main__":
    main()
