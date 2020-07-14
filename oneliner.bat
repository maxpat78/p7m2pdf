REM Estrae e decodifica il PDF allegato a una fattura elettronica in formato SDI
perl -MMIME::Base64 -ne "print decode_base64($1) if /<Attachment>(.+)<\/Attachment>/" %1 >%~n1.pdf
