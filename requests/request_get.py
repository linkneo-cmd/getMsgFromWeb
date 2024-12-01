import requests

res = requests.get("https://automatetheboringstuff.com/files/rj.txt")
if(res.status_code == requests.codes.ok):
    print(res.text[:251])
    playFile = open('RomeoAndJuliet.txt', 'wb')
    for chunk in res.iter_content(100_000):
        playFile.write(chunk)
    playFile.close()
else:
    print(f"There was a problem: {res.status_code}")


res = requests.get("https://inventwithpython.com/page_that_does_not_exist")
try:
    res.raise_for_status()
except Exception as exc:
    print(f"There was a problem: {exc}")