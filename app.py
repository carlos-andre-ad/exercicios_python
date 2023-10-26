
import sqlite3
import os

BD = "mundo.db"

def criar_db():
    if not os.path.exists(BD):
        try:
            conn = sqlite3.connect(BD)
            cursor = conn.cursor()
            cursor.execute("CREATE TABLE setemaravilhas (id INTEGER PRIMARY KEY AUTOINCREMENT, codigo TEXT, pais TEXT,cidade TEXT,descricao TEXT, nota REAL)")
            conn.close()
            return True
        except sqlite3.Error as e:
            print(f"Erro ao criar banco de dados: {e}") 
            return False
    else:
       return True 
    
    
def inserir(pais, cidade, descricao, nota, codigo):
    try:
        conn = sqlite3.connect(BD)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM setemaravilhas WHERE codigo=?", (codigo,))
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO setemaravilhas (pais, cidade, descricao, nota, codigo) VALUES (?, ?, ?, ?, ?)",
                           (pais, cidade, descricao, nota, codigo))
            conn.commit()
            print("Dados inseridos com sucesso!")
        else:
            print(f"O código {codigo} já existe na tabela.")
        conn.close()

    except sqlite3.Error as e:
        print(f"Erro ao inserir dados no banco de dados: {e}") 
        
        
def listar():
    try:
        conn = sqlite3.connect(BD)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM setemaravilhas")
        dados = cursor.fetchall()
        conn.close()
        resultados = []

        for registro in dados:
            resultado = {
                "ID": registro[0],
                "País": registro[1],
                "Cidade": registro[2],
                "Descrição": registro[3],
                "Nota": registro[4],
                "Código": registro[5]
            }
            resultados.append(resultado)

        return resultados

    except sqlite3.Error as e:
        print(f"Erro ao listar os dados da tabela: {e}")    
        
        
def alterar_nota(codigo, nova_nota):
    try:
        conn = sqlite3.connect(BD)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM setemaravilhas WHERE codigo=?", (codigo,))
        resultado = cursor.fetchone()

        if resultado:
            id_registro = resultado[0]
            cursor.execute("UPDATE setemaravilhas SET nota = ? WHERE id = ?", (nova_nota, id_registro))
            conn.commit()
            print("Nota alterada com sucesso")
        else:
            print(f"Registro com código {codigo} não encontrado na tabela.")
        conn.close()

    except sqlite3.Error as e:
        print(f"Erro ao alterar a nota na tabela: {e}")     
        
        
        
def excluir(codigo):
    try:
        conn = sqlite3.connect(BD)
        cursor = conn.cursor()
        cursor.execute("SELECT id FROM setemaravilhas WHERE codigo=?", (codigo,))
        resultado = cursor.fetchone()

        if resultado:
            id_registro = resultado[0]
            cursor.execute("DELETE FROM setemaravilhas WHERE id=?", (id_registro,))
            conn.commit()
            print(f"Registro com código {codigo} excluído com sucesso.")
        else:
            print(f"Registro com código {codigo} não encontrado na tabela.")
        conn.close()

    except sqlite3.Error as e:
        print(f"Erro ao excluir o registro da tabela: {e}")        
        
               

if __name__ == "__main__":
    if criar_db() == True:
        inserir("Brasil", "Rio de Janeiro", "Cristo Redentor", 9.5, "MR-01")
        inserir("Egito", "Cairo", "Pirâmides", 9, "MR-02")
        print(listar())
        alterar_nota("MR-01", 10)
        print(listar())
        excluir("MR-02")
