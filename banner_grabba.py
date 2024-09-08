# Banner Grabba v.1
# 20240606
#!/usr/bin/env python

import subprocess

def read_list(file_path, num_lines=20):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f.readlines()[:num_lines]]

def read_request(file_path):
    with open(file_path, 'r') as f:
        return f.read()

def run_ncat(host, request):
    try:
        result = subprocess.run(
            ['ncat', host, '80'],
            input=request.encode(),
            capture_output=True,
            text=True
        )
        return result.stdout + result.stderr
    except Exception as e:
        print(f"Error running ncat for {host}: {e}")
        return ''

def filter_and_write_results(output, search_term, result_file):
    with open(result_file, 'a') as f:
        for line in output.splitlines():
            if search_term.lower() in line.lower():
                f.write(line + '\n')

def main():
    hosts = read_list('list')
    request = read_request('request')
    result_file = 'Results'
    search_term = 'server'
    
    for host in hosts:
        print(f"Processing {host}")
        output = run_ncat(host, request)
        filter_and_write_results(output, search_term, result_file)
        print(f"Done with {host}")

if __name__ == '__main__':
    main()

