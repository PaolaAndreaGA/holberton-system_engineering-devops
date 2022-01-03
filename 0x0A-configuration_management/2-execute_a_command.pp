# 2. Execute a command

exec { 'pkill killmenow':
    path  =>  '/usr/bin',
}