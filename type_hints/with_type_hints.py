from typing import List, Dict, Optional

def process_order(order: List[Dict[str, float]], tax_rate: float, discount: Optional[float] = None) -> float:
    total: float = 0
    for item in order:
        price: float = item['price']
        quantity: float = item['quantity']
        total += price * quantity
    if discount:
        total -= discount
    total += total * tax_rate
    return total

def send_email(to_address: str, subject: str, body: str) -> None:
    print("Sending email to", to_address)
    print("Subject:", subject)
    print("Body:", body)

order: List[Dict[str, float]] = [{'price': 20, 'quantity': 2}, {'price': 15, 'quantity': 1}]
final_price: float = process_order(order, 0.15, discount=5)
send_email("customer@example.com", "Your Order Total", f"Total: {final_price}")

process_order("this is not an order", 0.1)
