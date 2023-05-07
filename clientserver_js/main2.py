import asyncio
import subprocess
import os

async def run_subprocess(cmd):
    proc = await asyncio.create_subprocess_shell(cmd)
    await proc.communicate()

async def main():
    current_path = os.path.dirname(os.path.realpath(__file__))
    venv_activate = os.path.join(current_path, "server_python", ".venv", "Scripts","activate.bat")
    server_path = os.path.join(current_path, "server_python", "server.py")
    frontend_path = os.path.join(current_path, "client")
    listener_path = os.path.join(current_path, "server_python", "listener.py")

    commands = [
        f"{venv_activate} && python {server_path}",
        f"cd {frontend_path} && npm start",
        f"{venv_activate} && python {listener_path}",
    ]
    tasks = []
    for cmd in commands:
        task = asyncio.ensure_future(run_subprocess(cmd))
        tasks.append(task)
    await asyncio.gather(*tasks)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())