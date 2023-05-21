
import math

#products and price
products = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

#declaring the variables
offers=[]
cart = []
total_amount = 0
total_quantity = 0

#asking the user to add products to the cart
for product, price in products.items():
    # print(product,price)
    quantity = int(input(f"\nEnter the quantity of {product}: "))
   
    is_gift_wrapped = input(f"\nIs {product} wrapped as a gift? (yes/no): ")
    
    gift = 0
    

    product_total = quantity*price

    total_quantity += quantity
#
    if is_gift_wrapped == "yes":
        gift = int(input(f"\nEnter the no.of {product} wrapped as a gift: "))
        while gift > quantity:
            print("\nPlease enter valid no.of gifts...")
            gift = int(input(f"\nRe Enter the no.of {product} wrapped as a gift: "))
        # product_total += gift
    cart.append({'name':product,'quantity':quantity,"gift":gift,"total":product_total})

    total_amount += product_total


#setting discount rules and find the discounts applicable the user
if total_amount>200:
    offers.append({"offer_name":"flat_10_discount"})

product_with_max_quantity = max(cart, key=lambda p: p['quantity'])

if product_with_max_quantity['quantity']>10:
    offers.append({"offer_name":"bulk_5_discount"})

if total_quantity >20:
    offers.append({"offer_name":"bulk_10_discount"})

if total_quantity > 30 and product_with_max_quantity['quantity'] > 15:
    offers.append({"offer_name":"tiered_50_discount"})

#apply offers 
apply_offer = []


for offer in offers:
    if offer['offer_name'] == "flat_10_discount":
        # print("discount : "+str(10))
        apply_offer.append({"offer_name":"flat_10_discount","discount":10})
    
    if offer['offer_name'] == "bulk_5_discount":
        # print(product_with_max_quantity['total']*0.05)
        apply_offer.append({"offer_name":"bulk_5_discount","discount":product_with_max_quantity['total']*0.05})


    if offer['offer_name'] == "bulk_10_discount":
        # print(total_amount*0.1)
        apply_offer.append({"offer_name":"bulk_10_discount","discount":total_amount*0.1})


    if offer['offer_name'] == "tiered_50_discount":
        discount_price=0
        if total_quantity > 30:
            for i in cart:
                if i['quantity'] > 15:
                    discount_price += i['total'] * 0.5
        apply_offer.append({"offer_name":"tiered_50_discount","discount":discount_price})

#find the best offer to the customer         
best_offer = max(apply_offer, key=lambda p: p['discount'])
#find the number of packages here we use the math.ceil for get ceiling value .
packs = math.ceil(total_quantity / 10)
total_gift = 0;

print("=========================================")
print("                BILL                ")

print("=========================================")
print('product   Quantity      total')
print("--------------------------------")
for i in cart:
    total_gift += i['gift']
    print(i['name']+"   "+str(i['quantity'])+"          $ "+str(i['total']))
print("--------------------------------")
print("Sub total : $ "+str(total_amount))
print("--------------------------------")
print("Offer Aplied : "+best_offer['offer_name'])
print("    Discount : $ "+str(best_offer['discount']))
print("--------------------------------")
print("Shipping fee  : "+str(packs)+" X 5 = $ "+str(packs*5) )
print("Gift wrap fee : "+str(total_gift)+" X 1 = $ "+str(total_gift*1))

print("--------------------------------")
print("Total        :          $ "+str(total_amount-best_offer['discount']+packs*5+total_gift))
print("=========================================")














# Enter the quantity of Product A: 5

# Is Product A wrapped as a gift? (yes/no): n

# Enter the quantity of Product B: 15

# Is Product B wrapped as a gift? (yes/no): yes

# Enter the no.of Product B wrapped as a gift: 5

# Enter the quantity of Product C: 13

# Is Product C wrapped as a gift? (yes/no): n
# =========================================
# product   Quantity      total
# --------------------------------
# Product A   5          $ 100
# Product B   15         $ 600
# Product C   13         $ 650
# --------------------------------
# Sub total : $ 1350
# --------------------------------
# Offer Aplied : bulk_10_discount
#     Discount : $ 135.0
# --------------------------------
# Shipping fee  : 4 X 5 = $ 20
# Gift wrap fee : 5 X 1 = $ 5
# --------------------------------
# Total        :          $ 1240.0
# =========================================