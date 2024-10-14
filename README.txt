# PDF to Image Converter

Questo script Python converte tutte le pagine di un file PDF in immagini ad alta risoluzione (formato PNG).

## Prerequisiti

Assicurati di avere installato Python (versione 3.6 o successiva) e le seguenti librerie:

- **pdf2image**: per la conversione delle pagine del PDF in immagini.
- **Poppler**: necessario per il funzionamento di pdf2image.


### Installazione delle librerie

	#pdf2image

		Puoi installare `pdf2image` utilizzando `pip`. Apri il prompt dei comandi e digita:
											pip install pdf2image

	#Poppler 

		per installare Poppler puoi passare da github e scaricare l'ultima versione: https://github.com/oschwartz10612/poppler-windows/releases

		Estrai il file zip e annota il percorso della cartella `bin`.
		Aggiungi il percorso della cartella `bin` alla variabile d'ambiente PATH di sistema.

###Uso dello Script

Apri il file pdf2imageTool.py e modifica il percorso del file PDF nella variabile pdf_path
Esegui lo script nel prompt dei comandi: 
				python pdf2imageTool.py

Dopo l'esecuzione, le immagini delle pagine del PDF verranno salvate nella stessa directory dello script. 
Riceverai un messaggio che indica il numero di immagini salvate.


###Licenza
Questo progetto è open source e disponibile sotto la licenza MIT.