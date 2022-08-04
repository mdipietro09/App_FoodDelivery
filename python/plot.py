
import folium


class Plot():

    def __init__(self, start, end):
        self.start = start
        self.end = end


    def create_map(self, route):
        print("--- creating map ---")
        map_ = ox.plot_route_folium(self.graph, route, zoom=12)

        start_marker = folium.Marker(location=self.start, popup="start", icon=folium.Icon(color='green'))
        end_marker = folium.Marker(location=self.end, popup="end", icon=folium.Icon(color='red'))
        start_marker.add_to(map_)
        end_marker.add_to(map_)

        folium.LatLngPopup().add_to(map_)
        folium.ClickForMarker(popup="Delivery").add_to(map_)

        map_.save("static/output.html")
        print("--- saved ---")