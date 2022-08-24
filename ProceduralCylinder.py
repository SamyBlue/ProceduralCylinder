import bpy
import math

def createCylinder(radius, height):
    # Set up the scene
    mesh = bpy.data.meshes.new("myBeautifulMesh")  # add the new mesh
    obj = bpy.data.objects.new(mesh.name, mesh)
    col = bpy.data.collections["Collection"]
    col.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    
    # Create the mesh
    verts = []
    faces = []
    for i in range(0, height):
        for j in range(0, 360):
            x = radius * math.cos(math.radians(j))
            y = radius * math.sin(math.radians(j))
            z = i
            verts.append((x, y, z))
            if i > 0:
                faces.append(((i * 360) + j, (i * 360) + j + 1, ((i - 1) * 360) + j + 1, ((i - 1) * 360) + j))
    mesh.from_pydata(verts, [], faces)

    return mesh

createCylinder(1, 14)