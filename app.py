from shiny import App, ui
from htmltools import tags, HTML

kakao_js_key = "3d91fd34529d5628fb6503bc106ebd0d"

# 지도 ID 리스트
map_ids = [f"kakao_map{i}" for i in range(1, 6)]

# --- UI 구성 ---
app_ui = ui.page_fluid(
    ui.h2("🗺️ 탭마다 카카오 지도 넣기"),
    ui.navset_tab(
        *[
            ui.nav_panel(
                f"Tab{i} - 지도",
                tags.div(
                    id=map_ids[i - 1],
                    style="width:100%; height:400px; background-color:#eee;",
                ),
            )
            for i in range(1, 6)
        ]
    ),
    # --- Kakao SDK 로드 ---
    tags.script(
        HTML(
            f"""
        const script = document.createElement("script");
        script.src = "https://dapi.kakao.com/v2/maps/sdk.js?appkey={kakao_js_key}&autoload=false";
        script.onload = function () {{
            window.kakao_loaded = true;
        }};
        document.head.appendChild(script);
        """
        )
    ),
    # --- 모든 탭 클릭 시 개별 지도 로드 ---
    tags.script(
        HTML(
            f"""
        document.addEventListener("DOMContentLoaded", function () {{
            let loadedMaps = {{}};

            function initKakaoMap(mapId, lat, lng) {{
                if (!window.kakao_loaded || loadedMaps[mapId]) return;

                const container = document.getElementById(mapId);
                if (!container) return;

                kakao.maps.load(function () {{
                    const map = new kakao.maps.Map(container, {{
                        center: new kakao.maps.LatLng(lat, lng),
                        level: 3
                    }});
                    map.addOverlayMapTypeId(kakao.maps.MapTypeId.TRAFFIC);
                    loadedMaps[mapId] = true;
                }});
            }}

            // 탭 버튼 감지해서 해당 div가 보이면 지도 초기화
            const tabButtons = document.querySelectorAll('button[data-bs-toggle="tab"]');
            tabButtons.forEach(btn => {{
                btn.addEventListener("click", () => {{
                    setTimeout(() => {{
                        {''.join([f'initKakaoMap("{id}", 37.56{i}, 126.97{i});' for i, id in enumerate(map_ids, start=1)])}
                    }}, 300);
                }});
            }});

            // 첫 번째 탭은 자동 초기화
            setTimeout(() => {{
                initKakaoMap("{map_ids[0]}", 37.561, 126.971);
            }}, 500);
        }});
        """
        )
    ),
)


# --- 서버 구성 ---
def server(input, output, session):
    pass


app = App(app_ui, server)
