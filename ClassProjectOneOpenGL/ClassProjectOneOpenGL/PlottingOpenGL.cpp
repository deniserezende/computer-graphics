//
//  PlottingOpenGL.cpp
//  ClassProjectOneOpenGL
//
//  Created by Denise F. de Rezende on 28/03/23.
//

#define GL_SILENCE_DEPRECATION
#include "PlottingOpenGL.hpp"
#include <GLUT/GLUT.h>
#include <stdlib.h>
#include <math.h>
#include <stdio.h>

void Init(int argc, char** argv, char const* title){
    // Inicializa o GLUT e processa qualquer parâmetro passado pela linha de comandos. Deve ser chamada antes de qualquer outra rotina GLUT.
    
    glutInit(&argc, argv);
    // Especifica como o vídeo será utilizado, no caso será alocado um buffer e o sistema de cor será RGB.
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
    
    // Especifica as dimensões da janela em pixels.
    glutInitWindowSize (640, 480);
    
    // Especifica a coordenada superior esquerda da janela. Define a localização da janela dentro da tela
    glutInitWindowPosition (100, 100);
    
    // Cria a janela e devolve um identificador único para a janela. Até que o comando glutMainLoop seja chamado, a janela não será mostrada.
    glutCreateWindow (title);
}

void SetDefaults(void){
    // Setando a cor do fundo branco
    glClearColor(1.0,1.0,1.0,0.0);
    
    // Define cor corrente de desenho
    glColor3f(0.0f, 0.0f, 0.0f);
    
    // Define o tamanho do ponto: 4 por 4 pixels
    glPointSize(4.0);
    
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    
    // Define janela com resolução de 640 por 480
    gluOrtho2D(0.0, 640.0, 0.0, 480.0);
}

void ExamplePoints(void){
        glClear(GL_COLOR_BUFFER_BIT); // limpa a janela
        glBegin(GL_POINTS);
            glVertex2f(100, 50); // desenha 3 pontos
            glVertex2f(100, 130);
            glVertex2i(150, 130);
        glEnd();
        glFlush(); // Garante a execução de todas as rotinas de desenho
}

void ExampleLine(void){
        glClear(GL_COLOR_BUFFER_BIT); // limpa a janela
        glBegin(GL_LINES);
            glVertex2f(100, 50); // desenha 1 linha
            glVertex2f(20, 130);
        glEnd();
        glBegin(GL_LINES);
            glVertex2f(20, 130); // desenha 1 linha
            glVertex2f(30, 200);
        glEnd();
        glBegin(GL_LINES);
            glVertex2f(30, 200); // desenha 1 linha
            glVertex2f(100, 50);
        glEnd();
        glFlush(); // Garante a execução de todas as rotinas de desenho
}

void DisplayFunction(void (*func)(void)){
    glutDisplayFunc(func);
}


// A rotina a seguir termina o programa com a tecla Esc
void Keyboard(unsigned char key, int x, int y){
     switch (key) {
         case 27:
         exit(0);
         break;
     }
}

void KeyboardFunction(void (*func)(unsigned char key, int x, int y)){
    glutKeyboardFunc(func);
}


void ShowWindowsLoop(){
    // É o último comando que chamamos. Ele faz com que todas as janelas criadas sejam mostradas. Uma vez que entramos neste loop, só saímos quando o programa se encerra.
    glutMainLoop( );
}
