REM Estrae e decodifica il PDF allegato a una fattura elettronica in formato SDI
perl -MMIME::Base64 -e "$n=q(%1);$n=~s/xml.p7m/pdf/i;open(my $f,'>>',$n);binmode $f;for(`openssl smime -decrypt -verify -inform DER -in %1 -noverify`) {print $f decode_base64($1) if /<Attachment>(.+)<\/Attachment>/}"

