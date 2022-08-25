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

    for i in range(0, layers): # "like v"
        for j in range(0, sides): # "like u"
            theta = (j / sides) * 2 * math.pi
            x = radius * math.cos(theta)
            y = radius * math.sin(theta)
            z = height * i / (layers - 1)
            verts.append((x, y, z))

            edges.append((i * sides + j, i * sides + (j + 1) % sides))

            if i > 0:
                edges.append((j + i * sides, j + (i - 1) * sides))
                faces.append((j + i * sides, j + (i - 1) * sides, (j + 1) % sides + (i - 1) * sides, (j + 1) % sides + i * sides))
                
    
    renderMesh(mesh, verts, edges, faces)

    return mesh

createCylinder(1, 14, 5, 5).validate(verbose=True)

print("Done")