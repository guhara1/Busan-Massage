# 전체 페이지 목록 집계 — 부산 간다GO
import importlib
import pkgutil

from . import main, areas, stations, living, info, about

PAGES = (
    [main.PAGE]
    + areas.PAGES
    + stations.PAGES
    + living.PAGES
    + info.PAGES
    + [about.PAGE]
)

# 대표 동·읍·면 모듈(content/dong_*.py)을 자동 수집해 합친다.
# (dong_data.py 는 데이터 전용이므로 제외)
_dong_mods = sorted(
    name
    for _, name, _ in pkgutil.iter_modules(__path__)
    if name.startswith("dong_") and name != "dong_data"
)
for _name in _dong_mods:
    _mod = importlib.import_module(f"{__name__}.{_name}")
    PAGES += getattr(_mod, "PAGES", [])
