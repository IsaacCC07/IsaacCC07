 # Introducción
 
 Este documento detalla el proceso de identificación y explotación de una vulnerabilidad de autenticación débil en el servicio VNC
 (Virtual Network Computing) de la máquina Metasploitable 2.El objetivo es demostrar cómo una configuración
 insegura permite obtener acceso remoto total al sistema.

## Fase 1: Reconocimiento (Reconnaissance)
### En esta etapa buscamos identificar la dirección IP del objetivo dentro de nuestra red local utilizando la herramienta netdiscover.

bash sudo netdiscover -r 192.168.1.0/24

![uno](https://github.com/IsaacCC07/IsaacCC07/blob/6d75e701c0d9cc8196701699b6ff8c44ca4d702b/img/1.PNG)

###Procedemos a realizar un escaneo de puertos y servicios con Nmap para determinar 
qué puertos están abiertos y qué versiones de software están ejecutando.

bash nmap -sV -sS -p- --open 192.168.1.59

![dos](https://github.com/IsaacCC07/IsaacCC07/blob/82d7821f84d4c3badf41d916684b8ff0ffe2e880/img/2.PNG)
