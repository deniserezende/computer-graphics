//
//  main.cpp
//  ProjectLabirintoDoTerror
//
//
//

#include <iostream>
#define GL_SILENCE_DEPRECATION
#include <GLUT/GLUT.h>

const int mazeWidth = 10;
const int mazeHeight = 10;
const int windowWidth = 800;
const int windowHeight = 600;
const float playerInitX = 0.25f;
const float playerInitY = 0.25f;

float playerX = playerInitX;  // Posição inicial do jogador (coordenada X)
float playerY = playerInitY;  // Posição inicial do jogador (coordenada Y)
int mouseX = 0;       // Posição atual do mouse (coordenada X)
int mouseY = 0;       // Posição atual do mouse (coordenada Y)

bool winGame = false;
bool gameOver = false;
bool startGame = false;


int maze[mazeHeight][mazeWidth] = {
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 3, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 0, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 0, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 0, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 0, 0, 0, 0, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 0, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 0, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 0, 0, 0, 2, 1},
    {1, 1, 1, 1, 1, 1, 1, 1, 1, 1}
};

void drawText(float x, float y, const std::string& text, void* font = GLUT_BITMAP_HELVETICA_18, float r = 1.0f, float g = 1.0f, float b = 1.0f) {
    glColor3f(r, g, b);
    glRasterPos2f(x, y);
    for (char c : text) {
        glutBitmapCharacter(font, c);
    }
}

void keyboard(unsigned char key, int x, int y) {
  if (key == 'r' || key == 'R') {
    startGame = false;
    gameOver = false;
    winGame = false;
    glutPostRedisplay();
  }
  if (key == 'q') {
    exit(0);
  }
}

void drawMaze() {
    glClearColor(0.0f, 0.0f, 0.0f, 1.0f);  // Define a cor de fundo como preto
    glClear(GL_COLOR_BUFFER_BIT);
    
    if(winGame){
        drawText(windowWidth/4, windowHeight/2, "Bom Trabalho!");
        drawText(windowWidth/4, windowHeight/2-20, "R = restart");
        drawText(windowWidth/4, windowHeight/2-40, "Q = quit");

    }
    else{
        
        if(gameOver){
            drawText(windowWidth/4, windowHeight/2, "BOOOM! Perdeu!");
            drawText(windowWidth/4, windowHeight/2-20, "R = restart");
            drawText(windowWidth/4, windowHeight/2-40, "Q = quit");
        }
        
        else{
            // Desenha o labirinto usando quadrados
            float cellWidth = static_cast<float>(windowWidth) / mazeWidth;
            float cellHeight = static_cast<float>(windowHeight) / mazeHeight;
            
            std::cout << "DRAW MAZE" << std::endl;

            for (int y = 0; y < mazeHeight; y++) {
                for (int x = 0; x < mazeWidth; x++) {
                    if (maze[y][x] == 1) {
                        glColor3f(0.0f, 0.0f, 0.0f);  // Cor para a parede (preto)
                    } else {
                        if(maze[y][x] == 2){
                            glColor3f(0.0f, 1.0f, 0.0f);  // Cor para o final (verde)
                        }
                        else{
                            if(maze[y][x] == 3){
                                glColor3f(0.0f, 0.0f, 1.0f);  // Cor para o inicio (azul)
                            }
                            else{
                                glColor3f(1.0f, 1.0f, 1.0f);  // Cor para o corredor (branco)
                            }
                        }
                    }

                    float posX = x * cellWidth;
                    float posY = y * cellHeight;

                    glBegin(GL_QUADS);
                    glVertex2f(posX, posY);
                    glVertex2f(posX + cellWidth, posY);
                    glVertex2f(posX + cellWidth, posY + cellHeight);
                    glVertex2f(posX, posY + cellHeight);
                    glEnd();
                }
            }
        }
        if(!startGame){
            drawText(10, 10, "To start go to the blue square.");
        }
    }
    
    // Desenha o jogador como um ponto vermelho
    glColor3f(1.0f, 0.0f, 0.0f);
    glPointSize(10.0f);
    glBegin(GL_POINTS);
    glVertex2f(playerX * windowWidth, playerY * windowHeight);
    glEnd();

    glutSwapBuffers();
}

bool checkCollision() {
    int cellX = static_cast<int>(playerX * mazeWidth);
    int cellY = static_cast<int>(playerY * mazeHeight);

    if (maze[cellY][cellX] == 1) {
        return true;  // O jogador colidiu com uma parede
    }

    return false;
}

bool checkWin() {
    int cellX = static_cast<int>(playerX * mazeWidth);
    int cellY = static_cast<int>(playerY * mazeHeight);

    if (maze[cellY][cellX] == 2) {
        return true;
    }

    return false;
}

bool checkStart() {
    
    int cellX = static_cast<int>(playerX * mazeWidth);
    int cellY = static_cast<int>(playerY * mazeHeight);

    if (maze[cellY][cellX] == 3) {
        return true;
    }

    return false;
}

// Função de atualização da posição do jogador
void atualizarJogador(int x, int y) {
    mouseX = x;
    mouseY = y;

    playerX = static_cast<float>(x) / windowWidth;
    playerY = static_cast<float>(windowHeight - y) / windowHeight;
    
    glutPostRedisplay();
}

void onMouseMove(int x, int y) {
    if(!winGame && !gameOver){
        atualizarJogador(x, y);
    }
    if(!startGame){
        if(checkStart()){
            std::cout << "START GAME" << std::endl;
            startGame = true;
        }
    }
    else{
        if (checkWin()) {
            std::cout << "WIN" << std::endl;
            playerX = playerInitX;  // Redefine a posição inicial do jogador
            playerY = playerInitY;
            winGame = true;
        }
        // Verifica colisões
        if (checkCollision()) {
            std::cout << "COLLISION" << std::endl;
            playerX = playerInitX;  // Redefine a posição inicial do jogador
            playerY = playerInitY;
            gameOver = true;
        }
    }
}


// Function to handle window resize
void resize(int width, int height) {
    glViewport(0, 0, width, height);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluOrtho2D(0, width, 0, height);
    glMatrixMode(GL_MODELVIEW);
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE);
    glutInitWindowSize(windowWidth, windowHeight);
    glutCreateWindow("Labirinto do Terror");
    glutDisplayFunc(drawMaze);
    glutPassiveMotionFunc(onMouseMove);
    glutKeyboardFunc(keyboard);
    glutReshapeFunc(resize);
    glutMainLoop();
    return 0;
}
