---
title: "Expandir una partición EXT4 de forma dinámica"
date: 2021-11-14T21:16:00+01:00
draft: false
tags: ["linux", "comandos"]
---

El sistema de archivos EXT4 te permite redimensionar las particiones de
un disco duro sin tener que apagar el PC ni borrar tus datos. En caso de
no utilizar el 100% de tu disco duro, o si estas gestionando discos
virtuales, estes sencillos comandos te pueden facilitar la vida sin
tener que volver a formatear el disco.

> *Antes de realizar cualquier modificacion en el disco es necesario
> señalar la importancia de tener un backup reciente a mano por si
> metemos la pata.*

## Aumentar partición hasta un tamaño exacto

Suponiendo que la partición que quieres expandir es `/dev/sdb1` (**la
única del disco**), con un tamaño inicial de **200MB**, y que quieres
que su tamaño sea de **400MB**, podemos ejecutar los siguientes
comandos:

    sudo parted /dev/sdb resizepart 1 400M
    sudo resize2fs /dev/sdb1

## Aumentar partición hasta ocupar la totalidad del disco

Suponiendo que la partición que quieres expandir es `/dev/sdb1` (**la
única del disco**), cuyo tamano es **menor a la totalidad del disco**,
podemos ejecutar los siguientes comandos para que lo ocupe todo:

    sudo parted /dev/sdb resizepart 1 100%
    sudo resize2fs /dev/sdb1

> Cualquier mejora o precaución que veais necesaria añadir a estos
> comandos es bienvenida, en tal caso solo debeis hacermelo saber a
> través del [medio que prefirais](#contacto).
