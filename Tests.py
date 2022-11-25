from obj import *
import numpy
import time

cube = Obj('./models/cube.obj')

vertex_data = numpy.array([], dtype=numpy.float32)

for face in cube.faces:
    print('cara')

    if (len(face) == 4):
        f1 = face[0][0] - 1
        f2 = face[1][0] - 1
        f3 = face[2][0] - 1
        f4 = face[3][0] - 1

        v1 = [*cube.vertices[f1]]
        v2 = [*cube.vertices[f2]]
        v3 = [*cube.vertices[f3]]
        v4 = [*cube.vertices[f4]]

        print('v1 ', v1)
        print('v2 ', v2)
        print('v3 ', v3)
        print('v4 ', v4)

        vm1 = []
        for x in v1:
            vm1.append(x)
        vm1.append(1.0)
        vm1.append(0.0)
        vm1.append(0.0)

        vm2 = []
        for x in v2:
            vm2.append(x)
        vm2.append(0.0)
        vm2.append(1.0)
        vm2.append(0.0)

        vm3 = []
        for x in v3:
            vm3.append(x)
        vm3.append(0.0)
        vm3.append(0.0)
        vm3.append(1.0)

        vm4 = []
        for x in v3:
            vm4.append(x)
        vm4.append(0.0)
        vm4.append(1.0)
        vm4.append(0.0)

        vm5 = []
        for x in v4:
            vm4.append(x)
        vm5.append(0.0)
        vm5.append(0.0)
        vm5.append(1.0)

        vertex_data = numpy.append(vertex_data, [vm1])
        vertex_data = numpy.append(vertex_data, [vm2])
        vertex_data = numpy.append(vertex_data, [vm3])

        vertex_data = numpy.append(vertex_data, [vm1])
        vertex_data = numpy.append(vertex_data, [vm4])
        vertex_data = numpy.append(vertex_data, [vm5])

        print(vertex_data)

# array = np.array([], dtype=np.float32)
# array = np.append(array, [[4.0, 4.3]])

print(vertex_data)

print(time.perf_counter())