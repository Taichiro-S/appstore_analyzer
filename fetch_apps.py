import requests
ITUNES_STORE_API_ENDPOINT = 'https://itunes.apple.com/search?'
# def fetch_itunes_data(term, country, media='software', limit=10):
    # base_url = "https://itunes.apple.com/search"
    # params = {
    #     'term': term,
    #     'media': media,
    #     'country': country,
    #     'limit': limit
    # }
    # response = requests.get(base_url, params=params, timeout=10)
    # return response.json()
def fetch_app_data(term,country,sort_order='mostPopular', limit=100):
    params = {
        'term': term,
        'entity': 'software',
        'limit': limit,
        'country': country,
        'media': 'software',
        'lang': 'ja_jp'
    }
    response = requests.get(ITUNES_STORE_API_ENDPOINT, params=params, timeout=5)
    result = []
    for app in response.json()['results']:
        # Check if the app supports Japanese
        is_lang_jp = 'JA' in  app['languageCodesISO2A']
        is_lang_us = 'EN' in  app['languageCodesISO2A']
        if not is_lang_jp:
            continue
        
        curr_rating_count = app['userRatingCountForCurrentVersion'] if 'userRatingCountForCurrentVersion' in app else 0
        curr_rating_avg = app['averageUserRatingForCurrentVersion'] if 'averageUserRatingForCurrentVersion' in app else 0
        rating_count = app['userRatingCount'] if 'userRatingCount' in app else 0
        rating_avg = app['averageUserRating'] if 'averageUserRating' in app else 0
        image = app['artworkUrl100'] if 'artworkUrl100' in app else ''
        screenshots = app['screenshotUrls'] if 'screenshotUrls' in app else []
        price = app['formattedPrice'] if 'formattedPrice' in app else ''
        genres = app['genres'] if 'genres' in app else []
        description = app['description'] if 'description' in app else ''
        last_update = app['currentVersionReleaseDate'] if 'currentVersionReleaseDate' in app else ''
        release_date = app['releaseDate'] if 'releaseDate' in app else ''
        app_data = {
            'name': app['trackName'],
            'id': app['trackId'],
            'currRatingCount': curr_rating_count,
            'currRatingAvr': curr_rating_avg,
            'ratingCount': rating_count,
            'ratingAvr': rating_avg,
            # 'image': image,
            # 'screenshots': screenshots,
            # 'isLangJP': is_lang_jp,
            # 'isLangUS': is_lang_us,
            'price': price,
            # 'genres': genres,
            'description': description,
            'lastUpdate': last_update,
            'releaseDate': release_date
        }
        
        result.append(app_data)
    if sort_order == 'mostPopular':
        result.sort(key=lambda x: x['currRatingCount'], reverse=True)
    elif sort_order == 'highestRating':
        result.sort(key=lambda x: x['currRatingAvr'], reverse=True)
    return result