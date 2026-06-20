#!/usr/bin/env python3
"""Google Indexing API 통보 (옵션).

Google은 IndexNow에 참여하지 않으므로 별도 경로가 필요하다.
주의: Indexing API는 공식적으로 JobPosting·BroadcastEvent 구조화 데이터
페이지를 위한 것이다. 일반 페이지에도 호출은 동작하지만 색인을 보장하지
않으며, 일반 콘텐츠의 가장 확실한 경로는 Search Console 사이트맵 제출 +
URL 검사 → 색인 요청이다.

사전 준비:
  1) Google Cloud 프로젝트에서 "Indexing API" 사용 설정
  2) 서비스 계정 생성 → JSON 키 다운로드
  3) Search Console 속성에 그 서비스 계정 이메일을 '소유자'로 추가
  4) pip install google-auth requests
  5) 환경변수 GOOGLE_APPLICATION_CREDENTIALS=서비스계정.json

사용법:
  python tools/google_indexing.py                # sitemap.xml 전체 URL_UPDATED
  python tools/google_indexing.py <url> [<url>…] # 지정 URL
  python tools/google_indexing.py --delete <url> # URL_DELETED
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from content.site import BASE_URL  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
SCOPES = ["https://www.googleapis.com/auth/indexing"]


def urls_from_sitemap() -> list:
    path = os.path.join(ROOT, "sitemap.xml")
    if not os.path.exists(path):
        sys.exit("sitemap.xml 이 없습니다. 먼저 `python3 build.py` 를 실행하세요.")
    return re.findall(r"<loc>(.*?)</loc>", open(path, encoding="utf-8").read())


def main() -> None:
    try:
        import google.auth.transport.requests
        from google.oauth2 import service_account
    except ImportError:
        sys.exit("의존성 필요: pip install google-auth requests")

    cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not cred_path or not os.path.exists(cred_path):
        sys.exit("GOOGLE_APPLICATION_CREDENTIALS 환경변수에 서비스계정 JSON 경로를 지정하세요.")

    args = sys.argv[1:]
    notif = "URL_DELETED" if "--delete" in args else "URL_UPDATED"
    targets = [a for a in args if a.startswith("http")] or urls_from_sitemap()

    creds = service_account.Credentials.from_service_account_file(cred_path, scopes=SCOPES)
    session = google.auth.transport.requests.AuthorizedSession(creds)

    ok = 0
    for url in targets:
        r = session.post(ENDPOINT, json={"url": url, "type": notif}, timeout=30)
        flag = "OK" if r.status_code == 200 else f"{r.status_code}"
        if r.status_code == 200:
            ok += 1
        print(f"  {flag}  {notif}  {url}")
    print(f"완료: {ok}/{len(targets)} 성공  (참고: Indexing API는 일반 페이지 색인을 보장하지 않음)")


if __name__ == "__main__":
    main()
