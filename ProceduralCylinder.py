import bpy
import math

def renderMesh(mesh, verts, edges, faces):
    mesh.from_pydata(verts, edges, faces)

def createCylinder(radius: float, height: float, sides: int, layers: int): #TODO: Add support for sides and fix single vertex bug
    # Set up the scene
    mesh = bpy.data.meshes.new("cylinderMesh")  # add the new mesh
    obj = bpy.data.objects.new(mesh.name, mesh)
    col = bpy.data.collections["Collection"]
    col.objects.link(obj)
    bpy.context.view_layer.objects.active = obj
    
    # Create the mesh
    verts = []
    edges = []
    faces = []
    for i in range(0, layers):
        for j in range(0, 360):
            x = radius * math.cos(math.radians(j))
            y = radius * math.sin(math.radians(j))
            z = height * i / (layers - 1)
            verts.append((x, y, z))

            if j > 0:
                edges.append((j + i * 360, j + (i + 1) * 360))
                edges.append((j + (i + 1) * 360, j + i * 360))
            
            if i > 0:
                faces.append(((i * 360) + j, (i * 360) + j + 1, ((i - 1) * 360) + j + 1, ((i - 1) * 360) + j))

    renderMesh(mesh, verts, edges, faces)

    return mesh

createCylinder(1, 14, 10, 5).validate(verbose=True)

print("Done")