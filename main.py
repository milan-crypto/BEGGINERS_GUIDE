class location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Location: (Latitude={self.latitude}, Longitude={self.longitude}"

    def __str__(self):
        return f"(Latitude={self.latitude}, Longitude={self.longitude}"

bham_academy = location(52.488647, -1.887249)
print(f"The coordinates for the Birmingham Academy are: {bham_academy}")
