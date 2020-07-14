p7m2pdf
=======

Un *one-liner* Perl[1] per il prompt dei comandi di Windows che estrae al volo la copia PDF allegata a una fattura elettronica in formato SDI.

Aiuta a ricavare l'allegato sul proprio PC, senza bisogno di *tool* a pagamento o servizi *on-line*.

Presuppone la presenza sul PC di OpenSSL (usato per estrarre la fattura XML dalla busta P7M firmata digitalmente) e di Perl (usato per estrarre il campo `<Attachment>` dalla fattura XML e decodificarlo dal formato Base64).



[1] Vedi https://www.perl.org/
