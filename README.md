## Hi there 👋

# 🛡️ Mi Portafolio de Aprendizaje en Ciberseguridad

¡Bienvenido! En este repositorio documento mis herramientas de automatización y mis prácticas de hacking ético. Mi objetivo es demostrar mis habilidades en **Python**, **Scripting en Bash** y **Pentesting**.

---

## 🛠️ Herramientas Desarrolladas

### 1. Simple Port Scanner (Python)
Este script permite realizar un escaneo de puertos TCP para identificar servicios activos en una máquina objetivo.

*   **Lógica del script:** Utiliza la librería `socket` para realizar un "Three-Way Handshake" parcial. Si el puerto responde, se reporta como abierto.
*   **Uso:** 
    ```bash
    python3 scanner.py
    ```
*   **Aprendizaje:** Gestión de tiempos de espera (timeouts) y manejo de conexiones de red en Python.


## 2. 🚀 Automatización de Entorno Seguro (ZSH Functions)

He desarrollado una suite de comandos personalizados integrados directamente en la shell (`.zshrc`) para gestionar el anonimato del sistema de forma interactiva.

### Comando: `abrir`
Activa un túnel de seguridad completo y ofrece una interfaz de lanzamiento de herramientas.
- **Flujo de trabajo:**
  1. Inicia **Anonsurf** (Túnel Tor para todo el sistema).
  2. Arranca el servicio **Tor** local.
  3. Verifica la IP pública para confirmar el enmascaramiento.
  4. **Menú Interactivo:** Permite lanzar automáticamente **Firefox** o **Nmap** bajo la protección de **Proxychains**.

### Comando: `cerrar`
Finaliza todos los servicios de forma limpia.
- **Flujo de trabajo:** Detiene Anonsurf y el servicio Tor, verificando la restauración de la IP real del usuario para evitar fugas de información accidentales.

---
