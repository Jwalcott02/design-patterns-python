class Handler:
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    def handle(self, ticket):
        pass

class Ticket:
    def __init__(self, id, description, severity):
        self.id = id
        self.description = description
        self.severity = severity

class LowLevelHandler(Handler):
    def handle(self, ticket):
        if ticket.severity < 10:
            print(f"LowLevelHandler handles the request: {ticket.id}")
        elif self.next_handler:
            print("Level 1 is passing ticket to next handler")
            self.next_handler.handle(ticket)
        else:
            print("No handler available for the ticket")

class MidLevelHandler(Handler):
    def handle(self, ticket):
        if 10 <= ticket.severity < 50:
            print(f"MidLevelHandler handles the request: {ticket.id}")
        elif self.next_handler:
            print("Level 2 is passing ticket to next handler")
            self.next_handler.handle(ticket)
        else:
            print("No handler available for the ticket")

class HighLevelHandler(Handler):
    def handle(self, ticket):
        if ticket.severity >= 50:
            print(f"HighLevelHandler handles the request: {ticket.id}")
        elif self.next_handler:
            print("Level 3 is passing ticket to next handler")
            self.next_handler.handle(ticket)
        else:
            print("No handler available for the ticket")

# Chain the handlers
chain = LowLevelHandler(MidLevelHandler(HighLevelHandler()))

# Create tickets
ticket1 = Ticket(1, "Login issue", 5)
ticket2 = Ticket(2, "Server crash", 20)
ticket3 = Ticket(3, "Critical System failure", 30)
ticket4 = Ticket(4, "Unresolvable issue", 70)

tickets = [ticket1, ticket2, ticket3, ticket4]

for req in tickets:
    print(f"\nProcessing ticket: {req.id}, severity: {req.severity}")
    print(f"Description: {req.description}")
    chain.handle(req)
    print("----------------------------------------------------------------------")
