p7m2pdf
=======

Un banale one-liner Perl[1] per il prompt dei comandi di Windows che estrae al volo la copia PDF allegata a una fattura elettronica in formato SDI.

Aiuta a ricavare l'allegato sul proprio PC, senza bisogno di tool a pagamento o servizi on-line.

Ovviamente non verifica la validità della firma CAdES né del file XML della fattura.

Presuppone l'esistenza di un solo campo <Attachment> nel file, recante un valido contenuto codificato in Base64.



[1] Vedi https://www.perl.org/