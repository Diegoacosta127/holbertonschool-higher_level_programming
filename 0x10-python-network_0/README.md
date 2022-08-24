# 0x10. Python - Network #0
## Requirements
### General
* Allowed editors: `vi`, `vim`, `emacs`
* A `README.md` file, at the root of the folder of the project, is mandatory
* All your scripts will be tested on Ubuntu 20.04 LTS
* All your Bash scripts should be exactly 3 lines long (`wc -l file` should print 3)
* All your files should end with a new line
* All your files must be executable
* The first line of all your bash files should be exactly `#!/bin/bash`
* The second line of all your Bash scripts should be a comment explaining what is the script doing
* All `curl` commands must have the option `-s` (silent mode)
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3` (version 3.8.5)
* The first line of all your Python files should be exactly `#!/usr/bin/python3`
* Your code should use the pycodestyle (version `2.8.*`)
* All your modules should be documented: `python3 -c 'print(__import__("my_module").__doc__)'`
* All your classes should be documented: `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`
* All your functions (inside and outside a class) should be documented: `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
## Tasks
### 0. cURL body size
Write a Bash script that takes in a URL, sends a request to that URL, and displays the size of the body of the response
* The size must be displayed in bytes
* You have to use `curl`
Please test your script in the sandbox provided, using the web server running on port 5000
~~~~
guillaume@ubuntu:~/0x10$ ./0-body_size.sh 0.0.0.0:5000
10
guillaume@ubuntu:~/0x10$ 
~~~~
### 1. cURL to the end
Write a Bash script that takes in a URL, sends a `GET` request to the URL, and displays the body of the response
* Display only body of a `200` status code response
* You have to use `curl`
Please test your script in the sandbox provided, using the web server running on port 5000
~~~~
guillaume@ubuntu:~/0x10$ ./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
guillaume@ubuntu:~/0x10$ 
~~~~
### 2. cURL Method
Write a Bash script that sends a `DELETE` request to the URL passed as the first argument and displays the body of the response
* You have to use `curl`
Please test your script in the sandbox provided, using the web server running on port 5000
~~~~
guillaume@ubuntu:~/0x10$ ./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
guillaume@ubuntu:~/0x10$
~~~~
### 3. cURL only methods
Write a Bash script that takes in a URL and displays all HTTP methods the server will accept.
* You have to use `curl`
Please test your script in the sandbox provided, using the web server running on port 5000
~~~~
guillaume@ubuntu:~/0x10$ ./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
guillaume@ubuntu:~/0x10$ 
~~~~
### 4. cURL headers
Write a Bash script that takes in a URL as an argument, sends a `GET` request to the URL, and displays the body of the response
* A header variable `X-HolbertonSchool-User-Id` must be sent with the value `98`
* You have to use `curl`
Please test your script in the sandbox provided, using the web server running on port 5000
~~~~
guillaume@ubuntu:~/0x10$ ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello Holberton School!
guillaume@ubuntu:~/0x10$ 
~~~~
### 5. cURL POST parameters
Write a Bash script that takes in a URL, sends a `POST` request to the passed URL, and displays the body of the response
* A variable `email` must be sent with the value `test@gmail.com`
* A variable `subject` must be sent with the value `I will always be here for PLD`
* You have to use `curl`
Please test your script in the sandbox provided, using the web server running on port 5000
~~~~
guillaume@ubuntu:~/0x10$ ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
    email: test@gmail.com
    subject: I will always be here for PLD
guillaume@ubuntu:~/0x10$ 
~~~~
### 6. Only status code
Write a Bash script that sends a request to a URL passed as an argument, and displays only the status code of the response.
* You are not allowed to use any pipe, redirection, etc.
* You are not allowed to use `;` and `&&`
* You have to use `curl`
Please test your script in the sandbox provided, using the web server running on port 5000
~~~~
guillaume@ubuntu:~/0x10$ ./100-status_code.sh 0.0.0.0:5000 ; echo ""
200
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ ./100-status_code.sh 0.0.0.0:5000/nop ; echo ""
404
guillaume@ubuntu:~/0x10$
~~~~
### 7. cURL a JSON file
Write a Bash script that sends a JSON `POST` request to a URL passed as the first argument, and displays the body of the response.
* Your script must send a `POST` request with the contents of a file, passed with the filename as the second argument of the script, in the body of the request
* You have to use `curl`
Please test your scripts in the sandbox provided, using the web server running on port 5000
~~~~
guillaume@ubuntu:~/0x10$ cat my_json_0
{
    "name": "John Doe",
    "age": 33
}
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_0 ; echo ""
Valid JSON
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ cat my_json_1
I'm a JSON! really!
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_1 ; echo ""
Not a valid JSON
guillaume@ubuntu:~/0x10$ 
guillaume@ubuntu:~/0x10$ cat my_json_2
{
    "name": "John Doe",
    "age": 33,
}
guillaume@ubuntu:~/0x10$ ./101-post_json.sh 0.0.0.0:5000/route_json my_json_2 ; echo ""
Not a valid JSON
guillaume@ubuntu:~/0x10$
~~~~