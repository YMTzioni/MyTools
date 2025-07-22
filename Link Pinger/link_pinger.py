import requests
import csv
import sys
import time
import os

INPUT_FILE = 'links.txt'  # Input file with URLs, one per line
OUTPUT_FILE = 'link_report.csv'
TIMEOUT = 5  # seconds
SLOW_THRESHOLD = 2  # seconds

def normalize_url(url):
    if url.startswith('http://') or url.startswith('https://'):
        return [url]
    # Try https first, then http as fallback
    return [f'https://{url}', f'http://{url}']

def check_link(url):
    urls_to_try = normalize_url(url)
    last_exception = None
    for u in urls_to_try:
        try:
            start = time.time()
            response = requests.get(u, timeout=TIMEOUT, allow_redirects=True)
            elapsed = time.time() - start
            if response.status_code == 200:
                if elapsed > SLOW_THRESHOLD:
                    return 'Alive (Slow)', response.status_code, elapsed, response.url
                return 'Alive', response.status_code, elapsed, response.url
            elif 300 <= response.status_code < 400:
                return 'Redirect', response.status_code, elapsed, response.headers.get('Location', response.url)
            else:
                return 'Dead', response.status_code, elapsed, response.url
        except requests.exceptions.RequestException as e:
            last_exception = e
            continue
    return 'Dead', None, None, str(last_exception)

def main():
    if not os.path.exists(INPUT_FILE):
        print(f'Input file {INPUT_FILE} not found.')
        sys.exit(1)
    with open(INPUT_FILE, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]
    results = []
    print(f'Checking {len(urls)} links...')
    for url in urls:
        status, code, elapsed, info = check_link(url)
        print(f'{url}: {status} (code={code}, time={elapsed}, info={info})')
        results.append({'url': url, 'status': status, 'code': code, 'time': elapsed, 'info': info})
    # Write to CSV
    with open(OUTPUT_FILE, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['url', 'status', 'code', 'time', 'info']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in results:
            writer.writerow(row)
    print(f'Results saved to {OUTPUT_FILE}')

if __name__ == '__main__':
    main() 