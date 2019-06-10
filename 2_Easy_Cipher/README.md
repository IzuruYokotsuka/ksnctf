#

Ebiil Tloia
を3文字進めて置換すると
Hello World
になる

```
$ echo "Ebiil Tloia" | sed -e 'y/abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ/defghijklmnopqrstuvwxyzabcDEFGHIJKLMNOPQRSTUVWXYZABC/'
Hello World

```

```

izuru@IzuruYokotsukanoMacBook-puro:~/workspace/private/ksnctf/#2_Easy_Cipher
$ python rot_n.py "EBG KVVV vf n fvzcyr yrggre fhofgvghgvba pvcure gung ercynprf n yrggre jvgu gur yrggre KVVV yrggref nsgre vg va gur nycunorg. EBG KVVV vf na rknzcyr bs gur Pnrfne pvcure, qrirybcrq va napvrag Ebzr. Synt vf SYNTFjmtkOWFNZdjkkNH. Vafreg na haqrefpber vzzrqvngryl nsgre SYNT." 13
ROT XIII is a simple letter substitution cipher that replaces a letter with the letter XIII letters after it in the alphabet. ROT XIII is an example of the Caesar cipher, developed in ancient Rome. Flag is FLAGSwzgxBJSAMqwxxAU. Insert an underscore immediately after FLAG.
```