# Is there a bug here?

def process_order(order, tax_rate, discount=None):
    total = 0
    for item in order:
        price = item['price']
        quantity = item['quantity']
        total += price * quantity
    if discount:
        total -= discount
    total += total * tax_rate
    return total

def send_email(to_address, subject, body):
    print("Sending email to", to_address)
    print("Subject:", subject)
    print("Body:", body)

order = [{'price': 20, 'quantity': 2}, {'price': 15, 'quantity': 1}]
final_price = process_order(order, 0.15, discount=5)
send_email("customer@example.com", "Your Order Total", f"Total: {final_price}")


process_order("this is an order", 0.1)
