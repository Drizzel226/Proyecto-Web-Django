python manage.py shell
from porque.utils import importar_miembros
importar_miembros()


    # Campos existentes
    que_ocurre = models.TextField("¿Qué ocurre? ¿En qué parte de la máquina o materal se visualiza el problema?")
    como_ocurre = models.TextField("¿Cómo ocurre? Describir desde el punto de vista físico el mecanismo de acción visibilizado en el momento.")
    donde_ocurre = models.TextField("¿Dónde ocurre? Producto, equipo, zona de la máquina, etc.")
    cuando_ocurre = models.TextField("¿Cuando ocurrió? Producción, arranque, saneado, cambio de formato, mantención, etc.")
    quien_presente = models.TextField("¿Quién estaba presente cuando ocurrió? ¿El problema pasa en todos los turnos?")