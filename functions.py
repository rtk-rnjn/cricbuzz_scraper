from __future__ import annotations

import asyncio
from concurrent.futures import ThreadPoolExecutor
from functools import partial, wraps

from typing import Any, List, Optional

from bs4 import BeautifulSoup
from html import unescape
import re


class ToAsync:
    def __init__(self, *, executor: Optional[ThreadPoolExecutor] = None):

        self.executor = executor

    def __call__(self, blocking):
        @wraps(blocking)
        async def wrapper(*args, **kwargs):

            loop = asyncio.get_event_loop()
            if not self.executor:
                self.executor = ThreadPoolExecutor()

            func = partial(blocking, *args, **kwargs)

            return await loop.run_in_executor(self.executor, func)

        return wrapper


def __parse_text(st: str) -> str:
    return re.sub(r" +", " ", unescape(st).replace("\n", " "))


def parse_text(st: str) -> str:
    return __parse_text(st)


@ToAsync()
def find_one(soup: BeautifulSoup, name: str, **kwargs: Any) -> Optional[str]:

    if finder := soup.find(name, kwargs):
        return __parse_text(finder.text)

    return "Data not available"


@ToAsync()
def find_all(soup: BeautifulSoup, name: str, **kwargs: Any) -> Optional[List[str]]:
    if finder := soup.find_all(name, kwargs):
        return [__parse_text(i.text) for i in finder]

    return ["Data not available"]


@ToAsync()
def parse_url(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "html.parser")


@ToAsync()
def get_batting(soup: BeautifulSoup) -> Dict[str, Any]:
    table = soup.find_all("table", {"class": "table table-condensed"})
    data = [
        [__parse_text(i.text) for i in mini_table.find_all("td")] for mini_table in table
    ]
    i = data[0]
    return dict(zip(i, zip(i[10:], i[5:10])))


@ToAsync()
def get_bowling(soup: BeautifulSoup) -> Dict[str, Any]:
    data = [
        [__parse_text(i.text) for i in mini_table.find_all("td")] for mini_table in soup.find_all("table", {"class": "table table-condensed"})
    ]
    i = data[1]
    return dict(zip(i, zip(i[10:], i[5:10])))
  