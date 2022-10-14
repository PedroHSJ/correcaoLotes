from crianca10Anos import crianca10Anos
from domicilioFamiliaSemMembro import domicilio_familia_sem_membro
from sexoDoIndividuo import sexo_do_individuo
from numeroMoradores import numero_moradores
from microarea import microarea

try:
    crianca10Anos()
    domicilio_familia_sem_membro()
    sexo_do_individuo()
    numero_moradores()
    microarea()
except e:
    print(e)
    