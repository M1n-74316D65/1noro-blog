---
title: "Solución a algunas series numéricas en Java y Python"
date: 2020-10-04T11:36:00+01:00
draft: false
tags: ["java", "python", "programación"]
---

Lista del código que calcula las diferentes series numéricas propuestas
en el Ejercicio evaluable 1 de la asignatura Programación Multimedia y
Dispositivos Móviles.

> *Voy a tomar como regla que todas las listas serán de 100 elementos
> como máximo.*

## 1. La serie de Fibonacci

Mi explicación: Empezando con `[0, 1]`, el siguiente se calcula
con la suma de los dos anteriores.

### Fibonacci en Java

    package ej1pmydm;

    public class Ej1pmydm {
        public static void main(String[] args) {
            double lista[] = new double[100];
            lista[0] = 0;
            lista[1] = 1;
            int i = 1;
            while (i < lista.length - 1) {
                lista[i + 1] = lista[i - 1] + lista[i];
                i++;
            }
            for (i = 0; i < lista.length; i++) {
                System.out.println(lista[i]);
            }
        }
    }

### Fibonacci en Python

    lista = [0, 1]
    while len(lista) < 100:
        lista.append(lista[-2] + lista[-1])
    print(lista)

## 2. La serie de Tribonacci

Mi explicación: Empezando con `[1, 1, 2]`, el siguiente se
calcula con la suma de los tres anteriores.

### Tribonacci en Java

    package ej2pmydm;

    public class Ej2pmydm {
        public static void main(String[] args) {
            double lista[] = new double[100];
            lista[0] = 1;
            lista[1] = 1;
            lista[2] = 2;
            int i = 2;
            while (i < lista.length - 1) {
                lista[i + 1] = lista[i - 2] + lista[i - 1] + lista[i];
                i++;
            }
            for (i = 0; i < lista.length; i++) {
                System.out.println(lista[i]);
            }
        }
    }

### Tribonacci en Python

    lista = [1, 1, 2]
    while len(lista) < 100:
        lista.append(lista[-3] + lista[-2] + lista[-1])
    print(lista)

## 3. La serie en la cual si el anterior es par se suman los tres anteriores y, si es impar, solo los dos anteriores

Mi explicación: Empezamos con la lista `[1, 1]`.

-   Si el último es impar, se suman los 2 últimos para calcular el
    siguiente.
-   Si el último es par, se suman los 3 últimos para calcular el
    siguiente.

### La serie anterior en Java

    package ej3pmydm;

    public class Ej3pmydm {
        public static void main(String[] args) {
            double lista[] = new double[100];
            lista[0] = 1;
            lista[1] = 1;
            int i = 1;
            while (i < lista.length - 1) {
                if (lista[i] % 2 != 0) {
                    lista[i + 1] = lista[i - 1] + lista[i];
                } else {
                    lista[i + 1] = lista[i - 2] + lista[i - 1] + lista[i];
                }
                i++;
            }
            for (i = 0; i < lista.length; i++) {
                System.out.println(lista[i]);
            }
        }
    }

### La serie anterior en Python

    lista = [1, 1]
    while len(lista) < 100:
        if lista[-1] % 2 != 0:
            lista.append(lista[-1] + lista[-2])
        else:
            lista.append(lista[-1] + lista[-2] + lista[-3])
    print(lista)

## 4. La serie de los cuadrados perfectos escritos al revés

Tengo dudas, no sé si se refiere a esto:

### Los cuadrados perfectos al revés en Java

    package ej4pmydm;

    public class Ej4pmydm {
        public static void main(String[] args) {
            int lista[] = new int[100];
            int numero = 100;
            int i = 0;
            while (i < lista.length) {
                lista[i] = numero * numero;
                numero---;
                i++;
            }
            for (i = 0; i < lista.length; i++) {
                System.out.println(lista[i]);
            }
        }
    }

### Los cuadrados perfectos al revés en Python

    lista = []
    numero = 100
    while numero > 0:
        lista.append(numero * numero)
        numero -= 1
    print(lista)

## 5. La serie que suma las cifras de los anteriores

Ojo, se refiere a el **número de cifras**, no a la suma del os valores
anteriores.

### La suma las cifras de los anteriores en Java

    package ej5pmydm;

    public class Ej5pmydm {
        public static void main(String[] args) {
            int lista[] = new int[100];
            lista[0] = 1;
            int i = 0;
            while (i < lista.length - 1) {
                lista[i+1] = lista[i] + Integer.toString(lista[i]).length();
                i++;
            }
            for (i = 0; i < lista.length; i++) {
                System.out.println(lista[i]);
            }
        }
    }

### La suma las cifras de los anteriores en Python

    lista = [1]
    while len(lista) < 100:
        nuevo = 0
        for numero in lista:
            nuevo += len(str(numero))
        lista.append(nuevo)
    print(lista)
