from tkinter import *


pessoa = {
    "PRIMEIRAS INFORMAÇÕES": {
        "TITULO": "NOME",
        "NOME": None,
        "ENDEREÇO": {
            "LOGRADOURO": None,
            "NOME DO LOGRADOURO": None,
            "NÚMERO": None,
            "COMPLEMENTO": None,
            "BAIRRO": None,
            "CEP": None
            },
        "TELEFONES": [],
        "EMAILS": []
        },
    
    "DADOS PESSOAIS": {
        "TITULO": "DADOS PESSOAIS",
        "DATA DE NASCIMENTO": None,
        "NATURALIDADE": None,
        "NASCIONALIDADE": None,
        "ESTADO CIVIL": None,
        "HABILITAÇÂO": None
        },
    
    "FORMACÂO": {
        "TITULO": "FORMACÂO",
        "GRAU": None,
        "STATUS": None
        },
    
    "CURSOS": {
        "TITULO": "CURSOS",
        "NOME": None,
        "LOCAL": None,
        "STATUS": None
        },

    "EXPERIÊNCIAS PROFISSIONAIS": {
        "TITULO": "EXPERIÊNCIAS PROFISSIONAIS",
        "EMPREGO1": {
            "EMPRESA": None,
            "FUNÇÂO": None,
            "PERÌODO": None
            },
        "EMPREGO2": {
            "EMPRESA": None,
            "FUNÇÂO": None,
            "PERÌODO": None
            },
        "EMPREGO2": {
            "EMPRESA": None,
            "FUNÇÂO": None,
            "PERÌODO": None
            }
        },
    
    "EXPERIÊNCIAS PROFISSIONAIS SEM REGISTRO": {
        "TITULO": "EXPERIÊNCIAS PROFISSIONAIS SEM REGISTRO",
        "EMPREGO1": {
            "EMPRESA": None,
            "FUNÇÂO": None,
            "PERÌODO": None
            },
        "EMPREGO2": {
            "EMPRESA": None,
            "FUNÇÂO": None,
            "PERÌODO": None
            },
        "EMPREGO2": {
            "EMPRESA": None,
            "FUNÇÂO": None,
            "PERÌODO": None
            }
        },

    "OBJETIVO": {
        "TITULO": "OBJETIVO",
        "TEXTO": None
        },

    "INFORMAÇÔES COMPLEMENTARES": {
        "TITULO": "INFORMAÇÔES COMPLEMENTARES",
        "TEXTO": None
        },

    "PERFIL":{
        "TITULO": "INFORMAÇÔES COMPLEMENTARES",
        "TEXTO": None
        }
    }


OEDEM_DAS_CAIXAS_NA_TELA = []


class Caixa_de_dados:

    def __init__(self, row, window):

        self.row = row
        self.window = window

        self.PADX = 2
        self.PADY = 2

        
    def main(self):
        self.frames()
        
        self.botao_subir()
        self.botao_descer()

        self.botao_editar_titulo()
        self.titulo()
        self.botao_deletar()


    def frames(self):
        self.main_fr = Frame(self.window)
        self.main_fr.grid(row=self.row, column=0)

        self.fr_botoes_subir_descer = Frame(self.main_frame)
        self.fr_botoes_subir_descer.pack(side=LEFT)
        
        self.fr_entrada_de_dados = Frame(self.main_frame)
        self.fr_entrada_de_dados.pack(side=RIGHT)

        self.fr_titulo = Frame(fr_entrada_de_dados)
        self.fr_titulo.grid(row=0, column=0)


    def titulo(self):
        self.ent_titulo = Entry(self.fr_titulo)
        self.ent_titulo.pack(side=LEFT)


    def botao_editar_titulo(self):
        self.bt_editar_titulo = Button(self.fr_titulo, text="E", command=self.func_do_botao_editar_titulo)
        self.bt_editar_titulo.pack(side=LEFT)


    def func_do_botao_editar_titulo(self):
        if self.bt_editar_titulo["state"] == "disabled":
            self.bt_editar_titulo["state"] = "normal"
        else:
            self.bt_editar_titulo["state"] = "disabled"


    def botao_deletar(self):
        self.bt_deletar = Button(self.fr_titulo, text="X", bg="red", command=self.main_fr.destroy)
        self.bt_deletar.pack(side=RIGHT)


    def botao_subir(self):
        self.bt_subir = Button(self.fr_botoes_subir_descer, text=" /\ ", height=5)
        self.bt_subir.pack()


    def botao_descer(self):
        self.bt_descer = Button(self.fr_botoes_subir_descer, text=" \/ ", height=5)
        self.bt_descer.pack()


    def botao_limpar(self):
        pass

    
    def _get(self):
        pass


    def _set(self):
        pass



class Primeiras_info(Caixa_de_dados):

    def __init__(self, row, window):

        super().__init__(row, window)

        self.main()


    def main(self):

        super().main()
        
        self.titulo()
        self.nome()
        self.endereco()
        self.telefone()
        self.email()


    def frames(self):
        super().frames()


    def _get(self):
        pass

 
   def _set(self, titulo, nome, endereco, telefone, email):
        pass


    def titulo(self):
        self.fr1 = Frame(self.fr_entrada_de_dados)
        self.fr1.grid(row=0, column=0, sticky="w")

        self.cx_titulo = Entry(self.fr1)
        self.cx_titulo.pack(side=LEFT, padx=self.PADX, pady=self.PADY)

        self.cx_titulo.insert(0, "Primeiras Informações")
        self.cx_titulo.config(state="disabled")
        


    def botao_editar_titulo(self):
        pass


    def botao_deletar(self):
        self.bt_deletar = Button(self.fr1, command=self.main_fr.destroy)
        self.bt_deletar.pack(side=RIGHT, padx=self=self.PADX, pady=self.PADY)


    def nome(self):
        self.fr2 = Frame(self.fr_entrada_de_dados)
        self.fr2.grid(row=1, column=0, sticky="w")


    def endereco(self):
        pass


    def telefone(self):
        pass


    def email(self):
        pass




class Dados_pessoais(Caixa_de_dados):

    def __init__(self, row, frame_botoes_subir_descer, frame_entrada_de_dados, window):
        pass
    

    def main(self):
        pass


    def _get(self):
        pass


    def _set(self):
        pass



class Escolaridade(Caixa_de_dados):

    def __init__(self, row, frame_botoes_subir_descer, frame_entrada_de_dados, window):
        pass
    

    def main(self):
        pass


    def _get(self):
        pass


    def _set(self):
        pass



class Cursos(Caixa_de_dados):

    def __init__(self, row, frame_botoes_subir_descer, frame_entrada_de_dados, window):
        pass
    

    def main(self):
        pass


    def _get(self):
        pass


    def _set(self):
        pass



class Experiencias_profissionais(Caixa_de_dados):

    def __init__(self, row, frame_botoes_subir_descer, frame_entrada_de_dados, window):
        pass
    

    def main(self):
        pass


    def _get(self):
        pass


    def _set(self):
        pass



class Experiencias_profissionais_sem_registro(Caixa_de_dados):

    def __init__(self, row, frame_botoes_subir_descer, frame_entrada_de_dados, window):
        pass
    

    def main(self):
        pass


    def _get(self):
        pass


    def _set(self):
        pass



class Objetivo(Caixa_de_dados):
    
    def __init__(self, row, frame_botoes_subir_descer, frame_entrada_de_dados, window):
        pass
    

    def main(self):
        pass


    def _get(self):
        pass


    def _set(self):
        pass



class Info_complementares(caixa_de_dados):
    
    def __init__(self, row, frame_botoes_subir_descer, frame_entrada_de_dados, window):
        pass
    

    def main(self):
        pass


    def _get(self):
        pass


    def _set(self):
        pass



class Perfil(Caixa_de_dados):
    
    def __init__(self, row, frame_botoes_subir_descer, frame_entrada_de_dados, window):
        pass
    

    def main(self):
        pass


    def _get(self):
        pass


    def _set(self):
        pass



class Caixa_generica(Caixa_de_dados):
    
    def __init__(self, row, frame_botoes_subir_descer, frame_entrada_de_dados, window):
        pass
    

    def main(self):
        pass


    def _get(self):
        pass


    def _set(self):
        pass
