# Crawler tester

## Dependencies 

Poetry:

```
pip3 install poetry
```

## Run

```sh
poetry install --no-root
poetry run gunicorn 'crawler_tester:create_app()'
```

## Available endpoints

| Endpoint | Role | Params
|-|-|-|
| `/` | Test page, should display an Hello World message ||
| `/status/<code>` | Return a sample page with the specified HTTP status code | `code`: any value from 200 to 205 |
| `/redirect/http-<code>` | Return an HTTP redirect header, leading to page /landing | `code`: any value from 300 to 308, except 304 |
| `/redirect/js-location-assign` | Return a page with a JS script using location.assign() to redirect to the _/landing_ page | |
| `/redirect/js-location-replace` | Return a page with a JS script using location.replace() to redirect to the _/landing_ page | |
| `/redirect/js-location-href` | Return a page with a JS script using location.href to redirect to the _/landing_ page | |
| `/redirect/js-meta-refresh` | Return a page with a META tag to redirect to the _/landing_ page | `delay`: delay in milliseconds before redirection |
| `/redirect/js-obfuscated-location-assign` | Return a page with a JS script redirecting to the _/landing_ page after the _onload_ event is triggered | `delay`: delay in milliseconds before redirection |
| `/redirect-chain/<number>` | Return <number> times using HTTP headers, eventually leading to page /landing | `number`: how many redirects will be performed in total |
| `/delay/page` | Return a valid HTML page after a given delay | `delay`: delay in milliseconds before the response is sent |
| `/delay/contents` | Return a valid HTML page containing _count + 1_ images, some of them being returned after the specified delay | `delay`: delay in milliseconds before the images are sent<br>`count`: number of image to load in the page |
