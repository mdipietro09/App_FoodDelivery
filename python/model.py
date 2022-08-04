
import geopy
import osmnx as ox
import networkx as nx
import folium


class Model():

    @staticmethod
    def get_geo(query):
        locator = geopy.geocoders.Nominatim(user_agent="myGeocoder")
        location = locator.geocode(query)
        return location.latitude, location.longitude


    def __init__(self, query, end):
        self.start = self.get_geo(query)
        self.end = end


    def calculate_route(self):
        print("--- calculating ---")
        self.graph = ox.graph_from_point(self.start, dist=1000, network_type='drive')
        #graph = ox.graph_from_place(query=self.start, network_type='drive')
        start_node = ox.get_nearest_node(self.graph, self.start)
        end_node = ox.get_nearest_node(self.graph, self.end)
        route = nx.shortest_path(self.graph, start_node, end_node, weight="time")
        return route


    def create_map(self, route):
        print("--- creating map ---")
        map_ = ox.plot_route_folium(self.graph, route, zoom=12)

        start_marker = folium.Marker(location=self.start, popup="start", icon=folium.Icon(color='green'))
        end_marker = folium.Marker(location=self.end, popup="end", icon=folium.Icon(color='red'))
        start_marker.add_to(map_)
        end_marker.add_to(map_)

        #folium.LatLngPopup().add_to(map_)
        folium.ClickForMarker(popup="Delivery").add_to(map_)

        map_.save("static/output.html")
        print("--- saved ---")


    #def move(route):
    #    return route