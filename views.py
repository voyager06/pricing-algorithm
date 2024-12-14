from django.shortcuts import render
from pricing.utils import get_competitors, get_weather, adjust_prices
from .parsers import parse_menu

def pricing_view(request):
    # Example data to pass to the template
    village_menu = parse_menu('static/village_menu.txt')
    weather = get_weather(lat=40.7687, lng=-73.5256)
    competitors =   {
            "name": "Competitor A",
            "menu": {
                "Rasam": 4.50,
                "Sambar": 4.75,
                "Mulligatawny Soup": 4.80,
                "Garden Soup": 4.60,
                "Kachumbar Salad": 4.40,
                "Idly": 5.50,
                "Masala Idly": 7.50,
                "Veg Hakka Noodles": 9.50,
                "Paneer Tikka Masala": 12.50,
                "Palak Paneer": 12.00,
            },
        },
    {
            "name": "Competitor B",
            "menu": {
                "Rasam": 4.95,
                "Sambar": 5.00,
                "Mulligatawny Soup": 4.70,
                "Garden Soup": 4.85,
                "Kachumbar Salad": 4.50,
                "Idly": 5.95,
                "Masala Idly": 7.95,
                "Veg Hakka Noodles": 10.00,
                "Paneer Tikka Masala": 12.95,
                "Palak Paneer": 12.50,
            },
        },
    {
            "name": "Competitor C",
            "menu": {
                "Rasam": 4.60,
                "Sambar": 4.80,
                "Mulligatawny Soup": 4.90,
                "Garden Soup": 4.50,
                "Kachumbar Salad": 4.20,
                "Idly": 5.75,
                "Masala Idly": 7.75,
                "Veg Hakka Noodles": 9.75,
                "Paneer Tikka Masala": 13.00,
                "Palak Paneer": 13.50,
            },
        },
    
    is_busy = True  # Dummy busy condition

    # Adjust prices (logic in utils.py)
    adjusted_prices = adjust_prices(village_menu, weather, is_busy, competitors)

    # Render pricing.html and pass data to it
    return render(request, 'pricing/pricing.html', {'prices': adjusted_prices})
    

