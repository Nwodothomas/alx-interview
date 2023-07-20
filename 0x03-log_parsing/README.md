Solution to the Task for 0x03. Log Parsing
# Log Parsing Script - README

This repository contains a Python script that reads logs in a specific format from standard input (stdin) and computes metrics based on the input.

## Requirements

### General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable
- The length of your files will be tested using `wc`

## Tasks

### Task 0: Log Parsing

**File**: `0-stats.py`

**Description**: Write a script that reads `stdin` line by line and computes metrics based on the input. The input should follow the format:

<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>


The script should perform the following tasks:

1. After every 10 lines and/or a keyboard interruption (CTRL + C), it should print the following statistics from the beginning:
   - Total file size: `<total size>` (where `<total size>` is the sum of all previous `<file size>`)
   - Number of lines by status code:
     - Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500
     - If a status code doesn’t appear or is not an integer, don’t print anything for this status code
     - Format: `<status code>: <number>`
     - Status codes should be printed in ascending order

**Input Example**:

```bash
$ ./0-generator.py | ./0-stats.py

###
### Output

File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3

File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3

File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4

^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4

Traceback (most recent call last):
  File "./0-stats.py", line 15, in <module>
    for line in sys.stdin:
KeyboardInterrupt

## Repository Information

- GitHub repository: [alx-interview](https://github.com/username/alx-interview)
- Directory: 0x03-log_parsing
- File: `0-stats.py`
