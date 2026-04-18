 # Introducción
 
 Este documento detalla el proceso de identificación y explotación de una vulnerabilidad de autenticación débil en el servicio VNC
 (Virtual Network Computing) de la máquina Metasploitable 2.El objetivo es demostrar cómo una configuración
 insegura permite obtener acceso remoto total al sistema.

## Fase 1: Reconocimiento (Reconnaissance)
### En esta etapa buscamos identificar la dirección IP del objetivo dentro de nuestra red local utilizando la herramienta netdiscover.


  ```bash
     sudo netdiscover -r 192.168.1.0/24
  ```
 

![uno](https://github.com/IsaacCC07/IsaacCC07/blob/6d75e701c0d9cc8196701699b6ff8c44ca4d702b/img/1.PNG)

# Fase 2: Escaneo de Puertos y Servicios
Procedemos a realizar un escaneo de puertos y servicios con Nmap para determinar 
qué puertos están abiertos y qué versiones de software están ejecutando.

```bash
   nmap -sV -sS -p- --open 192.168.1.59
```

![dos](https://github.com/IsaacCC07/IsaacCC07/blob/82d7821f84d4c3badf41d916684b8ff0ffe2e880/img/2.PNG)

# Fase 3: Explotación (Exploitation)
Utilizaremos el framework Metasploit para intentar descubrir las credenciales 
de acceso al servicioVNC mediante un ataque de diccionario/fuerza bruta.

Iniciamos metasploit con:

```bash
   msfconsole
```

![tres](https://github.com/IsaacCC07/IsaacCC07/blob/82d7821f84d4c3badf41d916684b8ff0ffe2e880/img/3.PNG)

le indicamos lo que queremos buscar, en este caso el protocolo vnc 3.3 con la palabra "search"

![ttro](https://github.com/IsaacCC07/IsaacCC07/blob/82d7821f84d4c3badf41d916684b8ff0ffe2e880/img/4.PNG)

seleccionamos el numero 4 con "use" o usamos la ruta indexada por metasploit

```bash
   use auxiliary/scanner/vnc/vnc_login
```

ahora seteamos la ip de la maquina vulnerable en RHOSTS para que funcione el exploit y posterior mente lo ejecutamos
usando "run" o "exploit"


![ttro](https://github.com/IsaacCC07/IsaacCC07/blob/82d7821f84d4c3badf41d916684b8ff0ffe2e880/img/5.PNG)

### Como veremos Tras ejecutar el módulo, el sistema nos arroja una coincidencia exitosa:

![ttro](https://github.com/IsaacCC07/IsaacCC07/blob/82d7821f84d4c3badf41d916684b8ff0ffe2e880/img/6.PNG)

# Fase 4: Acceso y Post-Explotación (Gaining Access)

Con la contraseña obtenida, utilizamos un cliente VNC para conectarnos gráficamente a la máquina víctima.

![ttro](https://github.com/IsaacCC07/IsaacCC07/blob/82d7821f84d4c3badf41d916684b8ff0ffe2e880/img/7.PNG)

Al ingresar la contraseña password, obtenemos una ventana con una terminal de comandos.
Y si ejecutamos el comando whoami, confirmamos que tenemos privilegios de root.

![ttro](https://github.com/IsaacCC07/IsaacCC07/blob/82d7821f84d4c3badf41d916684b8ff0ffe2e880/img/root.PNG)

# Conclusión y Recomendaciones

El compromiso del sistema fue posible debido al uso de una contraseña extremadamente débil. Para mitigar este riesgo, se recomienda:
- Implementar políticas de contraseñas robustas.
- Deshabilitar el servicio VNC si no es estrictamente necesario.
- Usar túneles SSH para cifrar el tráfico de VNC, ya que el protocolo 3.3 transmite datos en texto claro.
















