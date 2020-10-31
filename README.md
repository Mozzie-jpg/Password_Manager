# Shit Password Manager

I recommend creating a virtualenv before building

so something like this:
```
python3 -m venv pass_venv
source pass_venv/bin/activate
bash build_script.sh
```
if the build scripts dont work, it might be because you might need to use it through "python3 -m" instead

You must also have a C compiler installed

For example gcc

For the first time creating a set, you need to manually delete the empty line in ~/.pass_man
