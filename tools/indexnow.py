#!/usr/bin/env python3
"""IndexNow 즉시 색인 통보 — 빙·네이버·얀덱스.

사용법:
  python tools/indexnow.py                 # sitemap.xml 의 모든 URL 일괄 통보
  python tools/indexnow.py <url> [<url> …]  # 지정한 URL만 통보 (새 글 올릴 때마다)

원리:
  IndexNow는 참여 검색엔진(Bing, Naver, Yandex, Seznam)에 변경된 URL을
  즉시 알려 색인을 앞당기는 프로토콜이다. 키 파일은 빌드 시 사이트 루트에
  "{KEY}.txt" 로 발행된다(build.py). 한 엔드포인트에 보내면 참여 엔진끼리
  공유되지만, 안정성을 위해 공용·빙·네이버 엔드포인트에 함께 통보한다.

  Google은 IndexNow 미참여 — tools/google_indexing.py 참고.
"""
import json
import os
import re
import sys
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL, INDEXNOW_KEY  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = BASE_URL.rstrip("/")
HOST = re.sub(r"^https?://", "", BASE).split("/")[0]
KEY_LOCATION = f"{BASE}/{INDEXNOW_KEY}.txt"

ENDPOINTS = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow",
    "https://searchadvisor.naver.com/indexnow",
    "https://yandex.com/indexnow",
]


def urls_from_sitemap() -> list:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python3 build.py` 를 실행하세요.")
    text = open(path, encoding="utf-8").read()
    return re.findall(r"<loc>(.*?)</loc>", text)


def submit(endpoint: str, urls: list) -> str:
    body = json.dumps({
        "host": HOST,
        "key": INDEXNOW_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls,
    }).encode("utf-8")
    req = urllib.request.Request(
        endpoint, data=body, method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return f"{resp.status} {resp.reason}"
    except urllib.error.HTTPError as e:
        # 200/202 외에도 일부 엔진은 본문 없이 코드만 반환
        return f"{e.code} {e.reason}"
    except Exception as e:  # noqa: BLE001
        return f"ERROR {e}"


def main() -> None:
    args = [a for a in sys.argv[1:] if a.startswith("http")]
    urls = args or urls_from_sitemap()
    if not urls:
        sys.exit("통보할 URL이 없습니다.")
    # IndexNow 한 번에 최대 10,000 URL
    urls = urls[:10000]
    print(f"host={HOST}  key={INDEXNOW_KEY[:8]}…  urls={len(urls)}")
    for ep in ENDPOINTS:
        print(f"  → {ep}  ::  {submit(ep, urls)}")
    print("완료. (200/202 = 접수됨)")


if __name__ == "__main__":
    main()
