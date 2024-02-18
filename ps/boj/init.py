import os
import sys
import requests

from bs4 import BeautifulSoup as bs


def main():
    # <NO>/<NO>.py
    no = int(sys.argv[1])
    os.mkdir(str(no))
    with open('template.py', 'r') as f:
        template = f.readlines()
        with open(f'{no}/{no}.py', 'w') as g:
            template[2] = f'# No. {no}\n'
            template[10] = '\n'
            template[13] = '\n'
            template[16] = '\n'
            g.writelines(template)

    # 예제_입력_<CNT>.txt
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.9',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Dest': 'document',
        'Host': 'www.acmicpc.net',
        'Referer': 'https://www.acmicpc.net/',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
    }

    response = requests.get(f'https://www.acmicpc.net/problem/{no}', headers=headers)
    soup = bs(response.text, 'html.parser')

    cnt = 0
    while True:
        cnt += 1
        sample_input = soup.find('pre', id=f'sample-input-{cnt}')
        if sample_input is None:
            break

        with open(f'{no}/예제_입력_{cnt}.txt', 'w') as h:
            h.write(sample_input.text)


if __name__ == '__main__':
    main()
