# Hotel Recommendation System

This is a console-based hotel recommendation system written in Python. It allows users to find hotels based on their preferences, such as price, rating, and amenities. The system is pre-populated with a list of hotels in major Turkish cities.

## Project Structure

*   `main.py`: The entry point of the application. It initializes the hotel data and starts the recommendation system.
*   `hotel.py`: Defines the `Hotel` class, which represents a hotel with its attributes (name, price, rating, location, amenities).
*   `hotel_recommendation_system.py`: Contains the core logic of the recommendation system, including sorting, filtering, and the user menu.

## Features

*   **Sort by Price:** Sort hotels by price in either ascending or descending order.
*   **Sort by Rating:** Sort hotels by their rating in either ascending or descending order.
*   **Filter by Amenity:** Find hotels that offer a specific amenity.
*   **Pre-populated Data:** The system comes with a sample list of hotels.
*   **User-Friendly Interface:** A simple command-line menu for easy interaction.

## How to Use

1.  Clone the repository or download the project files (`main.py`, `hotel.py`, `hotel_recommendation_system.py`).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the files.
4.  Run the main script using the following command:

    ```bash
    python main.py
    ```

5.  Use the on-screen menu to find hotels based on your preferences.

### Example

```
--- Hotel Recommendation System ---
1. Sort by Price
2. Sort by Rating
3. Filter by Amenity
4. Exit
Enter your choice (1-4): 1
Sort by: 1. Low to High  2. High to Low: 1

Hotel Name: Ankara Business Hotel
Price: $120
Rating: 3.9/5
Location: Ankara
Amenities: Wi-Fi, AC, Fitness, Room Service

Hotel Name: Istanbul City Hotel
Price: $150
Rating: 4.2/5
Location: İstanbul
Amenities: Pool, Wi-Fi, Restaurant, Sea View, Pet Friendly

Hotel Name: Historic İzmir Inn
Price: $180
Rating: 4.5/5
Location: İzmir
Amenities: Spa, Sauna, Wi-Fi, Fitness, Room Service

Hotel Name: Luxury Antalya Resort
Price: $250
Rating: 4.8/5
Location: Antalya
Amenities: Pool, Spa, Wi-Fi, Restaurant, AC

--- Hotel Recommendation System ---
1. Sort by Price
2. Sort by Rating
3. Filter by Amenity
4. Exit
Enter your choice (1-4): 4
Exiting the system. Goodbye!
```