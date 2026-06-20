# 사이트 공통 설정
# 배포 도메인 확정 후 BASE_URL 을 실제 도메인으로 변경하세요.
BASE_URL = "https://busan-massage.pages.dev"

BRAND = "간다GO"
BRAND_MARK = "간"
PHONE = "0508-202-4719"
PHONE_DISPLAY = "0508-202-4719"

# 상단 메뉴 — 하위 메뉴에는 키워드를 반복하지 않고 지역명·역명만 표시한다.
NAV = [
    ("부산 홈", "/", [
        ("부산 출장마사지 메인", "/"),
        ("부산 홈타이 이용 기준", "/guide/#standard"),
        ("16개 구·군 선택 안내", "/busan/"),
        ("예약 전 확인사항", "/check/#address"),
    ]),
    ("지역별 안내", "/busan/", [
        ("부산 전체", "/busan/"),
        ("중구", "/busan/jung-gu-chuljangmassage/"),
        ("서구", "/busan/seo-gu-chuljangmassage/"),
        ("동구", "/busan/dong-gu-chuljangmassage/"),
        ("영도구", "/busan/yeongdo-gu-chuljangmassage/"),
        ("부산진구", "/busan/busanjin-gu-chuljangmassage/"),
        ("동래구", "/busan/dongnae-gu-chuljangmassage/"),
        ("남구", "/busan/nam-gu-chuljangmassage/"),
        ("북구", "/busan/buk-gu-chuljangmassage/"),
        ("해운대구", "/busan/haeundae-gu-chuljangmassage/"),
        ("사하구", "/busan/saha-gu-chuljangmassage/"),
        ("금정구", "/busan/geumjeong-gu-chuljangmassage/"),
        ("강서구", "/busan/gangseo-gu-chuljangmassage/"),
        ("연제구", "/busan/yeonje-gu-chuljangmassage/"),
        ("수영구", "/busan/suyeong-gu-chuljangmassage/"),
        ("사상구", "/busan/sasang-gu-chuljangmassage/"),
        ("기장군", "/busan/gijang-gun-chuljangmassage/"),
    ]),
    ("역세권 안내", "/busan/stations/", [
        ("역세권 전체", "/busan/stations/"),
        ("부산역", "/busan/busan-station-chuljangmassage/"),
        ("서면역", "/busan/seomyeon-station-chuljangmassage/"),
        ("해운대역", "/busan/haeundae-station-chuljangmassage/"),
        ("센텀시티역", "/busan/centum-city-station-chuljangmassage/"),
        ("광안역", "/busan/gwangan-station-chuljangmassage/"),
        ("수영역", "/busan/suyeong-station-chuljangmassage/"),
        ("남포역", "/busan/nampo-station-chuljangmassage/"),
        ("자갈치역", "/busan/jagalchi-station-chuljangmassage/"),
        ("동래역", "/busan/dongnae-station-chuljangmassage/"),
        ("연산역", "/busan/yeonsan-station-chuljangmassage/"),
        ("사상역", "/busan/sasang-station-chuljangmassage/"),
        ("하단역", "/busan/hadan-station-chuljangmassage/"),
        ("부산대역", "/busan/busan-national-univ-station-chuljangmassage/"),
        ("덕천역", "/busan/deokcheon-station-chuljangmassage/"),
        ("장산역", "/busan/jangsan-station-chuljangmassage/"),
        ("기장역", "/busan/gijang-station-chuljangmassage/"),
    ]),
    ("생활권 안내", "/busan/areas/", [
        ("생활권 전체", "/busan/areas/"),
        ("해운대 해수욕장", "/busan/haeundae-beach-area-chuljangmassage/"),
        ("센텀시티·벡스코", "/busan/centum-bexco-area-chuljangmassage/"),
        ("서면·전포", "/busan/seomyeon-jeonpo-area-chuljangmassage/"),
        ("남포동·자갈치", "/busan/nampo-jagalchi-area-chuljangmassage/"),
        ("부산역·초량", "/busan/busan-station-choryang-area-chuljangmassage/"),
        ("광안리·수영", "/busan/gwangalli-suyeong-area-chuljangmassage/"),
        ("동래·온천장", "/busan/dongnae-oncheonjang-area-chuljangmassage/"),
        ("사상터미널", "/busan/sasang-terminal-area-chuljangmassage/"),
        ("하단·다대포", "/busan/hadan-dadaepo-area-chuljangmassage/"),
        ("명지·강서", "/busan/myeongji-gangseo-area-chuljangmassage/"),
        ("정관·기장", "/busan/jeonggwan-gijang-area-chuljangmassage/"),
        ("부산대·금정", "/busan/busan-univ-geumjeong-area-chuljangmassage/"),
    ]),
    ("예약 안내", "/reservation/", [
        ("예약 가능 지역 확인", "/reservation/#area"),
        ("예약 가능 시간 안내", "/reservation/#hours"),
        ("추가 이동비 안내", "/reservation/#fee"),
        ("결제 방식 안내", "/reservation/#payment"),
        ("예약 변경 안내", "/reservation/#change"),
        ("취소 기준 안내", "/reservation/#cancel"),
    ]),
    ("이용 전 확인사항", "/check/", [
        ("방문 가능 주소 확인", "/check/#address"),
        ("자택 이용 전 확인사항", "/check/#home"),
        ("숙소 이용 전 확인사항", "/check/#lodging"),
        ("사무실 인근 이용 전 확인사항", "/check/#office"),
        ("개인정보 처리 기준", "/check/#privacy"),
        ("고객 안전 안내", "/check/#safety"),
        ("불법·선정적 서비스 불가 안내", "/check/#prohibited"),
    ]),
    ("홈타이 이용 가이드", "/guide/", [
        ("홈타이란?", "/guide/#what"),
        ("출장마사지와 홈타이 차이", "/guide/#diff"),
        ("부산 홈타이 이용 전 기준", "/guide/#standard"),
        ("지역별 이동 기준", "/guide/#move"),
        ("추가 비용 확인 기준", "/guide/#fee"),
        ("처음 이용하는 고객 안내", "/guide/#first"),
    ]),
    ("고객센터", "/support/", [
        ("문의하기", "/support/#contact"),
        ("자주 묻는 질문", "/support/#faq"),
        ("운영 기준", "/support/#policy"),
        ("사이트 소개", "/about/"),
        ("개인정보 처리방침", "/support/privacy/"),
        ("이용약관", "/support/terms/"),
    ]),
]
