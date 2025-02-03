import requests
from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
from django.db.models import Q
from cities_light.models import City
import json
from datetime import datetime

def get_cities():
    """Get list of major cities ordered by population"""
    try:
        cities = City.objects.filter(population__gt=100000).order_by('-population').select_related('region', 'country')[:200]
        return [format_city(city) for city in cities]
    except:
        # Fallback cities if database is not yet populated
        return [
            {'name': 'London, United Kingdom', 'lat': '51.5074', 'lon': '-0.1278'},
            {'name': 'New York, United States', 'lat': '40.7128', 'lon': '-74.0060'},
            {'name': 'Tokyo, Japan', 'lat': '35.6762', 'lon': '139.6503'},
            {'name': 'Paris, France', 'lat': '48.8566', 'lon': '2.3522'},
            {'name': 'Sydney, Australia', 'lat': '-33.8688', 'lon': '151.2093'},
            {'name': 'Dubai, United Arab Emirates', 'lat': '25.2048', 'lon': '55.2708'},
            {'name': 'Singapore, Singapore', 'lat': '1.3521', 'lon': '103.8198'},
            {'name': 'Rome, Italy', 'lat': '41.9028', 'lon': '12.4964'},
            {'name': 'Beijing, China', 'lat': '39.9042', 'lon': '116.4074'},
            {'name': 'Moscow, Russia', 'lat': '55.7558', 'lon': '37.6173'},
        ]

def format_city(city):
    """Format city name with region and country"""
    if city.region:
        return {
            'name': f"{city.name}, {city.region.name}, {city.country.name}",
            'lat': str(city.latitude),
            'lon': str(city.longitude)
        }
    return {
        'name': f"{city.name}, {city.country.name}",
        'lat': str(city.latitude),
        'lon': str(city.longitude)
    }

def get_weather(request):
    # Get list of cities for the dropdown
    cities = get_cities()
    context = {
        'cities': cities,
        'weather_api_key': settings.WEATHER_API_KEY
    }

    if request.method == 'POST':
        try:
            city_input = request.POST.get('city', '')
            lat = request.POST.get('lat')
            lon = request.POST.get('lon')
            
            if lat and lon:
                # Use coordinates for more accurate results
                current_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={settings.WEATHER_API_KEY}&units=metric"
                forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={settings.WEATHER_API_KEY}&units=metric"
            else:
                # Fallback to city name
                city = city_input.split(',')[0]  # Get only the city name
                current_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.WEATHER_API_KEY}&units=metric"
                forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={settings.WEATHER_API_KEY}&units=metric"
            
            # Get current weather
            current_response = requests.get(current_url)
            current_data = current_response.json()
            
            if current_response.status_code == 200:
                # Get forecast data
                forecast_response = requests.get(forecast_url)
                forecast_data = forecast_response.json()
                
                # Process forecast data
                forecast_list = []
                for item in forecast_data['list'][::8]:  # Get one entry per day
                    date = datetime.fromtimestamp(item['dt'])
                    forecast_list.append({
                        'date': date.strftime('%A'),  # Day name
                        'temp': round(item['main']['temp']),
                        'description': item['weather'][0]['description'].capitalize(),
                        'icon': item['weather'][0]['icon'],
                        'humidity': item['main']['humidity'],
                        'wind_speed': item['wind']['speed']
                    })
                
                # Use the provided city name if available
                display_city = city_input if city_input else f"{current_data['name']}, {current_data['sys']['country']}"
                
                # Current weather data
                weather_data = {
                    'city': display_city,
                    'temperature': round(current_data['main']['temp']),
                    'feels_like': round(current_data['main']['feels_like']),
                    'description': current_data['weather'][0]['description'].capitalize(),
                    'humidity': current_data['main']['humidity'],
                    'wind_speed': current_data['wind']['speed'],
                    'icon': current_data['weather'][0]['icon'],
                    'pressure': current_data['main']['pressure'],
                    'sunrise': datetime.fromtimestamp(current_data['sys']['sunrise']).strftime('%H:%M'),
                    'sunset': datetime.fromtimestamp(current_data['sys']['sunset']).strftime('%H:%M'),
                    'forecast': forecast_list
                }
                
                context['weather'] = weather_data
                
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'weather': weather_data})
            else:
                error_message = current_data.get('message', 'City not found. Please try again.')
                context['error'] = error_message
                if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({'error': error_message})
                
        except requests.RequestException as e:
            error_message = f"Could not fetch weather data. Please try again later. Error: {str(e)}"
            context['error'] = error_message
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({'error': error_message})
    
    return render(request, 'weather/index.html', context)