def domain_name(url):
    if "//" in url:
        top_level = url.split('//')[-1]
    if "www." in url:
        top_level = url.split('www.')[-1]
    return top_level.split('.')[0]

assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("https://youtube.com") == "youtube"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("http://github.com/carbonfive/raygun")
assert domain_name("http://www.zombie-bites.com")
assert domain_name("https://www.cnet.com")
