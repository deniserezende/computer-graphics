//
//  PaintGlut.cpp
//  ThirdProject
//
//  Created by Denise F. de Rezende on 24/04/23.
//

#include "PaintGlut.hpp"
#define GL_SILENCE_DEPRECATION
#include <GLUT/GLUT.h>
#define WINDOW_WIDTH 640
#define WINDOW_HEIGHT 480

void drawLine(int x1, int y1, int x2, int y2);
void mouse(int button, int state, int x, int y);
void motion(int x, int y);
void clearScreen();
void menu(int value);
void display();
void keyboard(unsigned char key, int x, int y);

// Variáveis para armazenar as informações do traço
int startX, startY, endX, endY;
int color = 0;
int thickness = 1;

void InitPaint(int argc, char** argv, char const* title){
    // Inicializa o GLUT e processa qualquer parâmetro passado pela linha de comandos. Deve ser chamada antes de qualquer outra rotina GLUT.
    
    glutInit(&argc, argv);
    // Especifica como o vídeo será utilizado, no caso será alocado um buffer e o sistema de cor será RGB.
    glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB);
    
    // Especifica as dimensões da janela em pixels.
    glutInitWindowSize (WINDOW_WIDTH, WINDOW_HEIGHT);
    
    // Especifica a coordenada superior esquerda da janela. Define a localização da janela dentro da tela
    glutInitWindowPosition (100, 100);
    
    // Cria a janela e devolve um identificador único para a janela. Até que o comando glutMainLoop seja chamado, a janela não será mostrada.
    glutCreateWindow (title);
}

void SetDefaultsForPaint(void){
    // Setando a cor do fundo branco
    glClearColor(1.0,1.0,1.0,0.0);
    
    gluOrtho2D(0.0, WINDOW_WIDTH, WINDOW_HEIGHT, 0.0);
}

void CreatingMenuForPaint(){
    int colorMenu = glutCreateMenu(menu);
    glutAddMenuEntry("Vermelho", 0);
    glutAddMenuEntry("Verde", 1);
    glutAddMenuEntry("Azul", 2);
    int thicknessMenu = glutCreateMenu(menu);
    glutAddMenuEntry("Fino", 3);
    glutAddMenuEntry("Médio", 4);
    glutAddMenuEntry("Grosso", 5);
    
    glutCreateMenu(menu);
    glutAddSubMenu("Cor", colorMenu);
    glutAddSubMenu("Espessura", thicknessMenu);
    glutAddMenuEntry("Limpar tela", 6);
    glutAttachMenu(GLUT_RIGHT_BUTTON);
}


void SetPaint(int argc, char** argv, char const* title){
    InitPaint(argc, argv, title);
    SetDefaultsForPaint();
    glutMouseFunc(mouse);
    glutMotionFunc(motion);
    glutDisplayFunc(display);
    CreatingMenuForPaint();
    glutKeyboardFunc(keyboard);
}

void StartPaint(){
    glutMainLoop();
}

void drawLine(int x1, int y1, int x2, int y2) {
    glColor3f(color == 0 ? 1.0 : 0.0,
            color == 1 ? 1.0 : 0.0,
            color == 2 ? 1.0 : 0.0);
    glLineWidth(thickness);
    glBegin(GL_LINES);
    glVertex2i(x1, y1);
    glVertex2i(x2, y2);
    glEnd();
    glFlush();
}

void mouse(int button, int state, int x, int y) {
    if (button == GLUT_LEFT_BUTTON && state == GLUT_DOWN) {
        startX = x;
        startY = y;
    }
}

void motion(int x, int y) {
    endX = x;
    endY = y;
    drawLine(startX, startY, endX, endY);
    startX = endX;
    startY = endY;
}

void clearScreen() {
    // Limpa todos os traços da tela
    glClear(GL_COLOR_BUFFER_BIT);
    glFlush();
}

void keyboard(unsigned char key, int x, int y) {
   if (key == 'D' || key == 'd') {
       clearScreen();
   }
}


void menu(int value) {
    switch (value) {
        case 0: color = 0; break;
        case 1: color = 1; break;
        case 2: color = 2; break;
        case 3: thickness = 1; break;
        case 4: thickness = 5; break;
        case 5: thickness = 10; break;
        case 6: clearScreen(); break;
    }
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT);
    glFlush();
}

