import numpy
import pygame
import random
from OpenGL.GL import *
from OpenGL.GL.shaders import *
from obj import *
import glm

# Shaders
vertex_shader = """
#version 460
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 vertexColor;

out vec3 ourColor;
uniform mat4 amatrix;

void main()
{
    gl_Position = amatrix * vec4(position, 1.0f);
    // ourColor = vertexColor;

}
"""

fragment_shader = """
#version 460

layout (location = 0) out vec4 fragColor;

uniform vec3 color;


in vec3 ourColor;

void main()
{
    // fragColor = vec4(ourColor, 1.0f);
    fragColor = vec4(color, 1.0f);
}
"""

# Model viewer class
class ModelViewer(object):
    def __init__(self, screen, model):
        self.screen = screen
        _, _, self.width, self.height = screen.get_rect()
        self.model = model

        self.angle = 0

        # Compile Shaders
        self.shader = self.compile_shader()
        glUseProgram(self.shader)

        # Vertex
        self.vertex_handling()

    def compile_shader(self):

        compiled_vertex_shader = compileShader(vertex_shader, GL_VERTEX_SHADER)
        compiled_fragment_shader = compileShader(fragment_shader, GL_FRAGMENT_SHADER)
        shader = compileProgram(
            compiled_vertex_shader,
            compiled_fragment_shader
        )
        return shader
        

    def calculateMatrix(self):
        i = glm.mat4(1)
        translate = glm.translate(i, glm.vec3(0, 0, 0))
        rotate = glm.rotate(i, glm.radians(self.angle), glm.vec3(0, 1, 0))
        scale = glm.scale(i, glm.vec3(1, 1, 1))

        model = translate * rotate * scale

        view = glm.lookAt(
            glm.vec3(0, 0, 5),
            glm.vec3(0, 0, 0),
            glm.vec3(0, 1, 0)
        )

        projection = glm.perspective(
        glm.radians(45),
        self.width/self.height,
        0.1,
        1000.0
        )

        glViewport(0, 0, self.width, self.height)

        amatrix = projection * view * model

        glUniformMatrix4fv(
        glGetUniformLocation(self.shader, 'amatrix'),
        1,
        GL_FALSE,
        glm.value_ptr(amatrix)
    )

    def vertex_handling(self):
        vertex_data = numpy.array([
            -1.0, -1.0, 0.0, 1.0, 0.0, 0.0,
            0.0, -1.0, 0.0, 0.0, 1.0, 0.0,
            -0.5, 0.0, 0.0, 0.0, 0.0, 1.0,

            1, -1.0, 0.0, 1.0, 0.0, 0.0,
            0.0, -1.0, 0.0, 0.0, 1.0, 0.0,
            0.5, 0.0, 0.0, 0.0, 0.0, 1.0,

            -0.5, 0.0, 0.0, 1.0, 0.0, 0.0,
            0.5, 0.0, 0.0, 0.0, 1.0, 0.0,
            0.0, 1.0, 0.0, 0.0, 0.0, 1.0
        ], dtype=numpy.float32)

        vertex_buffer_object = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, vertex_buffer_object)
        glBufferData(
            GL_ARRAY_BUFFER,    # Data type
            vertex_data.nbytes, # Data size in bytes    
            vertex_data,        # Data pointers
            GL_STATIC_DRAW
        )
        vertex_array_object = glGenVertexArrays(1)
        glBindVertexArray(vertex_array_object)

        glVertexAttribPointer(
            0,
            3,
            GL_FLOAT,
            GL_FALSE,
            6 * 4,
            ctypes.c_void_p(0)
        )
        glEnableVertexAttribArray(0)

    def render_object(self):
        color1 = random.uniform(0.95 ,0.1)
        color2 = random.uniform(0.95, 0.1)
        color3 = 0.25

        color = glm.vec3(color1, color2, color3)

        glUniform3fv(
            glGetUniformLocation(self.shader,'color'),
            1,
            glm.value_ptr(color)
        )

        self.calculateMatrix()
        glDrawArrays(GL_TRIANGLES, 0, 3)
        glDrawArrays(GL_TRIANGLES, 3, 3)
        glDrawArrays(GL_TRIANGLES, 6, 3)



pygame.init()

screen = pygame.display.set_mode(
    (800, 800),
    pygame.OPENGL | pygame.DOUBLEBUF
)
cube = Obj('./models/cube.obj')

mv = ModelViewer(screen, cube)

glClearColor(0.0, 0.0, 0.0, 1.0)

# running window
running = True
while running:

    glClear(GL_COLOR_BUFFER_BIT)

    mv.render_object()

    pygame.display.flip()

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            mv.angle -= 10

        if keys[pygame.K_d]:
            mv.angle += 10