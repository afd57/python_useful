import asyncio
from datetime import datetime

async def run(cmd):
    proc = await asyncio.create_subprocess_shell(
        cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
   
    while True:
        data = await proc.stdout.readline()
        print(str(datetime.now()), data.decode('utf-8'))
    # stdout, stderr = await proc.communicate()

    #print(f'[{cmd!r} exited with {proc.returncode}]')
    #if stdout:
    #    print(f'[stdout]\n{stdout.decode()}')
    #if stderr:
    #    print(f'[stderr]\n{stderr.decode()}')

asyncio.run(run('./long_process.sh'))
