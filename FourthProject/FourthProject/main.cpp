//
//  main.cpp
//  FourthProject
//
//  Created by Denise F. de Rezende on 25/04/23.
//
#define GL_SILENCE_DEPRECATION
#include <iostream>
#include <GLUT/GLUT.h>
#define WINDOW_WIDTH 640
#define WINDOW_HEIGHT 480

GLfloat GL_angX = 0, GL_angY = 0;
GLfloat Sx = 1, Sy = 1;
GLfloat Tx = 0, Ty = 0;
GLint Qx = 100, Qy = 100, Qs = 70;

void Init(int argc, char** argv, char const* title){
    // Inicializa o GLUT e processa qualquer parâmetro passado pela linha de comandos. Deve ser chamada antes de qualquer outra rotina GLUT.
    
    glutInit(&argc, argv);
    // Especifica como o vídeo será utilizado, no caso será alocado um buffer e o sistema de cor será RGB.
    glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB);
    
    // Especifica as dimensões da janela em pixels.
    glutInitWindowSize (WINDOW_WIDTH, WINDOW_HEIGHT);
    
    // Especifica a coordenada superior esquerda da janela. Define a localização da janela dentro da tela
    glutInitWindowPosition (100, 100);
    
    // Cria a janela e devolve um identificador único para a janela. Até que o comando glutMainLoop seja chamado, a janela não será mostrada.
    glutCreateWindow (title);
    
    
    gluOrtho2D(0.0, WINDOW_WIDTH, 0.0, WINDOW_HEIGHT);
    glClearColor(1.0,1.0,1.0,0.0);
    glColor3f(0.5f, 0.7f, 1.0f);
    glMatrixMode(GL_MODELVIEW);
    
}



void drawSquare(GLint x, GLint y, GLint size) {
  glBegin(GL_QUADS); // inicia o desenho do quadrado
    glVertex2f(x, y); // vértice inferior esquerdo
    glVertex2f(x + size, y); // vértice inferior direito
    glVertex2f(x + size, y + size); // vértice superior direito
    glVertex2f(x, y + size); // vértice superior esquerdo
  glEnd(); // finaliza o desenho do quadrado
  glFlush(); // força o desenho na tela
}

void display() {
    glClear(GL_COLOR_BUFFER_BIT); // limpa o buffer de cor
    glPushMatrix();
    glLoadIdentity();
    gluOrtho2D(0.0, WINDOW_WIDTH, 0.0, WINDOW_HEIGHT);
    
    // calcula a posição do centro geométrico
    float cx = (2*Qx+2*(Qx+Qs)) / 4;
    float cy = (2*Qy+2*(Qy+Qs)) / 4;

    // Translate
    glTranslatef(Tx, Ty, 1);
    
    // Rotate
    // transfere para a origem e aplica a translação para o centro geométrico
    glTranslatef(cx, cy, 0.0f);
    glRotatef(GL_angX, 0.0, 0.0, 1.0);
    glTranslatef(-cx, -cy, 0.0f);

    // Scale
    // transfere para a origem e aplica a translação para o centro geométrico
    glTranslatef(cx, cy, 0.0f);
    glScalef(Sx, Sy, 1);
    glTranslatef(-cx, -cy, 0.0f);

    // desenha o quadrado na posição (100, 100) com tamanho 50
    drawSquare(Qx, Qy, Qs);
    glPopMatrix();

    glutSwapBuffers(); // força o desenho na tela
}

void clearScreen() {
    // Limpa todos os traços da tela
    glClear(GL_COLOR_BUFFER_BIT);
    glFlush();
}

void keyboard(unsigned char key, int x, int y) {
    switch (key) {
        case 'D':
        case 'd':
            GL_angX += 5;
            GL_angY += 5;
            
            break;
        case 'A':
        case 'a':
            GL_angX -= 5;
            GL_angY -= 5;
            break;
        case 'W':
        case 'w':
            Sx *= 1.2;
            Sy *= 1.2;
            break;
        case 'S':
        case 's':
            Sx /= 1.2;
            Sy /= 1.2;
            break;
        default:
            break;
    }
    glutPostRedisplay();
}


void specialkeyboard(int key, int x, int y) {
    switch (key) {
        case GLUT_KEY_UP:
            Ty += 10;
            break;
        case GLUT_KEY_DOWN:
            Ty -= 10;
            break;
        case GLUT_KEY_LEFT:
            Tx -= 10;
            break;
        case GLUT_KEY_RIGHT:
            Tx += 10;
            break;
        default:
            break;
    }
    glutPostRedisplay();
}

int main(int argc, char** argv) {
    Init(argc, argv, "Square Program");
    glutDisplayFunc(display);
    glutSpecialFunc(specialkeyboard);
    glutKeyboardFunc(keyboard);
    glutMainLoop();
}


