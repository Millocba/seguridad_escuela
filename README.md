
# SEGURIDAD_ESCUELAS

Aplicación web responsive para el registro, reporte y gestión de incidentes en escuelas públicas de la provincia de Córdoba.

## 🚀 Tecnologías
- **Backend**: FastAPI (Python)
- **Base de Datos**: MySQL
- **Frontend**: Web responsive (HTML, CSS, JS)
- **Autenticación**: JWT + 2FA
- **Multimedia**: Enlaces externos (S3, GDrive, etc.)

## 👤 Roles del Sistema
- **Directivos**: Reportan incidentes y administran datos de su escuela.
- **Auditores**: Visualizan métricas y reportes.
- **Administradores**: Alta/Baja/Modificación de usuarios y escuelas, validación de registros.

## ⚙️ Funcionalidades
- Registro y login seguro con 2FA.
- ABM de usuarios y escuelas.
- Reporte de incidentes con multimedia.
- Visualización de métricas y estadísticas.
- Gestión de seguridad (domos, alarmas, adicionales).

## 📦 Instalación

```bash
git clone https://github.com/usuario/seguridad_escuelas.git
cd seguridad_escuelas
pip install -r requirements.txt
uvicorn main:app --reload
```

## 🧪 Base de Datos
La estructura inicial de la base de datos está en el archivo `database.sql`.

## 🛡️ Seguridad
Cumple con regulaciones de privacidad y cifrado de contraseñas. Autenticación de dos factores opcional.

## ✉️ Contacto
Desarrollado por [Dafne]. Contacto: tu. dafne.farias.090@gmail.com
