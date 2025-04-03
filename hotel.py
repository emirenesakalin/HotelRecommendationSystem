class Hotel:
    def __init__(self, name, price, rating, location, amenities):
        self.name = name
        self.price = price
        self.rating = rating
        self.location = location
        self.amenities = amenities  # List of amenities (e.g., ["pool", "spa", "wifi"])

    def __repr__(self):
        return (f"Hotel Name: {self.name}\n"
                f"Price: ${self.price}\n"
                f"Rating: {self.rating}/5\n"
                f"Location: {self.location}\n"
                f"Amenities: {', '.join(self.amenities)}\n")