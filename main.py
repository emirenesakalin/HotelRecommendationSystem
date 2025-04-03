from hotel import Hotel
from hotel_recommendation_system import HotelRecommendationSystem

def main():
    # Create hotel instances
    hotel1 = Hotel("Luxury Antalya Resort", 250, 4.8, "Antalya",["Pool", "Spa", "Wi-Fi", "Restaurant", "AC"])
    hotel2 = Hotel("Historic İzmir Inn", 180, 4.5, "İzmir",["Spa", "Sauna", "Wi-Fi", "Fitness", "Room Service"])
    hotel3 = Hotel("Istanbul City Hotel", 150, 4.2, "İstanbul",["Pool", "Wi-Fi", "Restaurant", "Sea View", "Pet Friendly"])
    hotel4 = Hotel("Ankara Business Hotel", 120, 3.9, "Ankara",["Wi-Fi", "AC", "Fitness", "Room Service"])

    # Initialize the recommendation system
    system = HotelRecommendationSystem()
    system.add_hotel(hotel1)
    system.add_hotel(hotel2)
    system.add_hotel(hotel3)
    system.add_hotel(hotel4)

    # Start the system
    system.main_menu()

if __name__ == "__main__":
    main()