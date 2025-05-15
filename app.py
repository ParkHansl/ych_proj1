from shiny import App, ui
from htmltools import tags, HTML

# --- API 키 ---
kakao_js_key = "3d91fd34529d5628fb6503bc106ebd0d"
naver_client_id = "exj399xajq"  # JavaScript SDK용 Client ID

# --- UI 구성 ---
app_ui = ui.page_fluid(
    ui.h2("🗺️ 카카오 지도 + 네이버 지도 함께 보기"),
    # --- 카카오 지도 영역 (변경 없음) ---
    ui.h4("카카오 지도 (서울시청 중심, 교통정보 포함)"),
    tags.div(id="kakao_map", style="width:100%; height:400px; margin-bottom:30px;"),
    tags.script(
        src=f"https://dapi.kakao.com/v2/maps/sdk.js?appkey={kakao_js_key}&autoload=false"
    ),
    tags.script(
        HTML(
            """
        document.addEventListener("DOMContentLoaded", function () {
            kakao.maps.load(function () {
                var container = document.getElementById('kakao_map');
                var options = {
                    center: new kakao.maps.LatLng(37.566826, 126.9786567),
                    level: 3
                };
                var map = new kakao.maps.Map(container, options);
                map.addOverlayMapTypeId(kakao.maps.MapTypeId.TRAFFIC);
            });
        });
    """
        )
    ),
    # --- 네이버 지도 영역 (수정된 부분) ---
    ui.h4("네이버 지도 (서울시청 중심)"),
    tags.div(id="naver_map", style="width:100%; height:400px; margin-top:30px;"),
    # → SDK 로드: 반드시 `clientId` 파라미터 사용
    tags.script(
        src=f"https://openapi.map.naver.com/openapi/v3/maps.js?ncpClientId={naver_client_id}"
    ),
    # → SDK 로드 후 초기화
    tags.script(
        HTML(
            """
        document.addEventListener("DOMContentLoaded", function () {
            var mapOptions = {
                center: new naver.maps.LatLng(37.566826, 126.9786567),
                zoom: 10
            };
            var map = new naver.maps.Map('naver_map', mapOptions);
        });
    """
        )
    ),
)


# --- 서버 구성 ---
def server(input, output, session):
    pass


# --- 앱 실행 ---
app = App(app_ui, server)
