import gsearch

def search (keyword):
    query = 'inurl:linkedin.com "company size" '+ keyword
    client = gsearch.SearchClient(
        query,
        tbs="li:1",
        max_search_result_urls_to_return=100,
        http_429_cool_off_time_in_minutes=45,
        http_429_cool_off_factor=1.5,
        # proxy="socks5h://127.0.0.1:9050",
        verbosity=1,
        verbose_output=True,  # False (only URLs) or True (rank, title, description, and URL)
    )
    client.assign_random_user_agent()
    urls = client.search()
    return urls

res = search("djezzy")
if res:
    print (res[0].get("title"))