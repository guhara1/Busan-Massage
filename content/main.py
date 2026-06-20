# 메인 페이지 — 부산 출장마사지·홈타이 허브. 키워드를 밀어 넣지 않고 상세 페이지로 연결한다.
from .site import BASE_URL, BRAND, PHONE, PHONE_DISPLAY
from .pricing import PRICING

_NAVER = '<meta name="naver-site-verification" content="68ea54219a78b253631d6bb938deefc1d19c8395" />\n'

_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "name": "부산 출장마사지·홈타이 지역별 예약 안내",
  "url": "{BASE_URL}/",
  "description": "부산 16개 구·군 출장마사지·홈타이 방문 관리 지역별 예약 안내",
  "inLanguage": "ko-KR",
  "primaryImageOfPage": {{
    "@type": "ImageObject",
    "url": "{BASE_URL}/assets/og-image.png",
    "width": 1200,
    "height": 630
  }},
  "publisher": {{
    "@type": "Organization",
    "name": "{BRAND}",
    "url": "{BASE_URL}/",
    "telephone": "{PHONE}",
    "logo": {{
      "@type": "ImageObject",
      "url": "{BASE_URL}/assets/icon-512.png"
    }},
    "image": "{BASE_URL}/assets/og-image.png",
    "areaServed": {{
      "@type": "AdministrativeArea",
      "name": "부산광역시"
    }}
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "{BRAND}",
  "url": "{BASE_URL}/",
  "telephone": "{PHONE}",
  "image": "{BASE_URL}/assets/og-image.png",
  "logo": "{BASE_URL}/assets/icon-512.png",
  "description": "부산 16개 구·군 방문 출장마사지·홈타이 예약 안내",
  "areaServed": {{
    "@type": "AdministrativeArea",
    "name": "부산광역시"
  }}
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{
      "@type": "ListItem",
      "position": 1,
      "name": "부산 출장마사지·홈타이",
      "item": "{BASE_URL}/"
    }}
  ]
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {{
      "@type": "Question",
      "name": "부산 전지역 방문이 가능한가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "부산 16개 구·군을 지역별 안내로 제공합니다. 가능 여부는 예약 시간, 정확한 위치, 추가 이동비, 배정 상황에 따라 달라지므로 예약 전화에서 위치 기준으로 확인합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "해운대·서면·광안리 같은 역세권도 안내하나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "부산역, 서면역, 해운대역, 센텀시티역, 광안역, 사상역 등 핵심 역세권을 별도 페이지로 안내합니다. 환승역도 노선·출구별로 나누지 않고 역마다 페이지 하나만 운영합니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "대연1동, 우1동 같은 번호 동은 왜 따로 없나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "번호가 붙은 행정동은 대표 동으로 통합해 안내합니다. 대연1~6동은 대연동, 우1~3동은 우동, 연산1~9동은 연산동 페이지에서 함께 다뤄 중복 페이지 위험을 줄입니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "강서구나 기장군처럼 외곽도 방문되나요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "명지·강서, 정관·기장 같은 외곽 생활권은 지하철보다 차량 이동이 기준이 됩니다. 예약 가능 시간과 추가 이동비를 먼저 확인한 뒤 방문 여부를 안내해 드립니다."
      }}
    }},
    {{
      "@type": "Question",
      "name": "홈타이와 출장마사지는 어떻게 다른가요?",
      "acceptedAnswer": {{
        "@type": "Answer",
        "text": "두 표현 모두 자택·숙소·사무실 인근으로 방문하는 관리 서비스를 가리킵니다. 차이와 이용 기준은 홈타이 이용 가이드 페이지에서 정리해 두었습니다."
      }}
    }}
  ]
}}
</script>
"""

_HERO = f"""<section class="hero">
  <div class="hero-inner">
    <p class="hero-badge">Premium Visiting Spa · 부산 16개 구·군</p>
    <h1>부산 출장마사지 · 부산광역시 홈타이<br>지역별 예약 안내</h1>
    <p class="hero-lead">샵까지 갈 필요 없이, 계신 곳에서 받는 방문 관리.<br>해운대·서면·광안리·남포동·기장까지 전화 한 통이면 가능 지역을 확인합니다.</p>
    <div class="hero-actions">
      <a class="hero-btn primary" href="tel:{PHONE}">📞 {PHONE_DISPLAY}</a>
      <a class="hero-btn" href="/busan/">16개 구·군 보기</a>
    </div>
    <ul class="hero-stats">
      <li><strong>16개</strong><span>구·군 안내</span></li>
      <li><strong>16개</strong><span>핵심 역세권</span></li>
      <li><strong>12개</strong><span>생활권 거점</span></li>
      <li><strong>24시간</strong><span>예약 상담</span></li>
    </ul>
  </div>
</section>
"""

_BODY = f"""
<section id="intro">
<h2>부산에서 출장마사지를 찾을 때 먼저 확인할 기준</h2>
<p>부산에서 출장마사지나 홈타이를 찾는 분들은 보통 현재 위치에서 가까운 방문 가능 지역을 먼저 확인합니다. 부산은 해운대와 센텀시티처럼 관광·업무 수요가 함께 있는 지역, 서면과 전포처럼 상권과 교통이 집중된 지역, 남포동과 자갈치처럼 원도심 생활권이 강한 지역, 기장과 명지처럼 차량 이동 기준이 중요한 지역이 한 도시 안에 섞여 있습니다. 그래서 이 사이트는 단순히 ‘부산 전지역 가능’이라고만 적는 방식 대신, 구·군과 생활권을 나누어 안내합니다. 방문 가능 여부는 행정 경계가 아니라 정확한 위치와 예약 시간, 추가 이동비로 판단하므로, 먼저 본인이 계신 곳이 어느 구·군과 생활권에 속하는지 확인하신 뒤 예약 전화에서 도로명 주소를 알려주시면 가장 빠르게 안내받으실 수 있습니다. {BRAND}는 예약 확인부터 방문까지 정해진 절차로만 진행하며, 안내된 관리 범위와 위생·안전 기준 안에서만 서비스를 제공합니다.</p>
</section>

<section id="districts">
<h2>16개 구·군별 방문 가능 지역 안내</h2>
<p>부산광역시는 15개 구와 1개 군으로 이루어져 있습니다. 이 사이트는 중구, 서구, 동구, 영도구, 부산진구, 동래구, 남구, 북구, 해운대구, 사하구, 금정구, 강서구, 연제구, 수영구, 사상구, 기장군 16개 구·군을 1차 지역 허브로 두고, 각 구·군 페이지에서 생활권 차이를 설명합니다. 우1·2·3동은 우동, 대연1~6동은 대연동, 연산1~9동은 연산동처럼 번호가 붙은 행정동은 대표 동 하나로 통합해, 같은 본문을 반복하는 도어웨이식 구성을 피했습니다. 아래에서 현재 위치에 맞는 구·군을 먼저 선택해 주세요.</p>
<ul class="card-grid">
<li><a href="/busan/jung-gu-chuljangmassage/">중구</a></li>
<li><a href="/busan/seo-gu-chuljangmassage/">서구</a></li>
<li><a href="/busan/dong-gu-chuljangmassage/">동구</a></li>
<li><a href="/busan/yeongdo-gu-chuljangmassage/">영도구</a></li>
<li><a href="/busan/busanjin-gu-chuljangmassage/">부산진구</a></li>
<li><a href="/busan/dongnae-gu-chuljangmassage/">동래구</a></li>
<li><a href="/busan/nam-gu-chuljangmassage/">남구</a></li>
<li><a href="/busan/buk-gu-chuljangmassage/">북구</a></li>
<li><a href="/busan/haeundae-gu-chuljangmassage/">해운대구</a></li>
<li><a href="/busan/saha-gu-chuljangmassage/">사하구</a></li>
<li><a href="/busan/geumjeong-gu-chuljangmassage/">금정구</a></li>
<li><a href="/busan/gangseo-gu-chuljangmassage/">강서구</a></li>
<li><a href="/busan/yeonje-gu-chuljangmassage/">연제구</a></li>
<li><a href="/busan/suyeong-gu-chuljangmassage/">수영구</a></li>
<li><a href="/busan/sasang-gu-chuljangmassage/">사상구</a></li>
<li><a href="/busan/gijang-gun-chuljangmassage/">기장군</a></li>
</ul>
<p>구·군 전체 구조는 <a href="/busan/">지역별 안내</a>에서 한눈에 확인하실 수 있습니다.</p>
</section>

<section id="areas">
<h2>해운대·서면·광안리·남포동·부산역 생활권 차이</h2>
<p>같은 부산이라도 생활권마다 검색 의도와 방문 수요가 다릅니다. 해운대 해수욕장과 센텀시티는 관광·숙소·전시 수요가 강하고, 서면·전포는 상권과 환승이 집중된 곳이며, 광안리·수영은 해변과 주거가 함께 있는 지역입니다. 남포동·자갈치와 부산역·초량은 원도심 생활권으로 묶이고, 명지·강서나 정관·기장은 차량 이동이 기준이 되는 외곽 신도시 생활권입니다. 생활권 페이지는 구·군 페이지나 역세권 페이지와 다른 각도에서 그 지역만의 방문 조건을 다룹니다.</p>
<ul class="card-grid">
<li><a href="/busan/haeundae-beach-area-chuljangmassage/">해운대 해수욕장</a></li>
<li><a href="/busan/centum-bexco-area-chuljangmassage/">센텀시티·벡스코</a></li>
<li><a href="/busan/seomyeon-jeonpo-area-chuljangmassage/">서면·전포</a></li>
<li><a href="/busan/nampo-jagalchi-area-chuljangmassage/">남포동·자갈치</a></li>
<li><a href="/busan/gwangalli-suyeong-area-chuljangmassage/">광안리·수영</a></li>
<li><a href="/busan/myeongji-gangseo-area-chuljangmassage/">명지·강서</a></li>
<li><a href="/busan/jeonggwan-gijang-area-chuljangmassage/">정관·기장</a></li>
</ul>
<p>전체 생활권 목록은 <a href="/busan/areas/">생활권 안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="stations">
<h2>부산역·서면역·해운대역·사상역 핵심 역세권 안내</h2>
<p>역 기준으로 위치를 떠올리는 분들을 위해 부산의 핵심 역세권을 별도로 안내합니다. 부산역, 서면역, 해운대역, 센텀시티역, 광안역, 수영역, 남포역, 자갈치역, 동래역, 연산역, 사상역, 하단역, 부산대역, 덕천역, 장산역, 기장역을 다룹니다. 서면역·연산역·동래역·수영역·사상역처럼 노선이 두 개 이상인 환승역도 페이지는 하나만 운영하며, 노선별·출구별로 페이지를 쪼개지 않습니다. 예정역이나 미개통역은 별도 색인 페이지로 만들지 않습니다.</p>
<ul class="card-grid">
<li><a href="/busan/busan-station-chuljangmassage/">부산역</a></li>
<li><a href="/busan/seomyeon-station-chuljangmassage/">서면역</a></li>
<li><a href="/busan/haeundae-station-chuljangmassage/">해운대역</a></li>
<li><a href="/busan/centum-city-station-chuljangmassage/">센텀시티역</a></li>
<li><a href="/busan/gwangan-station-chuljangmassage/">광안역</a></li>
<li><a href="/busan/nampo-station-chuljangmassage/">남포역</a></li>
<li><a href="/busan/sasang-station-chuljangmassage/">사상역</a></li>
<li><a href="/busan/hadan-station-chuljangmassage/">하단역</a></li>
</ul>
<p>16개 역 전체는 <a href="/busan/stations/">역세권 안내</a>에서 확인하실 수 있습니다.</p>
</section>

<section id="check">
<h2>부산 홈타이 예약 전 확인사항</h2>
<p>부산 출장마사지와 홈타이를 예약하기 전에는 방문 가능 지역, 예약 가능 시간, 추가 이동비, 결제 방식, 취소 기준, 개인정보 처리 기준을 먼저 확인하시는 것이 좋습니다. 같은 부산 안에서도 해운대·센텀과 명지·기장, 남포동·서면의 이동 기준은 다릅니다. 특히 주말 해운대, 광안리, 센텀시티, 사상터미널, 부산역 주변은 시간대에 따라 이동 시간이 달라질 수 있어 추가 이동비가 안내될 수 있습니다. 자택·숙소·사무실 인근별 준비사항은 <a href="/check/">이용 전 확인사항</a>에, 예약 절차와 변경·취소 기준은 <a href="/reservation/">예약 안내</a>에 정리해 두었습니다. 홈타이가 처음이라면 <a href="/guide/">홈타이 이용 가이드</a>를 먼저 보시면 이용 흐름을 쉽게 이해하실 수 있습니다.</p>
</section>

<section id="policy">
<h2>부산 지역 페이지 중복 방지 운영 기준</h2>
<p>이 사이트는 검색엔진을 속이기 위한 도어웨이 페이지를 만들지 않습니다. 1동·2동·3동처럼 번호가 붙은 동은 개별 페이지로 나누지 않고 대표 동 하나로 통합하며, 환승역은 역마다 URL 하나만 사용합니다. 지역명만 바꿔 같은 본문을 반복하지 않고, 각 페이지는 그 지역의 생활권·상권·이동 기준을 고유하게 설명합니다. 또한 실제 오프라인 사업장 주소가 없는 방문형 안내 사이트이므로, 위치를 가장하는 LocalBusiness 구조화 데이터 대신 WebPage·Organization 정보를 사용합니다. 불법·선정적 표현, 허위 후기, 가짜 체험담, 과도한 할인 문구는 사용하지 않으며, 방문 가능 지역과 예약 전 확인사항 같은 신뢰형 정보 문장으로만 구성합니다.</p>
</section>

<section id="howto">
<h2>부산 출장마사지 사이트 이용 방법</h2>
<p>이용 순서는 간단합니다. 먼저 메인에서 현재 위치에 맞는 구·군을 고르고, 필요하면 가까운 역세권이나 생활권 페이지로 이동해 세부 안내를 확인합니다. 그다음 예약 가능 시간과 추가 이동비를 점검하고, 예약 전화로 도로명 주소와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다. 메인페이지는 부산 전체 안내를 담당하고, 16개 구·군 페이지는 각 지역의 생활권 차이를, 역세권 페이지는 실제 검색 수요가 큰 역을, 생활권 페이지는 관광·업무·해변·터미널 같은 거점 수요를 담당합니다. 본인에게 익숙한 기준으로 보셔도 예약 절차는 동일합니다.</p>
</section>

<section id="faq">
<h2>자주 묻는 질문</h2>
<div class="faq-item">
<h3>부산 전지역 방문이 가능한가요?</h3>
<p>부산 16개 구·군을 지역별 안내로 제공합니다. 가능 여부는 예약 시간, 정확한 위치, 추가 이동비, 배정 상황에 따라 달라지므로 예약 전화에서 위치 기준으로 확인합니다.</p>
</div>
<div class="faq-item">
<h3>해운대·서면·광안리 같은 역세권도 안내하나요?</h3>
<p>부산역, 서면역, 해운대역, 센텀시티역, 광안역, 사상역 등 핵심 역세권을 별도 페이지로 안내합니다. 환승역도 노선·출구별로 나누지 않고 역마다 페이지 하나만 운영합니다.</p>
</div>
<div class="faq-item">
<h3>대연1동, 우1동 같은 번호 동은 왜 따로 없나요?</h3>
<p>번호가 붙은 행정동은 대표 동으로 통합해 안내합니다. 대연1~6동은 대연동, 우1~3동은 우동, 연산1~9동은 연산동 페이지에서 함께 다뤄 중복 페이지 위험을 줄입니다.</p>
</div>
<div class="faq-item">
<h3>강서구나 기장군처럼 외곽도 방문되나요?</h3>
<p>명지·강서, 정관·기장 같은 외곽 생활권은 지하철보다 차량 이동이 기준이 됩니다. 예약 가능 시간과 추가 이동비를 먼저 확인한 뒤 방문 여부를 안내해 드립니다.</p>
</div>
<div class="faq-item">
<h3>홈타이와 출장마사지는 어떻게 다른가요?</h3>
<p>두 표현 모두 자택·숙소·사무실 인근으로 방문하는 관리 서비스를 가리킵니다. 차이와 이용 기준은 <a href="/guide/">홈타이 이용 가이드</a> 페이지에서 정리해 두었습니다.</p>
</div>
</section>

{PRICING}
<section id="contact" class="cta">
<h2>예약문의</h2>
<p>부산 방문 관리 예약과 상담은 전화로 가장 빠르게 진행됩니다. 위치와 희망 시간을 알려주시면 가능 여부를 바로 확인해 드립니다.</p>
<a class="cta-phone" href="tel:{PHONE}">{PHONE_DISPLAY}</a>
</section>
"""

PAGE = {
    "path": "",
    "title": "부산 출장마사지｜16개 구·군 홈타이 지역별 예약 안내",
    "desc": "부산 출장마사지·홈타이 예약 전 해운대, 서면, 광안리, 남포동, 기장 생활권을 확인하세요.",
    "h1": "부산 출장마사지 · 부산광역시 홈타이 지역별 예약 안내",
    "body": _BODY,
    "extra_head": _NAVER + _JSONLD,
    "breadcrumb": [],
    "hero": _HERO,
}
