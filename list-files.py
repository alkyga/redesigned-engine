#!/usr/bin/env python3
# mostly just messing around with the os module

def main():
    print('wow, nice to meet you, world')
    output = f'''
get_dir_info: {get_dir_info()}
where_am_i: {where_am_i()}
get_my_proc_info: {get_my_proc_info()}
    '''
    print(output)

def where_am_i():
    import os
    where = {}
    return where

def get_dir_info():
    import os
    dir_info = {}
    dir_info.update({'cwd': os.getcwd()})
    dir_info.update({'egid': os.getegid()})
    dir_info.update({'euid': os.geteuid()})
    dir_info.update({'uname': os.uname()})
    dir_info.update({'ls': os.listdir(dir_info['cwd'])})
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
