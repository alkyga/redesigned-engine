#!/usr/bin/env python3
# mostly just messing around with the os module

def main():
    home_dir = '/home/kg'
    output = f'''
get_dir_info(): {get_dir_info()}
get_dir_info(home_dir): {get_dir_info(home_dir)}
where_am_i: {where_am_i()}
get_my_proc_info: {get_my_proc_info()}
    '''
    print(output)

def where_am_i():
    import os
    return {'cwd': os.getcwd()}

def get_dir_info(dir=''):
    import os
    dir = os.getcwd() if dir == '' else dir
    dir_info = {}
    dir_info.update({'ls': os.listdir(dir)})
    return dir_info

def get_my_proc_info():
    import os
    proc_info = {}
    proc_info.update({'cwd': os.getcwd()})
    proc_info.update({'resuid': os.getresuid()})
    proc_info.update({'resgid': os.getresgid()})
    proc_info.update({'uname': os.uname()})
    return proc_info

if __name__ == "__main__":
    main()
