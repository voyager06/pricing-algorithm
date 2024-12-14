# Pricing Algorithm Django Project

## **Overview**
This project implements a dynamic pricing algorithm for restaurant menus using Python and Django. The goal is to adjust menu item prices based on competitive pricing, weather conditions, and customer demand during busy times. The system uses static and real-time data to compute adjusted prices.

---

## **Features**

1. **Static Menu Parsing**:
   - Parses the menu from a provided text file (e.g., `village_menu.txt`).
   - Extracts item names, descriptions, and prices into a structured format.

2. **Competitor Menu Integration**:
   - Includes mock competitor data for testing purposes.
   - Compares prices of similar items across competitors.

3. **Dynamic Pricing Adjustments**:
   - Adjusts prices based on:
     - Competitive pricing (lowest or near-lowest competitor price).
     - Weather conditions (e.g., higher prices during rain or cold).
     - Busy times (e.g., increased demand).

4. **Frontend Integration**:
   - Displays adjusted menu prices dynamically on the web interface.

5. **Modular Design**:
   - Organized structure with separate files for parsing, utilities, and views.

---

## **Technologies Used**
- **Framework**: Django 4.2.17
- **Language**: Python 3.9
- **APIs**: OpenWeatherMap (optional for real-time weather data)
- **Database**: SQLite (default Django database for development)
- **HTML Templates**: Django templates for rendering the UI

---

## **Project Structure**
```
pricing_algorithm/
    manage.py                # Django entry point
    pricing_algorithm/       # Project configuration
        __init__.py
        settings.py
        urls.py
        wsgi.py
    pricing/                 # Main app
        __init__.py
        views.py             # Business logic
        utils.py             # Helper functions for adjustments
        parsers.py           # Menu parsing logic
        templates/
            pricing/
                pricing.html  # Frontend template
        static/
            village_menu.txt # Static menu file
        migrations/          # Database migrations
```

---

## **Setup Instructions**

### 1. **Clone the Repository**
```bash
git clone <repository_url>
cd pricing_algorithm
```

### 2. **Set Up a Virtual Environment**
```bash
python -m venv env
source env/bin/activate    # On Linux/Mac
env\Scripts\activate      # On Windows
```

### 3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4. **Configure the Database**
Run the following commands to apply migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. **Run the Server**
Start the Django development server:
```bash
python manage.py runserver
```
Access the application at `http://127.0.0.1:8000/`.

---

## **How to Use**

1. **Upload Village Menu**:
   - Ensure the `village_menu.txt` file is in the `static/` directory.

2. **Mock Competitor Data**:
   - Modify `competitors` data in `views.py` for custom competitor menus.

3. **Adjust Prices**:
   - Prices are adjusted automatically based on weather, competitor prices, and demand.

4. **View Adjusted Menu**:
   - Visit the root URL (`http://127.0.0.1:8000/`) to view the adjusted menu prices.

---

## **Customization**

### 1. **Weather Integration**
To fetch live weather data:
- Register for an API key at [OpenWeatherMap](https://openweathermap.org/).
- Add the key to your `settings.py`:
  ```python
  WEATHER_API_KEY = "your_api_key_here"
  ```

### 2. **Competitor Data**
- Replace the mock `competitors` data in `views.py` with real data fetched from APIs like Yelp or manually provided.

### 3. **Styling**
- Update the `pricing.html` template for custom styling and layout.

---

## **Example Adjusted Pricing Logic**
### If Conditions:
- **Temperature**: Below 45°F
- **Rain/Snow**: Moderate or heavier rain/snow
- **Busy Times**: Higher customer demand

### Then:
- Prices are increased by a percentage above the lowest competitive price.

### Else:
- Prices match the lowest competitive price.

---

## **Future Improvements**
- Integration with live competitor APIs (e.g., Yelp, Google Maps).
- Automated busy time tracking using real-time Google data.
- Advanced machine learning algorithms for dynamic price prediction.

---

## **Contributors**
- Vedant Swami - Developer
- OpenAI - Assistance

---

## **License**
This project is licensed under the MIT License. See the `LICENSE` file for details.

