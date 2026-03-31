from urllib.parse import urlparse, urlunparse

url = "https://mail.google.com/mail/u/0/#label/Marca%C3%A7%C3%A3o+de+ponto/FMfcgzQgLFgmskfCzGrvwPpBVSwTrdvX"
parsed_url = urlparse(url)
clean_url = urlunparse((parsed_url.scheme, parsed_url.netloc, parsed_url.path, '', '', ''))
print(clean_url)