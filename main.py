from crianca10Anos import crianca10Anos
from desfechoDaVisita3ou2 import desfecho_da_visita_3ou2
from domicilioFamiliaSemMembro import domicilio_familia_sem_membro
from microarea import microarea
from motivosVisita import motivos_visita
from numeroMoradores import numero_moradores
from numeroMoradoresNaoPodeSerPreenchido import numero_moradores_nao_pode_ser_preenchido
from sexoDoIndividuo import sexo_do_individuo
from sexoDoIndividuoNaoDeveSerPreenchida_02_03 import sexo_do_individuo_nao_deve_ser_preenchido
from situacaoMoradiaNaoPodeSerNull import situacao_moradia_nao_pode_ser_null
from situacaoRuaHigienePessoal import situacao_rua_higiene_pessoal
from tipoDeLogradouro import tipo_de_logradouro
from tipoLogradouroPreenchimentoObrigatorio import tipo_logradouro_preenchimento_obrigatorio



try:
    crianca10Anos()
    desfecho_da_visita_3ou2()
    domicilio_familia_sem_membro()
    microarea()
    motivos_visita()
    numero_moradores()
    numero_moradores_nao_pode_ser_preenchido()
    sexo_do_individuo()
    sexo_do_individuo_nao_deve_ser_preenchido()
    situacao_moradia_nao_pode_ser_null()
    situacao_rua_higiene_pessoal()
    tipo_de_logradouro()
    tipo_logradouro_preenchimento_obrigatorio()
except e:
    print(e)
    