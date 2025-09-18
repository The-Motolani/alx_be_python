#ask users for weather details
weather = input("What's the weather like today? (sunny/rainy/cold):")
# give appropriate respone for inputted weather
if weather.lower() == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather.lower() == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather.lower() == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I dont have recommendations for this weather.")