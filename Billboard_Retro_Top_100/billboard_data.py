import requests
from bs4 import BeautifulSoup


class BillboardData:
    def __init__(self, date):
        self.artists_tag = None
        self.songs = None
        self.billboard_year_chart_url = f"https://www.billboard.com/charts/year-end/{date}/hot-100-songs/"
        self.billboard_month_chart_url = f"https://www.billboard.com/charts/hot-100/{date}/"
        self.header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
        self.artists = []

        try:
            billboard_response = requests.get(url=self.billboard_year_chart_url, headers=self.header)

            if billboard_response.status_code != 200:
                raise Exception(f"Year chart request failed with status {billboard_response.status_code}")
            else:
                print(self.billboard_year_chart_url)
        except Exception as e:
            billboard_response = requests.get(url=self.billboard_month_chart_url, headers=self.header)
            print(self.billboard_month_chart_url)
        self.soup = BeautifulSoup(billboard_response.text, "html.parser")

    def get_songs(self):
        self.songs = [song.getText().strip() for song in self.soup.select(".o-chart-results-list__item .c-title")]
        return self.songs

    def get_artists(self):
        self.artists_tag = [tag for tag in self.soup.select(".o-chart-results-list__item")]
        for tag in self.artists_tag:
            if tag.select(".c-title"):
                self.artists.append(tag.select(".c-label")[0].getText().strip())
        return self.artists
