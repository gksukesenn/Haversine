# max_hiz = float(input("Droneun maksimum hızını girin (m/s): "))
# uzaklik = float(input("Ulaşılacak mesafeyi girin (metre): "))
# yuk = float(input("Taşınacak yükün ağırlığını girin (kilogram): "))

# Ortalama hız hesaplama
# toplam_yuk = yuk
# ucus_suresi = uzaklik / (max_hiz - (yuk * 0.1))


# print(f"Drone, {uzaklik} metrelik yolu {toplam_yuk} ile {ucus_suresi} saniyede tamamlayabilir.")

from geopy.geocoders import Nominatim
from math import radians, sin, cos, sqrt, atan2


def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Yeryüzü yarıçapı (km)

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2) * sin(dlat / 2) + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) * sin(dlon / 2)
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance


def get_coordinates(address):
    geolocator = Nominatim(user_agent="myapp")
    location = geolocator.geocode(address)
    return location.latitude, location.longitude


# Adresleri tanımla
adres1 = "Düzce Devlet Hastanesi,Türkiye"
adres2 = "Bursa Devlet Hastanesi,Türkiye"


enlem1, boylam1 = get_coordinates(adres1)
enlem2, boylam2 = get_coordinates(adres2)


mesafe = haversine_distance(enlem1, boylam1, enlem2, boylam2)
print(f"{adres1} ile {adres2} arasındaki kuş uçuşu mesafesi: {mesafe} kilometre")