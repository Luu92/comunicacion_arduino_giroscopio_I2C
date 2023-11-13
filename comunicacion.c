/*
 * Datos_Giroscopio_Interfaz_Grafica.c
 *
 * Created: 12/11/2023 09:19:55 p. m.
 * Author : DevLuu
 */ 
#include <avr/io.h>
#include <util/delay.h>
#include <stdio.h>

// Definir baud rate
#define BAUD 9600
#define MYUBRR F_CPU/16/BAUD-1

// Función para inicializar USART
void USART_Init(unsigned int ubrr) {
	UBRR0H = (unsigned char)(ubrr >> 8);
	UBRR0L = (unsigned char)ubrr;
	UCSR0B = (1 << TXEN0) | (1 << RXEN0);   // Habilitar transmisión y recepción
	UCSR0C = (1 << UCSZ01) | (1 << UCSZ00); // 8 bits de datos, 1 bit de stop
}

// Función para transmitir un byte
void USART_Transmit(unsigned char data) {
	while (!(UCSR0A & (1 << UDRE0))); // Esperar a que el buffer de transmisión esté vacío
	UDR0 = data; // Colocar el dato en el buffer, se envía automáticamente
}

// Función principal
int main(void) {
	// Inicializar USART con el baud rate deseado
	USART_Init(MYUBRR);

	// Inicializar el giroscopio (ajustar según tus necesidades)
	// Aquí deberías tener tu código de inicialización del giroscopio
	
	while (1) {
		// Leer datos del giroscopio (ajustar según tus necesidades)
		int16_t gyroX = 123; // Reemplaza esto con la lectura real del giroscopio
		int16_t gyroY = 456; // Reemplaza esto con la lectura real del giroscopio
		int16_t gyroZ = 789; // Reemplaza esto con la lectura real del giroscopio

		// Enviar datos a través de USART
		USART_Transmit((gyroX >> 8) & 0xFF);
		USART_Transmit(gyroX & 0xFF);

		USART_Transmit((gyroY >> 8) & 0xFF);
		USART_Transmit(gyroY & 0xFF);

		USART_Transmit((gyroZ >> 8) & 0xFF);
		USART_Transmit(gyroZ & 0xFF);

		// Pausa para evitar que los datos se envíen demasiado rápido
		_delay_ms(100);
	}
}
