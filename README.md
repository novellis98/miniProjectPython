# MiniProjectPython – Web App con Flask per Form di Contatto

Questo progetto è una semplice applicazione web realizzata con **Flask**, che consente la navigazione tra diverse pagine e la gestione di un **form di contatto**. I dati inviati tramite il form vengono salvati in un file CSV locale grazie al backend sviluppato in Python.

> ⚠️ **Nota bene**: Tutti i template HTML utilizzati in questo progetto sono stati **presi da [Orson.io](https://www.orson.io)** e appartengono alla collezione "Mashup templates" sviluppata dal team di Orson. Il **frontend non è stato realizzato da me**, in quanto il mio obiettivo era focalizzarmi esclusivamente sullo sviluppo backend con Python e Flask.

---

## 🚀 Funzionalità

- Navigazione tra più pagine statiche
- Form di contatto
- Gestione dell’invio del form con metodo `POST`
- Salvataggio dei dati in formato CSV tramite il modulo `csv` di Python
- Reindirizzamento alla pagina di ringraziamento dopo l’invio

---

## 🛠️ Tecnologie Utilizzate

- Python 3.x
- Flask (micro web framework)
- HTML/CSS (tramite template forniti da Orson.io)

---

## 🔧 Come Funziona

1. L’utente compila il form nella pagina `/contact`.
2. Al click su “Invia”, viene fatta una richiesta `POST` verso l’endpoint `/submit_form`.
3. Il backend raccoglie i dati del form, li converte in dizionario e li salva nel file `database.csv`.
4. Se tutto va a buon fine, l’utente viene reindirizzato alla pagina `/thankyou`.

---

### ✅ Obiettivo del progetto

Questo progetto è stato realizzato a scopo **didattico** per approfondire le basi dello sviluppo web con Flask e la gestione dei form in backend.
