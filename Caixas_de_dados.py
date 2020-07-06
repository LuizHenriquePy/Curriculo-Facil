from tkinter import *


pessoa = {
    "PRIMEIRAS INFORMAÇÕES": {
        "TITULO": "",
        "NOME": None,
        "ENDEREÇO": None,
        "TELEFONES": None,
        "EMAILS": None
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

        self.main_fr = Frame(self.window)
        self.main_fr.grid(row=self.row, column=0)

        self.fr_botoes_subir_descer = Frame(self.main_frame)
        self.fr_botoes_subir_descer.pack(side=LEFT)
        
        self.fr_entrada_de_dados = Frame(self.main_frame)
        self.fr_entrada_de_dados.pack(side=RIGHT)

        self.dict_de_dados = {}

        
    def main(self):

        self.botao_subir()
        self.botao_descer()


    def _get(self):
        pass


    def _set(self):
        pass


    def botao_subir(self):

        self.bt_subir = Button(self.fr_botoes_subir_descer, text=" /\ ", height=5, command=)


    def botao_descer(self):
        pass


    def botao_limpar(self):
        pass


    def botao_deletar(self):
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
