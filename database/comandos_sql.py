#   Biblioteca do sqlite
import  sqlite3  as sql;

#........................................
#                                       |
#       BIBLIOTECA DOS COMANDOS SQL     |
#                                       |
#.......................................'

#   Criado em:  06/07/2020 21:05
#   Biblioteca utilizada para realizar comandos SQL dentro do projeto Meridia.

#...................................
#       Manipulação tabela logins  |
#..................................'
#
#   Testes:
#   - Todas as rotinas estão funcionando perfeitamente dentro de seu escopo
#   Melhorias:
#   - Criar tratamento de condicionais caso alguma resulte em erro

#   Rotina utilizada para dar begin, execute e commit em uma consulta SQL
def ExecutaSQL(__sql, insert=None):
    with sql.connect('database.db') as __conn:
        __cur = __conn.cursor();
        __cur.execute('begin');
        if insert == None:
            __cur.execute(__sql);
        else:
            __cur.execute(__sql, insert)
        __cur.execute('commit');
    return True;

#...................................
#       Manipulação tabela logins  |
#..................................'

#   Cria a tabela de logins
#       Rotina que cria tabela que armazena os logins com login e senha como texto
def CriaTabelaLogins():
    sql = """
    CREATE TABLE logins(
        login           TEXT PRIMARY KEY,
        SENHA           TEXT NOT NULL
    )
    """;
    ExecutaSQL(sql);
    return True;

#   Deleta tabela de logins
#       Rotina que deleta a tabela que armazena os logins
def DeletaTabelaLogins():
    sql = """
    DROP TABLE logins
    """;
    ExecutaSQL(sql);
    
    return True;

#   Responsável por realizar cadastros na tabela de logins
#       Create
def CadastraLogin(login, senha):
    sql = """
    INSERT INTO logins(login, senha) VALUES (?, ?)
    """
    ExecutaSQL(sql, (login, senha));

    return True;

#   Responsável por realizar leitura e retornar o resultado da consulta
#       Read
def LeLogin(login="", senha=""):
    if login=="":
        __sql = """
        SELECT * FROM logins
        """;

    elif login !="" and senha !="":
        __sql = f"""
        SELECT * FROM logins WHERE login = '{login}' and senha = '{senha}'
        """;

    with sql.connect('database.db') as __conn:
        __cur = __conn.cursor();

    return __cur.execute(__sql).fetchall();

#   Responsável por alterações na tabela de logins
#       Update
def AtualizaLogin(login, senha_antiga, senha_nova):
    sql = f"""
    UPDATE logins SET senha = '{senha_nova}' WHERE login = '{login}' and senha = '{senha_antiga}'
    """;
    ExecutaSQL(sql);

    return True;

#   Responsável por deletar dados na tabela de logins
#       Delete
def DeletaLogin(login, senha, tudo=0):
    if tudo == 0:
        sql = f"""
        DELETE FROM logins WHERE login = '{login}' and senha = '{senha}'
        """;
    elif tudo == 1:
        sql = f"""
        DELETE FROM logins
        """;
    ExecutaSQL(sql);