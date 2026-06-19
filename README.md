# 간다GO — 부산 출장마사지·홈타이 지역 안내 사이트

부산광역시 16개 구·군 방문 관리(출장마사지·홈타이) 안내용 정적 사이트입니다.
예약전화: **0508-202-4719**

## 구조

- 정적 HTML 사이트 — 어느 호스팅(GitHub Pages, Netlify, 일반 웹서버)에서든 그대로 서빙 가능
- `build.py` + `content/` 패키지에서 페이지를 생성하는 빌드 방식
- 생성물(각 디렉터리의 `index.html`, `sitemap.xml`, `robots.txt`)도 저장소에 포함

```
build.py            # 빌드 스크립트 (레이아웃·글자수 검사·sitemap 생성)
content/
  site.py           # 상호(간다GO)·전화·BASE_URL·메뉴 구조
  main.py           # 부산 메인 (WebPage/Organization/BreadcrumbList/ImageObject/FAQ JSON-LD)
  areas.py          # 지역별: 부산 허브 + 16개 구·군
  stations.py       # 역세권별: 허브 + 16개 핵심 역
  living.py         # 생활권별: 허브 + 12개 주요 거점
  info.py           # 예약 안내·이용 전 확인사항·홈타이 가이드·고객센터·약관
  about.py          # 사이트 소개 (E-E-A-T)
  pricing.py        # 공용 요금 블록
assets/             # CSS(프리미엄 팔레트 + Pretendard), 모바일 내비 JS, 파비콘/OG
```

## 빌드

```bash
python3 build.py
```

빌드 시 페이지별 본문 글자수 리포트가 출력됩니다.

## SEO 운영 원칙 (빌드에 강제됨)

- 메타 디스크립션 **80자 이내** 유지
- 본문 **2,000자 미만 페이지는 자동 `noindex`** 처리되고 sitemap에서 제외
- 번호 행정동(우1·2·3동, 대연1~6동, 연산1~9동 등)은 개별 페이지 없이 **대표 동으로 통합**
- 환승역(서면역·연산역·동래역·수영역·사상역 등)도 **역마다 URL 하나** — 노선/출구별 페이지 없음
- 지역+역+테마 조합 도어웨이 페이지 없음
- 실제 오프라인 사업장 주소가 없는 방문형 사이트이므로 **LocalBusiness Schema 미사용** (WebPage/Organization 사용)
- 페이지마다 고유 본문 — 지역명만 바꾼 복붙 없음

## URL 구조

```
/                                              메인
/busan/                                        지역 허브 (16개 구·군)
/busan/{gu}-chuljangmassage/                   구·군 (예: haeundae-gu, busanjin-gu …)
/busan/stations/                               역세권 허브 (16개 역)
/busan/{station}-chuljangmassage/              역 (예: busan-station, seomyeon-station …)
/busan/areas/                                  생활권 허브 (12개 거점)
/busan/{area}-chuljangmassage/                 생활권 (예: haeundae-beach-area …)
/reservation/ /check/ /guide/ /support/        안내 페이지
/support/privacy/ /support/terms/ /about/
```

## 배포 전 해야 할 일

1. `content/site.py`의 `BASE_URL`을 실제 도메인으로 변경
2. `python3 build.py` 재실행 (canonical·sitemap·robots.txt에 반영됨)
3. Google Search Console에 `sitemap.xml` 제출
4. OG/파비콘 이미지의 브랜드 이니셜이 실제 상호와 일치하는지 확인
