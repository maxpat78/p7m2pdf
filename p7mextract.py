import re, sys, binascii, subprocess

res = subprocess.run('openssl.exe smime -decrypt -verify -inform DER -in %s -noverify' % sys.argv[1], stdout=subprocess.PIPE)
s = res.stdout
#~ open('filtered.xml','wb').write(s)

se = re.search(b'<Attachment>(.+)</Attachment>', s, re.M|re.S).group(1)
print ('Base64 encoded input: %d bytes' % len(se))

try:
    sd = binascii.a2b_base64(se)
except binascii.Error:
    bad = set()
    n=0
    for c in se:
        if (c !=43 and (c < 47 or c > 122))  or (c > 90 and c < 97):
            bad.add(c)
            n+=1
    print("%d bad Base64 symbols detected: %s" % (n,bad))
    for c in bad:
        se = se.replace(c.to_bytes(1,'little'), b'')
    try:
        sd = binascii.a2b_base64(se)
    except:
        print ("Could not decode Base64 after stripping bad symbols:", sys.exc_info()[1])
        open('encoded.b64','wb').write(se)
        sys.exit(1)
    print ("Note: Base64 decode succeded after stripping bad symbols.")
    
open(sys.argv[1][:-7]+'pdf', 'wb').write(sd)
