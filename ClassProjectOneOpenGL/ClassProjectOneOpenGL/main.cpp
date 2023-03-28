//
//  main.cpp
//  ClassProjectOneOpenGL
//
//  Created by Denise F. de Rezende on 28/03/23.
//

#include "PlottingOpenGL.hpp"
#include <stdlib.h>
#include <math.h>
#include <stdio.h>

int main(int argc, char** argv){
    char const *program_name = "Meu Primeiro Programa";
    // Rotina que implementa as configurações iniciais do programa.
    Init(argc, argv, program_name);
    
    // Rotina que seta parametros defauls, exemplo: cor do fundo, cor do ponto, tamanho do ponto...
    SetDefaults();
    
    // Chamada para a função de desenho enviando a rotina que cria alguns pontos
    DisplayFunction(ExampleLine); // Toda vez que o GLUT determinar que a janela tem de ser desenhada, ele chamará a função aqui determinada.
    
    // Determinam as funções que usaremos para ler o teclado e o mouse respectivamente.
    KeyboardFunction(Keyboard);
    
    ShowWindowsLoop();
    
    return 0;
}

