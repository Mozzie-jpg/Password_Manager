# Shit Password Manager

I recommend creating a virtualenv before building

so something like this:
```
python3 -m venv pass_venv
source pass_venv/bin/activate
```

For the first time creating a set, you need to manually delete the empty line in ~/.pass_man

you will also need to generate a key, you can generate one like so:
```
from cryptography.fernet import Fernet
key = Fernet.generate_key()
print (key)
```

then you will need to make a file at ~/.key

But remember you must remove the newline at the end of the file!
