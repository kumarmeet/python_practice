class Customer:
    class Billing:
        b_no: int
        b_street: str
        b_city: str
        b_country: str
        b_pin: str

        def __init__(self, no: int, street: str, city: str, country: str, pin: str):
            self.b_no = no
            self.b_street = street
            self.b_city = city
            self.b_country = country
            self.b_pin = pin

    class Shipping:
        s_no: int
        s_street: str
        s_city: str
        s_country: str
        s_pin: str

        def __init__(self, no: int, street: str, city: str, country: str, pin: str):
            self.s_no = no
            self.s_street = street
            self.s_city = city
            self.s_country = country
            self.s_pin = pin

    customer_id: str
    name: str
    billing: Billing
    shipping: Shipping

    def __init__(self, c_id: str, name: str, billing: Billing, shipping: Shipping):
        self.customer_id = c_id
        self.name = name.lower()
        self.billing = billing
        self.shipping = shipping

    def customer_details(self) -> str:
        return (f"{self.name.capitalize()} id is {self.customer_id}"
                f"billing address is {self.billing.b_street} {self.billing.b_city} {self.billing.b_pin} "
                f"shipping address is {self.shipping.s_street} {self.shipping.s_city} {self.shipping.s_pin}")


cus1_billing = Customer.Billing(1, "oreo", "bhopal", "india", "462002")
cus1_shipping = Customer.Shipping(1, "oreo", "bhopal", "india", "462002")

cus1 = Customer("1", "john", cus1_billing, cus1_shipping)

print(cus1.customer_details())
