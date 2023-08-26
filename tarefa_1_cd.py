# -*- coding: utf-8 -*-
"""Tarefa_1_CD.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1a-GP5oXuwx8DjpUl2gOy0hIwPGCBYKfx

#Estrutura curricular do TADS - 2023

Dicionário
"""

import pandas as pd

estrutura_curricular = {'codigo': ['TAD0001','TAD0006','TAD0102','TAD0105','TAD0201','TAD0202','TAD0009','TAD0012','TAD0013','TAD0016',
                                   'TAD0103','TAD0111','TAD0114','TAD0004','TAD0019','TAD0020','TAD0022','TAD0025','TAD0123','TAD0203',
                                   'TAD0018','TAD0027','TAD0028','TAD0029','TAD0030','TAD0032','TAD0204','TAD0015','TAD0108','TAD0156',
                                   'TAD0160','TAD0205','TAD0035','TAD0140','TAD0157' ],
                        'nome': ['FUNDAMENTOS DA COMPUTACAO','SISTEMAS OPERACIONAIS','ALGORITMOS E PROGRAMAÇÃO','MATEMÁTICA APLICADA',
                                 'RACIOCÍNIO LÓGICO','LEITURA E PRODUÇÃO DE TEXTOS','PROGRAMACAO ORIENTADA A OBJETOS',
                                 'PROCESSO DE DESENVOLVIMENTO DE SOFTWARE','MATEMATICA APLICADA II','VERTENTES PRODUTIVAS NAS CIENCIAS AGRARIAS',
                                 'BANCO DE DADOS','PROGRAMAÇÃO VISUAL E AUTORIA WEB','REDES DE COMPUTADORES','ANALISE E PROJETO ORIENTADO A OBJETOS',
                                 'PROGRAMACAO WEB','ESTRUTURAS DE DADOS','ESTATISTICA APLICADA','INTELIGÊNCIA COMPUTACIONAL','SISTEMAS DIGITAIS',
                                 'GESTÃO DE QUALIDADE DE SOFTWARE','PROCESSAMENTO DIGITAL DE IMAGENS','PROGRAMACAO PARA DISPOSITIVOS MOVEIS',
                                 'PLANEJAMENTO E GERENCIA DE PROJETOS','ARQUITETURA DE SOFTWARE','MICROCONTROLADORES','METODOLOGIA DO TRABALHO CIENTIFICO',
                                 'FUNDAMENTOS E TÉCNICAS EM CIÊNCIA DE DADOS','EMPREENDEDORISMO','CONTEXTO GEOGRÁFICO REGIONAL','PROJETOS APLICADOS I',
                                 'SISTEMAS DISTRIBUÍDOS','TRABALHO DE CONCLUSÃO DE CURSO I','LEGISLACAO E ETICA EM TI','TRABALHO DE CONCLUSAO DE CURSO II',
                                 'PROJETOS APLICADOS II'],
                        'carga_horaria': ['60h','60h','90h','60h','45h','60h','60h','45h','60h','45h','60h','60h','45h','60h','60h','45h',
                                          '60h','45h','45h','60h','60h','90h','45h','45h','60h','30h','60h','45h','30h','60h','30h','30h',
                                          '45h','60h','60h'],
                        'periodo': ['1','1','1','1','1','1','2','2','2','2','2','2','2','3','3','3','3','3','3','3','4','4','4','4','4','4','4',
                                    '5','5','5','5','5','6','6','6']
                        }

"""Dicionário de cada semestre com a lista de códigos das disciplinas do semestre"""

df = pd.DataFrame(data=estrutura_curricular)
print(df)

"""Dicionário com o código de cada disciplina e a lista de códigos dos pré requisitos, se houver. Para as que não tem pré-requisito, basta não inserir no dicionário"""

pre_requisitos = {'TAD0009': ['TAD0102'], #PROGRAMACAO ORIENTADA A OBJETOS --> ALGORITMOS E PROGRAMAÇÃO
                  'TAD0013': ['TAD0105'], #MATEMATICA APLICADA II --> MATEMÁTICA APLICADA
                  'TAD0019': ['TAD0009'], #PROGRAMACAO WEB --> PROGRAMACAO ORIENTADA A OBJETOS
                  'TAD0020': ['TAD0102'], #ESTRUTURAS DE DADOS --> ALGORITMOS E PROGRAMAÇÃO
                  'TAD0025': ['TAD0102'], #INTELIGÊNCIA COMPUTACIONAL --> ALGORITMOS E PROGRAMAÇÃO
                  'TAD0018': ['TAD0102'], #PROCESSAMENTO DIGITAL DE IMAGENS --> ALGORITMOS E PROGRAMAÇÃO
                  'TAD0027': ['TAD0009'], #PROGRAMACAO PARA DISPOSITIVOS MOVEIS --> PROGRAMACAO ORIENTADA A OBJETOS
                  'TAD0029': ['TAD0009, TAD0111, TAD0103'], #ARQUITETURA DE SOFTWARE --> PROGRAMACAO ORIENTADA A OBJETOS --> PROGRAMAÇÃO VISUAL E AUTORIA WEB --> BANCO DE DADOS
                  'TAD0204': ['TAD0022, TAD0102'], #FUNDAMENTOS E TÉCNICAS EM CIÊNCIA DE DADOS --> ESTATISTICA APLICADA --> ALGORITMOS E PROGRAMAÇÃO
                  'TAD0156': ['TAD0102,TAD0103,TAD0012'], #PROJETOS APLICADOS I --> ALGORITMOS E PROGRAMAÇÃO --> PROGRAMAÇÃO VISUAL E AUTORIA WEB --> PROCESSO DE DESENVOLVIMENTO DE SOFTWARE
                  'TAD0160': ['TAD0114'], #SISTEMAS DISTRIBUÍDOS --> ALGORITMOS E PROGRAMAÇÃO
                  'TAD0157': ['TAD0156, TAD0028'] #PROJETOS APLICADOS II --> PROJETOS APLICADOS I --> PLANEJAMENTO E GERENCIA DE PROJETOS
                 }

df = pd.DataFrame(data=pre_requisitos)
pre_requisitos

print(pre_requisitos)