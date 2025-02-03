# Weather App

A modern, responsive weather application built with Django that provides real-time weather information and forecasts for cities worldwide.

## Features

- **Dynamic City Search**: Type-ahead search functionality for cities worldwide
- **Current Weather Display**: 
  - Temperature (with Celsius/Fahrenheit toggle)
  - Feels like temperature
  - Weather description with icons
  - Humidity levels
  - Wind speed
  - Pressure
  - Sunrise and sunset times
- **5-Day Weather Forecast**
- **Responsive Design**: Works on desktop and mobile devices
- **Beautiful UI**: Modern interface with smooth transitions and animations

## Technologies Used

- **Backend**:
  - Django
  - Python
  - OpenWeatherMap API
- **Frontend**:
  - HTML5
  - CSS3
  - JavaScript
  - jQuery
  - Bootstrap 5
  - Select2.js
  - Font Awesome icons

## Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- OpenWeatherMap API key

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd weather_app
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenWeatherMap API key:
   ```
   WEATHER_API_KEY=your_api_key_here
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000` in your web browser

## Usage

1. Start typing a city name in the search box
2. Select a city from the dropdown suggestions
3. View current weather information and 5-day forecast
4. Toggle between Celsius and Fahrenheit using the temperature toggle

## Features in Detail

### City Search
- Powered by OpenWeatherMap's Geocoding API
- Provides city suggestions as you type
- Includes state/region and country information
- Caches results for better performance

### Weather Information
- **Current Weather**:
  - Real-time temperature data
  - Weather condition icons
  - Detailed atmospheric conditions
  - Day/night information with sunrise/sunset times

- **Forecast**:
  - 5-day weather forecast
  - Daily temperature predictions
  - Weather condition descriptions
  - Humidity and wind information

### User Interface
- Clean and intuitive design
- Responsive layout for all screen sizes
- Smooth animations and transitions
- Interactive elements for better user experience

## Configuration

The application uses environment variables for configuration. Create a `.env` file with the following variables:

```
WEATHER_API_KEY=your_openweathermap_api_key
DEBUG=True  # Set to False in production
SECRET_KEY=your_django_secret_key
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org/)
- Icons by [Font Awesome](https://fontawesome.com/)
- UI components by [Bootstrap](https://getbootstrap.com/)
- Search functionality by [Select2](https://select2.org/)
