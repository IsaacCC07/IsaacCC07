
# Portafolio de Aprendizaje en Ciberseguridad

---

## 🛠️ Herramientas Desarrolladas

### 1. Simple Port Scanner (Python)
Este script permite realizar un escaneo de puertos TCP para identificar servicios activos en una máquina objetivo.

*   **Lógica del script:** Utiliza la librería `socket` para realizar un "Three-Way Handshake" parcial. Si el puerto responde, se reporta como abierto.
*   **Uso:** 
    ```bash
    python3 scanner.py
    ```


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

## 📂 WriteUps

 guías sobre como resuelvo algunas maquinas paso a paso:

*   **[Explotación de VNC (Puerto 5900)]**: Cómo obtener acceso root mediante una debilidad en la configuración de contraseñas del servicio VNC.

## 🛠️ Herramientas Utilizadas
- **Kali Linux** (Máquina atacante)
- **Metasploitable 2** (Máquina objetivo)
- **Nmap** (Escaneo de red)
- **Metasploit Framework** (Explotación)
- **VNCViewer** (Acceso remoto)

---
> [!IMPORTANT]
> **Aviso de Seguridad:** Todo el contenido aquí compartido tiene fines estrictamente educativos y éticos. No me hago responsable del mal uso de esta información.
