import requests

api_url = 'http://numbersapi.com/{0}/math?json=true'

with open('in.txt') as in_f:
    with open('out.txt', 'w') as out_f:
        for line in in_f:
            number = int(line)
            api = api_url.format(number)
            print(api)
            res = requests.get(api)
            data = res.json()
            print(number,':', data['found'])
            if not data['found']:
                out_f.write('Boring\n')
            else:
                out_f.write('Interesting\n')