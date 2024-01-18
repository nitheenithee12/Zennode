def calculation(a,b,c, wrap):
    max_dis = 0
    cart_value = (20*a) + (40*b) + (50*c) #cart_value calculation
    total_p = a+b+c
    dis_name = ""
    #discount calculation
    if cart_value > 200:                    # discount for cart value greater than 200
        if 10 > max_dis:
            max_dis = 10
            dis_name = "flat_10_discount"
        
    if a > 10 or b > 10 or c > 10:          #discount for any product quanity greater than 10
        value = 0
        if a>10:
            value = (20*a)*0.05
        elif b > 10:
            value =  (40*b)*0.05
        elif c > 10:
            value =  (50*c)*0.05
            
        if value > max_dis:
            max_dis = value
            dis_name = "bulk_5_discount"
            
    if total_p > 20:                        #discount for total no. of products greater than 20
        if cart_value*0.1 > max_dis:
            max_dis = value
            dis_name = "bulk_10_discount"
        
        
    if total_p > 30 and (a>15 or b > 15 or c > 15):     #discount if, total quanity is greater than 20 and any single product > 15
        value = 0
    
        if a>15:
            value = (20*(a-15))*0.5
        elif b > 15:
            value = (40*(b-15))*0.5
        elif c > 15:
            value = (50*(c-15))*0.5
            
        if value > max_dis:
            dis_name = "tiered_50_discount"
            
            
    #gift wrap
    wrap_cost = 0
    if wrap == 1:
        wrap_cost += total_p
    #shipping fee
    half_filled = 1 if total_p % 10 != 0 else 0
    ful_filled = total_p//10
    shipping_fee = (half_filled+ful_filled)*5
    
    
    #-----------output----------
    print("Product A, quanity: ", a, "Amount: ", a*20)
    print("Product B, quanity: ", b, "Amount: ", b*40)
    print("Product C, quanity: ", c, "Amount: ", c*50)
    print("Subtotal, without discount: ", cart_value)
    print("Discount name: '", dis_name, "' Discount Amount: ", max_dis)
    print("Shipping Fee: ", shipping_fee, "Gift Wrap Fee: ", wrap_cost)
    print("Grand Total: ", cart_value - max_dis + shipping_fee+wrap_cost)
    

if __name__ == "__main__":                              #This is where program intantiates...
    a = int(input("Enter number of products(Type A): "))
    b = int(input("Enter number of products(Type B): "))
    c = int(input("Enter number of products(Type C): "))
    wrap = int(input("Enter 1 if Gift wrapper needed else enter 0: "))
    print()
    print()
    calculation(a,b,c, True)                            #a,b,c were the quantities of products A,B,C respectively.
