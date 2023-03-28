//
//  PlottingOpenGL.hpp
//  ClassProjectOneOpenGL
//
//  Created by Denise F. de Rezende on 28/03/23.
//

#ifndef PlottingOpenGL_hpp
#define PlottingOpenGL_hpp

#include <stdio.h>

void Init(int argc, char** argv, char const* title);
void SetDefaults(void);
void ExamplePoints(void);
void ExampleLine(void);
void Keyboard(unsigned char key, int x, int y);

// Funções mascaradas do GLUT
void DisplayFunction(void (*func)(void));
void KeyboardFunction(void (*func)(unsigned char key, int x, int y));
void ShowWindowsLoop();

#endif /* PlottingOpenGL_hpp */
