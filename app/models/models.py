# app/models/models.py
# Archivo para importar todos los modelos fácilmente

from .usuario import Usuario, RolEnum
from .escuela import Escuela
from .alarma import Alarma
from .reporte import Reporte, TipoIncidenteEnum

__all__ = ["Usuario", "RolEnum", "Escuela", "Alarma", "Reporte", "TipoIncidenteEnum"]
# Este archivo permite importar todos los modelos desde un solo lugar
# y facilita la organización del código en el proyecto.
# Puedes importar los modelos en otros archivos de la siguiente manera:
# from app.models import Usuario, Escuela, Alarma, Reporte, RolEnum, TipoIncidenteEnum
# Esto hace que el código sea más limpio y fácil de mantener.
# Asegúrate de que este archivo esté en la carpeta correcta y que los modelos
# estén correctamente definidos en sus respectivos archivos.    