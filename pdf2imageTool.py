from pdf2image import convert_from_path

# recupera il percorso al PDF
pdf_path = 'C:/Users/Giovanni/Downloads/parziale1editato/FABBRIPARZIALE1.pdf' # metti il percorso e il nome in coda del pdf che vuoi elaborare

# converte il PDF in immagini (alta risoluzione con >600 dpi)
images = convert_from_path(pdf_path, dpi=900) # risoluzione in dpi, conviene 900 nella maggior parte dei casi, c'e` un sistema di sicurezza per evitare che i file diventino troppo grandi e scoppi il computer

# loop che salva ogni pagina come immagine
for i, image in enumerate(images):
    image.save(f'pagina_{i + 1}.png', 'PNG') # volendo puoi cambiare il formato di immagine che vuoi in uscita ma il formato PNG e' consigliato in quanto comtemporaneamente lossless ed universale

# messaggio di conferma
num_images = len(images)
if num_images > 0:
    print(f"Conversione andata a termine! {num_images} immagini salvate nella cartella scriptPDFtoPNG che si trova al percorso C:/Users/Giovanni/Desktop/scriptPDFtoPNG.")
else:
    print("errore, nessuna immagine salvata. Controlla il file pdf, se il pdf non ha problemi allora lo script e' andato a puttane porco dio, trovi lo script al percorso C:/Users/Giovanni/Desktop/scriptPDFtoPNG/pdf2imageTool.py.")