# 대표 동·읍·면 데이터 — 단일 출처(slug·이름·상위 구).
# URL 패턴: /busan/{gu_base}/{dong_slug}-chuljangmassage/
# 번호 행정동은 대표 동 1개로 통합한다(도어웨이 방지).

# (gu_base, gu_name, gu_path) -> list of (dong_name, dong_slug)
DONGS = [
    ("jung-gu", "중구", "/busan/jung-gu-chuljangmassage/", [
        ("중앙동", "jungang-dong"), ("동광동", "donggwang-dong"), ("대청동", "daecheong-dong"),
        ("보수동", "bosu-dong"), ("부평동", "bupyeong-dong"), ("광복동", "gwangbok-dong"),
        ("남포동", "nampo-dong"), ("영주동", "yeongju-dong"),
    ]),
    ("seo-gu", "서구", "/busan/seo-gu-chuljangmassage/", [
        ("동대신동", "dongdaesin-dong"), ("서대신동", "seodaesin-dong"), ("부민동", "bumin-dong"),
        ("아미동", "ami-dong"), ("초장동", "chojang-dong"), ("충무동", "chungmu-dong"),
        ("남부민동", "nambumin-dong"), ("암남동", "amnam-dong"),
    ]),
    ("dong-gu", "동구", "/busan/dong-gu-chuljangmassage/", [
        ("초량동", "choryang-dong"), ("수정동", "sujeong-dong"),
        ("좌천동", "jwacheon-dong"), ("범일동", "beomil-dong"),
    ]),
    ("yeongdo-gu", "영도구", "/busan/yeongdo-gu-chuljangmassage/", [
        ("남항동", "namhang-dong"), ("영선동", "yeongseon-dong"), ("신선동", "sinseon-dong"),
        ("봉래동", "bongnae-dong"), ("청학동", "cheonghak-dong"), ("동삼동", "dongsam-dong"),
    ]),
    ("busanjin-gu", "부산진구", "/busan/busanjin-gu-chuljangmassage/", [
        ("부전동", "bujeon-dong"), ("연지동", "yeonji-dong"), ("초읍동", "choeup-dong"),
        ("양정동", "yangjeong-dong"), ("전포동", "jeonpo-dong"), ("부암동", "buam-dong"),
        ("당감동", "danggam-dong"), ("가야동", "gaya-dong"), ("개금동", "gaegeum-dong"),
        ("범천동", "beomcheon-dong"),
    ]),
    ("dongnae-gu", "동래구", "/busan/dongnae-gu-chuljangmassage/", [
        ("수민동", "sumin-dong"), ("복산동", "boksan-dong"), ("명륜동", "myeongnyun-dong"),
        ("온천동", "oncheon-dong"), ("사직동", "sajik-dong"), ("안락동", "allak-dong"),
        ("명장동", "myeongjang-dong"),
    ]),
    ("nam-gu", "남구", "/busan/nam-gu-chuljangmassage/", [
        ("대연동", "daeyeon-dong"), ("용호동", "yongho-dong"), ("용당동", "yongdang-dong"),
        ("감만동", "gamman-dong"), ("우암동", "uam-dong"), ("문현동", "munhyeon-dong"),
    ]),
    ("buk-gu", "북구", "/busan/buk-gu-chuljangmassage/", [
        ("구포동", "gupo-dong"), ("금곡동", "geumgok-dong"), ("화명동", "hwamyeong-dong"),
        ("덕천동", "deokcheon-dong"), ("만덕동", "mandeok-dong"),
    ]),
    ("haeundae-gu", "해운대구", "/busan/haeundae-gu-chuljangmassage/", [
        ("우동", "u-dong"), ("중동", "jung-dong"), ("좌동", "jwa-dong"),
        ("송정동", "songjeong-dong"), ("반여동", "banyeo-dong"), ("반송동", "bansong-dong"),
        ("재송동", "jaesong-dong"),
    ]),
    ("saha-gu", "사하구", "/busan/saha-gu-chuljangmassage/", [
        ("괴정동", "goejeong-dong"), ("당리동", "dangni-dong"), ("하단동", "hadan-dong"),
        ("신평동", "sinpyeong-dong"), ("장림동", "jangnim-dong"), ("다대동", "dadae-dong"),
        ("구평동", "gupyeong-dong"), ("감천동", "gamcheon-dong"),
    ]),
    ("geumjeong-gu", "금정구", "/busan/geumjeong-gu-chuljangmassage/", [
        ("서동", "seo-dong"), ("금사동", "geumsa-dong"), ("부곡동", "bugok-dong"),
        ("장전동", "jangjeon-dong"), ("선두구동", "seondugu-dong"), ("청룡노포동", "cheongnyongnopo-dong"),
        ("남산동", "namsan-dong"), ("구서동", "guseo-dong"), ("금성동", "geumseong-dong"),
    ]),
    ("gangseo-gu", "강서구", "/busan/gangseo-gu-chuljangmassage/", [
        ("대저동", "daejeo-dong"), ("강동동", "gangdong-dong"), ("명지동", "myeongji-dong"),
        ("가락동", "garak-dong"), ("녹산동", "noksan-dong"), ("신호동", "sinho-dong"),
        ("가덕도동", "gadeokdo-dong"),
    ]),
    ("yeonje-gu", "연제구", "/busan/yeonje-gu-chuljangmassage/", [
        ("거제동", "geoje-dong"), ("연산동", "yeonsan-dong"),
    ]),
    ("suyeong-gu", "수영구", "/busan/suyeong-gu-chuljangmassage/", [
        ("남천동", "namcheon-dong"), ("수영동", "suyeong-dong"), ("망미동", "mangmi-dong"),
        ("광안동", "gwangan-dong"), ("민락동", "millak-dong"),
    ]),
    ("sasang-gu", "사상구", "/busan/sasang-gu-chuljangmassage/", [
        ("삼락동", "samnak-dong"), ("모라동", "mora-dong"), ("덕포동", "deokpo-dong"),
        ("괘법동", "gwaebeop-dong"), ("감전동", "gamjeon-dong"), ("주례동", "jurye-dong"),
        ("학장동", "hakjang-dong"), ("엄궁동", "eomgung-dong"),
    ]),
    ("gijang-gun", "기장군", "/busan/gijang-gun-chuljangmassage/", [
        ("기장읍", "gijang-eup"), ("장안읍", "jangan-eup"), ("정관읍", "jeonggwan-eup"),
        ("일광읍", "ilgwang-eup"), ("철마면", "cheolma-myeon"),
    ]),
]


def dong_url(gu_base, dong_slug):
    return f"/busan/{gu_base}/{dong_slug}-chuljangmassage/"
