import folium

# Data for the 12 Jyotirlingas
jyotirlingas = [
    {"name": "Somnath", "location": [20.8902, 70.4028], "info": "Located in Gujarat, Somnath is the first Jyotirlinga and symbolizes the start of creation. Have a Happy, safe, and blessed journey", "link": "https://en.wikipedia.org/wiki/Somnath_temple"},
    {"name": "Mallikarjuna", "location": [16.0728, 78.8723], "info": "Located in Andhra Pradesh, it is situated on the Shri Shaila Mountain. Have a Happy, safe, and blessed journey", "link": "https://en.wikipedia.org/wiki/Mallikarjuna_Jyotirlinga"},
    {"name": "Mahakaleshwar", "location": [23.1828, 75.7680], "info": "Located in Ujjain, Madhya Pradesh, it is a temple where Lord Shiva is worshiped as Mahakal. Have a Happy, safe, and blessed journey", "link": "https://en.wikipedia.org/wiki/Mahakaleshwar_Jyotirlinga"},
    {"name": "Omkareshwar", "location": [22.0312, 76.0554], "info": "Located in Madhya Pradesh, Omkareshwar is situated on an island in the Narmada River. Have a Happy, safe, and blessed journey", "link": "https://en.wikipedia.org/wiki/Omkareshwar"},
    {"name": "Kedarnath", "location": [30.7352, 79.0669], "info": "Located in Uttarakhand, it is nestled in the Himalayan ranges. Have a Happy, safe, and blessed journey", "link": "https://en.wikipedia.org/wiki/Kedarnath_Temple"},
    {"name": "Bhimashankar", "location": [19.0544, 73.5530], "info": "Located in Maharashtra, Bhimashankar is surrounded by lush greenery. Have a Happy, safe, and blessed journey", "link": "https://en.wikipedia.org/wiki/Bhimashankar_Temple"},
    {"name": "Kashi Vishwanath", "location": [25.3109, 83.0097], "info": "Located in Varanasi, Uttar Pradesh, it is one of the most famous temples in India. Have a Happy, safe, and blessed journey", "link": "https://en.wikipedia.org/wiki/Kashi_Vishwanath_Temple"},
    {"name": "Trimbakeshwar", "location": [19.9270, 73.5530], "info": "Located in Maharashtra, it is near the origin of the Godavari River. Have a Happy, safe, and blessed journey", "link": "https://en.wikipedia.org/wiki/Trimbakeshwar_Shiva_Temple"},
    {"name": "Vaidyanath", "location": [24.0312, 86.7070], "info": "Located in Jharkhand, it is also known as Baba Dham. Have a Happy, safe, and blessed journey", "link": "https://en.wikipedia.org/wiki/Baidyanath_Temple"},
    {"name": "Nageshwar", "location": [22.4551, 69.1345], "info": "Located near Dwarka in Gujarat, it is famous for its serene atmosphere. Have a Happy, safe, and blessed journey", "link": "https://en.wikipedia.org/wiki/Nageshvara_Jyotirlinga"},
    {"name": "Rameshwar", "location": [9.2881, 79.3174], "info": "Located in Tamil Nadu, it is situated on Rameswaram Island. Have a Happy, safe, and blessed journey", "link": "https://en.wikipedia.org/wiki/Ramanathaswamy_Temple"},
    {"name": "Grishneshwar", "location": [20.0070, 75.1775], "info": "Located in Maharashtra, it is near the Ellora caves. Have a Happy, safe, and blessed journey", "link": "https://en.wikipedia.org/wiki/Grishneshwar_Temple"}
]

# Create a map centered around India
map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)

# Add markers for each Jyotirlinga
for jyotirlinga in jyotirlingas:
    folium.Marker(
        location=jyotirlinga["location"],
        popup=folium.Popup(f"<b>{jyotirlinga['name']}</b><br>{jyotirlinga['info']}<br><a href='{jyotirlinga['link']}' target='_blank'>More info</a>", max_width=300),
        tooltip=jyotirlinga["name"],  # Tooltip that will display the name on hover
        icon=folium.Icon(color='blue', icon='info-sign', prefix='glyphicon')  # Custom icon to make markers more visible
    ).add_to(map)

 # Display the name of the Jyotirlinga directly on the map
    folium.Marker(
        location=jyotirlinga["location"],
        popup=folium.Popup(f"<b>{jyotirlinga['name']}</b>", max_width=150),
        icon=folium.DivIcon(html=f'<div style="font-size: 12pt; color: black; font-weight: bold;">{jyotirlinga["name"]}</div>')
    ).add_to(map)

# Save the map to an HTML file
map.save("map.html")

# Custom HTML template
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>12 Jyotirlingas Map</title>
    <style>
        body {{
            margin: 0;
            font-family: Arial, sans-serif;
            text-align: center;
        }}
        .background {{
            background: url('https://www.tourmyindia.com/blog//wp-content/uploads/2021/05/12-Jyotirlingas-Temples-in-India.jpg') no-repeat center center fixed;
            background-size: cover;
            color: white;
            padding: 100px 20px;
        }}
        .background h1 {{
            font-size: 3em;
            margin: 0;
        }}
        .background p {{
            font-size: 1.5em;
            margin: 10px 0 50px 0;
        }}
        .map-container {{
            width: 100%;
            height: 80vh;
        }}
    </style>
</head>
<body>
    <div class="background">
        <h1>Divine Journey: The 12 Jyotirlingas</h1>
        <p>"The Jyotirlingas are the radiant light of the Eternal, guiding us on the path of devotion."</p>
    </div>
    <div class="map-container">
        <iframe src="map.html" style="width: 100%; height: 100%; border: none;"></iframe>
    </div>
</body>
</html>
"""

# Save the HTML template
with open("jyotirlingas_map_with_background.html", "w") as file:
    file.write(html_template)

print("Web page created with Lord Shiva's image and map. Open 'jyotirlingas_map_with_background.html' to view.")
