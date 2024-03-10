from django.views.generic import TemplateView
import folium
from folium.plugins import Draw


class DrawView(TemplateView):
    template_name = "core/maps.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        m = folium.Map(
            location=[-15.788497, -47.879873], zoom_start=10, control_scale=True
        )
        draw = Draw(export=True)
        draw.add_to(m)

        context["map"] = m._repr_html_()

        return context


class RouterBusView(TemplateView):
    template_name = "core/maps.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        m = folium.Map(location=(-10.439829, -45.16325), zoom_start=14)

        path_route_1 = "fixtures/route_1.geojson"
        path_route_2 = "fixtures/route_2.geojson"
        path_pins = "fixtures/pin_points.geojson"

        folium.GeoJson(
            path_route_1, name="route_1", style_function=lambda x: {"color": "green"}
        ).add_to(m)

        folium.GeoJson(
            path_route_2, name="route_2", style_function=lambda x: {"color": "red"}
        ).add_to(m)

        folium.Marker(
            [-10.430248, -45.173954],
            popup="Start",
            icon=folium.DivIcon(
                icon_size=(150, 36),
                icon_anchor=(0, 0),
                html="""<div style="font-size: 12pt; color: green;">
                <img  width="48" height="48" src="https://img.icons8.com/officel/16/bus.png" alt="bus"/>
                    </div>""",
            ),
        ).add_to(m)

        folium.GeoJson(
            path_pins,
            name="pins",
            marker=folium.Marker(
                icon=folium.DivIcon(
                    icon_size=(150, 36),
                    icon_anchor=(0, 0),
                    html="""<div style="font-size: 12pt; color: green;">
                        <img width="48" height="48" src="https://img.icons8.com/emoji/48/bus-stop-emoji.png" alt="bus-stop-emoji"/>
                        </div>""",
                )
            ),
        ).add_to(m)

        context["map"] = m._repr_html_()

        return context
