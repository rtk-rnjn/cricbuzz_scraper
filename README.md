# cricbuzz_scraper

> **⚠️ The Project is only for the educational purpose. I do not encourage the website abuse in any means by any kind.**

---

### How to get this shit working?

Clone the repo.
```bash
$ git clone https://github.com/rtk-rnjn/cricbuzz_scraper/
$ cd cricbuzz_scraper
```

Install the requirements
```bash
$ pip install -r requirements.txt
```

Run the script
```bash
$ python3 main.py
```

---


### Then?

On successful completion, you can make `get` request to `http://127.0.0.1:1729/cricket_api` to get the data.

```py
>>> import requests
>>> response = requests.get('http://127.0.0.1:1729/cricket_api?url=https://m.cricbuzz.com/cricket-commentary/45926/rr-vs-mi-9th-match-indian-premier-league-2022')
>>> data = response.json()
>>> print(data)
... {
...     'success': True, 
...     'title': 'Mumbai Indians vs Rajasthan Royals, 9th Match',
...     'status': 'Mumbai Indians need 170 runs',
...     'team_one': 'RR - 193/8 (20)', 'team_two': 'MI - 24/1 (3)',
...     'crr': ['CRR: \xa08.00', 'RR : \xa010.00'],
...     'extra': [
...         ['Partnership: ', '9(7)'],
...         ['Last wkt: ', 'Rohit Sharma c Riyan Parag b Prasidh 10(5) - 15/1 in 1.5 ov.'],
...         ['Recent balls: ', '... | 2 6 Wd 2 0 W 4 | 1 1 2 0 0 1']
...     ],
...     'batting': {
...         'Batting': ['Anmolpreet Singh', 'Ishan Kishan*'], 
...         'R(B)': ['5(2)', '8(11)'],
...         '4s': ['1', '1'],
...         '6s': ['0', '0'],
...         'SR': ['250', '72.73']
...     },
...     'bowling': {
...         'Bowling': ['Trent Boult', 'Prasidh Krishna*'],
...         'O': ['2', '1'],
...         'M': ['0', '0'],
...         'R': ['9', '15'],
...         'W': ['0', '1']
...     }
...     "commentry": [
...            "12.4 Boult to Ishan Kishan, 1 run, wider line, steered away through backward point
...             # ...
...     ]
... }
>>> 
```
> **Note:** May not get `batting` and `bowling` data if there is any website problem
