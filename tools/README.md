# 색인 가속 도구 (IndexNow · Google)

빌드(`python3 build.py`)는 다음을 사이트 루트에 생성합니다.

| 파일 | 용도 |
|------|------|
| `sitemap.xml` | 색인 페이지 전체 + `lastmod`·`changefreq`·`priority` |
| `rss.xml` | 구글·네이버 발견용 RSS 2.0 피드 |
| `robots.txt` | `*`/Googlebot/Yeti(네이버)/bingbot 허용 + Sitemap·RSS 위치 |
| `{INDEXNOW_KEY}.txt` | IndexNow 소유 확인 키 파일(공개) |

## 1. 빙·네이버·얀덱스 — IndexNow (즉시 통보)

```bash
python3 build.py                 # 결과물·키 파일 생성
python tools/indexnow.py         # sitemap의 모든 URL 즉시 통보 (첫 일괄)
python tools/indexnow.py https://busan-massage.pages.dev/busan/haeundae-gu/u-dong-chuljangmassage/
                                 # 새 글/수정 URL만 통보 (글 올릴 때마다)
```

- 키 파일이 **배포된 도메인에서 실제로 열려야** 통보가 검증됩니다. 배포 후 실행하세요.
- 응답 `200`/`202` = 접수됨.
- Naver는 IndexNow 참여사입니다(searchadvisor 엔드포인트 포함). 별도 등록은
  Naver 서치어드바이저에서 사이트 등록 + 사이트맵 제출도 함께 권장합니다.

## 2. 구글 — 사이트맵 + (옵션) Indexing API

구글은 IndexNow 미참여입니다. 또한 **사이트맵 ping 엔드포인트는 2023년 폐지**되어
더 이상 동작하지 않습니다. 구글의 정석 경로는:

1. Search Console에 속성 등록 → `sitemap.xml` 제출
2. 중요 URL은 URL 검사 → "색인 생성 요청"
3. (옵션) Indexing API — `tools/google_indexing.py`

```bash
pip install google-auth requests
export GOOGLE_APPLICATION_CREDENTIALS=/path/서비스계정.json
python tools/google_indexing.py        # sitemap 전체 URL_UPDATED
```

> Indexing API는 공식적으로 JobPosting·BroadcastEvent용이며 일반 페이지 색인을
> 보장하지 않습니다. 일반 콘텐츠는 사이트맵 + 내부링크 + 색인 요청이 가장 확실합니다.

## 3. 자동화 (글 올릴 때마다)

새 페이지를 추가/수정한 뒤:

```bash
python3 build.py && \
python tools/indexnow.py $NEW_URL && \
python tools/google_indexing.py $NEW_URL   # 서비스계정 설정 시
```

CI(GitHub Actions 등)에 배포 후 위 두 줄을 넣으면 푸시마다 자동 통보됩니다.
