import dtale
import pandas as pd
import webbrowser
import time

import dtale.global_state as global_state
global_state.set_app_settings(dict(enable_web_uploads=True))

print()
print('Starting D-Tale...')
print()

# Carregue seus dados
csv_file = r"titanic.csv"
df = pd.read_csv(csv_file)

# Inicie o D-Tale
d = dtale.show(df)

# Obtenha a URL do D-Tale
url = d._url

# Espere um pouco para garantir que o servidor D-Tale esteja pronto
time.sleep(2)

# Abra o navegador
webbrowser.open(url)

# Mantenha o script em execução
input("Pressione Enter para fechar o D-Tale...")
