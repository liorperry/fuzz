import asyncio


async def run_command_shell(command, timeout):
    """Run command in subprocess (shell)

    Note:
        This can be used if you wish to execute e.g. "copy"
        on Windows, which can only be executed in the shell.
    """
    # Create subprocess
    process = await asyncio.create_subprocess_shell(command, stdout=asyncio.subprocess.PIPE)

    try:
        await asyncio.wait_for(process, timeout)
    except asyncio.TimeoutError:
        print('timeout!')

    # Status
    print('Started:', command, '(pid = ' + str(process.pid) + ')')

    # Wait for the subprocess to finish
    stdout, stderr = await process.communicate()

    # Progress
    if process.returncode == 0:
        print('Done:', command, '(pid = ' + str(process.pid) + ')')
    else:
        print('Failed:', command, '(pid = ' + str(process.pid) + ')')

    # Result
    result = stdout.decode().strip()

    # Return stdout
    return result
