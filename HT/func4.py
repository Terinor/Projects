def discount_price(price, discount):
    def apply_discount():
        nonlocal price
        price = price - discount*price
        

    apply_discount()
    return price
print (discount_price(100, 0.3))

def get_fullname (first_name, last_name, middle_name = "" ):
    full_name = (first_name + " " + middle_name + " " + last_name) if middle_name else (first_name + " " + last_name)
    return full_name
print (get_fullname("kir", "struk", "andr"))

def cost_delivery(*quantities, discount=0):
    first_item_cost = 5
    additional_item_cost = 2
    
    if discount < 0 or discount > 1:
        raise ValueError("Discount should be between 0 and 1")
    
    total_cost = first_item_cost + additional_item_cost * (quantities[0]-1)
    total_cost_with_discount = total_cost * (1 - discount)
    
    return total_cost_with_discount

# Приклад викликів функції
print(cost_delivery(2, 1, 2, 3))  # Виведе 7.0
print(cost_delivery(3, 3))  # Виведе 9.0
print(cost_delivery(1))  # Виведе 5.0
print(cost_delivery(2, 1, 2, 3, discount=0.5)) 

