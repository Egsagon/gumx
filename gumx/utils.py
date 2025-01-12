import typing
import requests
import subprocess

from . import consts


def get(url: str, **kw) -> requests.Response:
    '''
    GET request wrapper.
    '''
    
    response = requests.get(url, **kw)
    response.raise_for_status()
    return response

def download(url: str, path: str, chunk_size = 8192) -> None:
    '''
    Download a large file.
    '''
    
    with get(url, stream = True) as stream, open(path, 'wb') as file:
        for chunk in stream.iter_content(chunk_size):
            file.write(chunk)

def dump(obj: typing.Any) -> str:
    '''
    Dump a single value into string.
    '''
    
    if obj == True:                   return ''
    if isinstance(obj, dict):         obj = [f'{k} - {v}' for k, v in obj.items()]
    if isinstance(obj, tuple | list): return ' '.join(map(dump, obj))
    if isinstance(obj, str):          return obj
    
    return repr(obj)

def flatten(obj: dict, t: dict = None, r: str = '') -> dict[str]:
    '''
    Flatten a style dict.
    '''
    
    track = t or {}
    
    for k in obj:
        if isinstance(obj[k], dict):
            flatten(obj[k], track, r + k + '.')
        
        else:
            track[r + k] = dump(obj[k])
    
    return track

def dump_args(func: typing.Callable, args: dict[str, typing.Any]) -> list[str]:
    '''
    Dump arguments into a shell command.
    '''
    
    t = func.__annotations__
    
    # Construct args chain
    output = []
    for arg, value in args.items():
        if value in (None, False) or arg == 'style': continue
        
        trailer = ('', f'--{arg} ')['Optional' in str(t[arg])]
        output.append((trailer + dump(value)).strip())
    
    for arg, value in flatten(args.get('style', {})).items():
        output.append(f'--{arg} {value}')
    
    return output

def run(func: typing.Callable, args: dict[str, typing.Any]) -> subprocess.CompletedProcess:
    '''
    Run a GUM command.
    '''
    
    cmd = [consts.INSTALL, func.__name__] + dump_args(func, args)
    
    print('[EXEC]', cmd)
    
    return subprocess.run(args = ' '.join(cmd), stdout = subprocess.PIPE)

# EOF