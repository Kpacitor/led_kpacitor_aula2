#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, url_for
import requests
import RPi.GPIO as GPIO
import time
import os

app = Flask(__name__)

# Limpando qualquer configurações anteriores
GPIO.cleanup()

# Configurando com o padão BCM (Padrão do Chip da Broadcom)
GPIO.setmode(GPIO.BCM)

# Confuigurando os pinos como saída
GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

led1 = GPIO.PWM(17, 100) #Criando objeto para o Led1
led2 = GPIO.PWM(22, 100) #Criando objeto para o Led2
led3 = GPIO.PWM(23, 100) #Criando objeto para o Led3
led4 = GPIO.PWM(27, 100) #Criando objeto para o Led4

#Função para receber a URL e comandar os leds
@app.route("/")
@app.route('/comando_led/<int:cod_led>/', methods=['GET', 'POST'])
def comando_led(cod_led):
	if request.method == 'GET':
		if cod_led == 1:
			led1.start(100)
		elif cod_led == 2:
			led2.start(100)
		elif cod_led == 3:
			led3.start(100)
		elif cod_led == 4:
			led4.start(100)	
		elif cod_led == 5:
			led1.stop()
		elif cod_led == 6:
			led2.stop()
		elif cod_led == 7:
			led3.stop()
		elif cod_led == 8:
			led4.stop()
		else:
			led1.stop()
			led2.stop()
			led3.stop()
			led4.stop()

	return render_template('led_interface.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
