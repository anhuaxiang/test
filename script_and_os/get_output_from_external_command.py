import subprocess


out_bytes = subprocess.check_output(['netstat', '-a'])
print(out_bytes)
out_text = out_bytes.decode('utf-8')
print(out_text)


# exception
try:
    out_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'])
except subprocess.CalledProcessError as e:
    out_bytes = e.output
    code = e.returncode

# stdout error
out_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'], stderr=subprocess.STDOUT)

# timeout
try:
    out_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'], timeout=5)
except subprocess.TimeoutExpired as e:
    ...  # =pass
