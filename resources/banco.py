import sqlite3

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY, nome text, estrelas real, diaria real, cidade text)"

cursor.execute(cria_tabela)

conexao.commit()
conexao.close()