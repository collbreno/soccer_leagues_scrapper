from league_scraper import LeagueScraper

if __name__ == '__main__':
    league_url = 'https://br.soccerway.com/national/england/premier-league/20232024/regular-season/r76443/matches/'
    scraper = LeagueScraper(url=league_url)

    for match in scraper.get_scheduled_matches():
        print(match)