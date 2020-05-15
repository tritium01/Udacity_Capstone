import http.client

conn = http.client.HTTPSConnection("rmgmex.auth0.com")

payload = "{\"client_id\":\"Tei3s19FOl3398SfCefQW6zmJM72l5hx\",\"client_secret\":\"x1NvTFxxwp5ak02Lh7y46Y1DRa1lNJQeTvZb4w9jLE_JdIZHVGhiKQKHvgI0pSvB\",\"audience\":\"capstone\",\"grant_type\":\"client_credentials\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))