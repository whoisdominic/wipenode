# Wipenode

Python script that will remove all node modules using recursion

# Instructions (MAC)

To make the script callable from anywhere using the `wipenode` command, you can follow these steps:

1. Move the `wipenode.py` file to a directory that's in your system's `$PATH`. For instance, you can move it to `/usr/local/bin`:

```bash
cp wipenode.py /usr/local/bin
```

2. Create a new shell script named `wipenode` in the same directory (`/usr/local/bin`):

```bash
touch /usr/local/bin/wipenode
```

3. Open the `wipenode` file in a text editor and add the following content:

```bash
#!/bin/bash
python /usr/local/bin/wipenode.py "$@"
```

4. Save and close the `wipenode` file, and make it executable by running:

```bash
chmod +x /usr/local/bin/wipenode
```

Now you should be able to run the `wipenode` command from anywhere in your terminal. It will execute the Python script to remove `node_modules` directories.

Please note that you may need to use `sudo` to move the files and make them executable, depending on the permissions of the directory you choose.
