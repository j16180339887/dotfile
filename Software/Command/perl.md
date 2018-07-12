Args
=====
```conf
-C              UTF8
-Mutf8          UTF8
-i              Replace in place (current file)
-e              Regex
```

Replace all strings in a file
=====
```sh
perl -C -Mutf8 -pi -e 's/blue/red/g' ~/path/file
```

Remove all lines contains a string
=====
```sh
# case
perl -C -Mutf8 -ni -e 'print if !/mystring/' ~/path/file
# ignore case
perl -C -Mutf8 -ni -e 'print if !/mystring/i' ~/path/file
```