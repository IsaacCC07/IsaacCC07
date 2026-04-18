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

### 2. Anonimato Suite (Bash)
Script de automatización para gestionar herramientas de privacidad en sistemas Linux (Kali/Parrot).

*   **Funciones:**
    *   Inicio rápido de **Anonsurf** para forzar todo el tráfico a través de la red Tor.
    *   Configuración y ejecución de **Proxychains** para herramientas específicas.
*   **Requisito:** Tener instalado `anonsurf` y el servicio `tor`.

---
