# 전체 페이지 목록 집계 — 부산 간다GO
from . import main, areas, stations, living, info, about

PAGES = (
    [main.PAGE]
    + areas.PAGES
    + stations.PAGES
    + living.PAGES
    + info.PAGES
    + [about.PAGE]
)
