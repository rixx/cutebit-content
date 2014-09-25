Title: CSAW 2014 Writeup: pybabbies
Date:   2014-09-19
Category: writeups
Tags: ctf,writeups,csaw,exploitation
Slug: csaw14
Status: Draft
Authors: rixx
Summary: Writeup of the pybabbies task at the recent CSAW14. Category: Exploitation. Points: 200. Team: krebs.

At the recent [CSAW14](https://ctf.isis.poly.edu/challenges#) I participated with the [krebs](http://krebsco.de/writeups/index.html) team. Sadly, I had only little time for the CTF, but I managed to complete one task nonetheless. It was called **pybabbies**, belonged to the category **Exploitation** and yielded **200** points (on a scale from 100 to 500).

## The Task

We were to connect to `54.165.210.171 12345` where we were greeted by a Python shell. Thankfully the code for this shell was included in the task:


    #!/usr/bin/env python 
    
    from __future__ import print_function
    
    print("Welcome to my Python sandbox! Enter commands below!")
    
    banned = [
        "import",
        "exec",
        "eval",
        "pickle",
        "os",
        "subprocess",
        "kevin sucks",
        "input",
        "banned",
        "cry sum more",
        "sys"
    ]
    
    targets = __builtins__.__dict__.keys()
    targets.remove('raw_input')
    targets.remove('print')
    for x in targets:
        del __builtins__.__dict__[x]
    
    while 1:
        print(">>>", end=' ')
        data = raw_input()
    
        for no in banned:
            if no.lower() in data.lower():
                print("No bueno")
                break
        else: # this means nobreak
            exec data

As you can see, this is a Python2 script. What it does is essentially the following:

* It removes all builtin functions and variables except for `raw_input` and `print`. This means we can't use any implicitly or explicitly used builtins such as `len` (which is commonly implicitly used in existental statements).
* It starts a REPL loop.
* It executes every (one-line) command we enter … except if it contains a banned word. Such as … `import`. Or `sys`. Or `os`. Or `eval` or `exec` or `input`. Basically everything we would want to escape the sandbox and find the keyfile.


