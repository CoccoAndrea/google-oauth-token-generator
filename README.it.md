
# 🔐 Google Oauth Token Generator
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue) ![License](https://img.shields.io/github/license/CoccoAndrea/google-oauth-token-generator) ![Last Commit](https://img.shields.io/github/last-commit/CoccoAndrea/google-oauth-token-generator) ![Issues](https://img.shields.io/github/issues/CoccoAndrea/google-oauth-token-generator) ![Stars](https://img.shields.io/github/stars/CoccoAndrea/google-oauth-token-generator?style=social)


Questo progetto Python serve a generare un **token di accesso OAuth 2.0** da utilizzare in altri script che comunicano con le **API di Google**, come Gmail e Google Drive.

---

## ✅ Funzionalità

- Effettua l'autenticazione OAuth 2.0 tramite browser
- Salva il token nel file `token.json`
- Invia un'email di test tramite Gmail API
- Carica un file di testo su Google Drive (nella cartella "TestFolder")
- Elimina il file di test da Google Drive

---

## 📦 Requisiti

- Python 3.7 o superiore
- Un progetto Google Cloud con Gmail API e Drive API abilitate
- Un file `credentials.json` ottenuto da Google Cloud Console


---
## ☁️ Come creare un progetto Google Cloud con Gmail e Drive API abilitate

1. Vai su [Google Cloud Console](https://console.cloud.google.com/).
2. Clicca su **Seleziona progetto** > **Nuovo progetto**.
3. Dai un nome al progetto e crealo.
4. Nel menu a sinistra, vai su **API e servizi** > **Libreria**.
5. Cerca e abilita le seguenti API:
   - **Gmail API**
   - **Google Drive API**
6. Vai su **Credenziali** > **Crea credenziali** > **ID client OAuth**.
7. Se richiesto, configura la schermata di consenso (nome app, email, ecc.).
8. Scegli **Applicazione desktop** come tipo di applicazione.
9. Scarica il file `credentials.json` e salvalo nella root del tuo progetto.
---

## 🔧 Installazione

1. **Clona il repository:**

```bash
git clone https://github.com/CoccoAndrea/google-oauth-token-generator.git
cd nome-repo
```

2. **Installa le dipendenze:**

```bash
pip install -r requirements.txt
```

3. **Inserisci le credenziali:**

Assicurati di avere il file `credentials.json` (ottenuto da [Google Cloud Console](https://console.cloud.google.com/apis/credentials)) nella root del progetto.

---

## ▶️ Come si usa

Esegui lo script principale:

```bash
python main.py
```

Il programma:

1. Ti guiderà nel login al tuo account Google (la prima volta).
2. Genererà e salverà il token in `token.json`, pronto per essere usato da altri script.
3. (Opzionale) Eseguirà una serie di test: invio email, caricamento file, e rimozione.

---

## 🔐 Autenticazione

La prima esecuzione aprirà una finestra del browser per autorizzare l'accesso al tuo account Google. Il token verrà salvato nel file `token.json`.

---

## 📬 Modifica l'indirizzo email di test

Nel file `main.py`, modifica la variabile `TEST_EMAIL`:

```python
TEST_EMAIL = "youremail@example.com"
```

---

## 📄 Licenza

Questo progetto è distribuito sotto licenza **MIT**.
