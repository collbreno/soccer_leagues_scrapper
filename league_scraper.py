from bs4 import BeautifulSoup
import requests

from constants import USER_AGENT
from match_info import MatchInfo
from date_utils import DateUtils

class LeagueScraper:
    def __init__(self, url) -> None:
        self.url = url
        self.headers = {
            "user-agent": USER_AGENT
        }

    def __get_td_text(self, row, column_name: str) -> str:
        return row.find("td", class_=column_name).get_text().strip()

    def __get_match_info(self, row, competition):
            timestamp = row['data-timestamp']
            time = self.__get_td_text(row, "day")
            home = self.__get_td_text(row, "team-a")
            away = self.__get_td_text(row, "team-b")
            if (DateUtils.is_valid_time(time)):
                return MatchInfo(
                    home = home,
                    away = away,
                    datetime = DateUtils.get_datetime_from_timestamp(timestamp),
                    competition = competition,
                )

    def get_scheduled_matches(self):
        response = requests.get(self.url, headers=self.headers)
        soup = BeautifulSoup(response.content, "html.parser")
        h1_tag = soup.find('div', id='subheading').find('h1')
        competition = h1_tag.get_text()
        table = soup.find("table", class_="matches")
        tbody = table.find("tbody")
        rows = tbody.find_all("tr", class_=lambda value: value and "match" in value)

        for row in rows:
            match = self.__get_match_info(row, competition)
            if match is not None:
                yield match


