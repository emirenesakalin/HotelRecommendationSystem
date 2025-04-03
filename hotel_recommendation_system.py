class HotelRecommendationSystem:
    def __init__(self):
        self.hotels = []

    def add_hotel(self, hotel):
        self.hotels.append(hotel)

    def sort_by_price(self, ascending=True):
        return sorted(self.hotels, key=lambda x: x.price, reverse=not ascending)

    def sort_by_rating(self, ascending=True):
        return sorted(self.hotels, key=lambda x: x.rating, reverse=not ascending)

    def sort_by_amenities(self, amenity):
        return [hotel for hotel in self.hotels if amenity in hotel.amenities]

    def display_hotels(self, hotels):
        if not hotels:
            print("No hotels found matching your criteria.")
        else:
            for hotel in hotels:
                print(hotel)

    def main_menu(self):
        while True:
            print("\n--- Hotel Recommendation System ---")
            print("1. Sort by Price")
            print("2. Sort by Rating")
            print("3. Filter by Amenity")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                order = input("Sort by: 1. Low to High  2. High to Low: ")
                sorted_hotels = self.sort_by_price(order == "1")
                self.display_hotels(sorted_hotels)
            elif choice == "2":
                order = input("Sort by: 1. Low to High  2. High to Low: ")
                sorted_hotels = self.sort_by_rating(order == "1")
                self.display_hotels(sorted_hotels)
            elif choice == "3":
                print("Available Amenities: Pool, Spa, Sauna, Wi-Fi, Restaurant, AC, Fitness, Room Service, Sea View, Pet Friendly")
                amenity = input("Enter the amenity to filter by: ")
                filtered_hotels = self.sort_by_amenities(amenity)
                self.display_hotels(filtered_hotels)
            elif choice == "4":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")