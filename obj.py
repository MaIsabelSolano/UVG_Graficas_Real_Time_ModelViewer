class Obj(object):
    def __init__(self, filename):
        

        self.vertices = []
        self.faces = []
        self.texture_v = []
        self.normal_v = []

        self.read(filename)


    def read(self, filename):

        with open(filename) as f:
            self.lines = f.read().splitlines()

        for line in self.lines:

            try:
                prefix, values, = line.split(' ', 1)
            except:
                prefix = ''

            # vertex
            if (prefix == 'v'):
                self.vertices.append(
                    list(
                        map(
                            float, values.split(' ')
                        )
                    )
                )

            # face
            if (prefix == 'f'):
                self.faces.append([
                    list(map(int, face.split('/'))) for face in values.split(' ')
                ])

            # texture vertex
            if (prefix == 'vt'):
                self.texture_v.append(
                    list(
                        map(
                            float, values.split(' ')
                        )
                    )
                )

            # normals
            if (prefix == 'vn'):
                self.normal_v.append(
                    list(
                        map(
                            float, values.split(' ')
                        )
                    )
                )

