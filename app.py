from shiny import App, ui
from htmltools import tags, HTML

# --- 카카오 JavaScript API Key ---
javascript_api_key = "3d91fd34529d5628fb6503bc106ebd0d"

# --- UI 구성 ---
app_ui = ui.page_fluid(
    ui.h2("영천시 카카오 지도"),
    tags.div(id="map_js", style="width:100%; height:400px;"),
    tags.script(
        src=f"https://dapi.kakao.com/v2/maps/sdk.js?appkey={javascript_api_key}&autoload=false"
    ),
    tags.script(
        HTML(
            """
            document.addEventListener("DOMContentLoaded", function () {
                kakao.maps.load(function () {
                    var container = document.getElementById('map_js');
                    if (!container) {
                        console.error('map_js element not found!');
                        return;
                    }

                    var options = {
                        center: new kakao.maps.LatLng(35.968251, 128.941506),
                        level: 4
                    };

                    var map = new kakao.maps.Map(container, options);

                    // 예시 마커
                    var marker = new kakao.maps.Marker({
                        position: new kakao.maps.LatLng(35.968251, 128.941506),
                        map: map,
                        title: '영천시청'
                    });

                    marker.setMap(map);
                });
            });
            """
        )
    ),
)


# --- 서버 구성 (불필요하지만 구성 필요) ---
def server(input, output, session):
    pass


# --- 앱 실행 ---
app = App(app_ui, server)
