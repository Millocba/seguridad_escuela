# schemas/__init__.py
from .usuario import *
from .escuela import *
from .alarma import *
from .reporte import *
__all__ = [
    "Usuario", "UsuarioCreate", "UsuarioUpdate", "RolEnum",
    "Escuela", "EscuelaCreate", "EscuelaUpdate",
    "Alarma", "AlarmaCreate", "AlarmaUpdate",
    "Reporte", "ReporteCreate", "ReporteUpdate", "TipoIncidenteEnum"
]