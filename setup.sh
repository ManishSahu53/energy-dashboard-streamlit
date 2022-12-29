mkdir -p ~/.streamlit/
echo "[general]
email = \"email@com\"
" > ~/.streamlit/credentials.toml
echo "[server]
headless = true
port = $PORT
enableCORS = true
" > ~/.streamlit/config.toml