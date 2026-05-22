from .records import reservations

def add_reservation(name, date):
    reservations.append({"name": name, "date": date})
    return "Reservation added successfully"

def view_reservations():
    return reservations