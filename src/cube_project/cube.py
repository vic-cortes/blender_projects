import random

import bpy

SPACING = 2.2
NUMBER_CUBES = 10

total_cubes = range(NUMBER_CUBES)

cubes_params = {
    "size": 2,
    "enter_editmode": False,
    "align": "WORLD",
    "scale": (1, 1, 1),
}

# Remove all objects at running script
# bpy.ops.outliner.item_activate(deselect_all=True)
# bpy.ops.mesh.primitive_cube_add(
#     size=2,
#     enter_editmode=False,
#     align="WORLD",
#     location=(19.8, 19.8, 0.865078),
#     scale=(1, 1, 1),
# )
# bpy.ops.object.delete(use_global=True, confirm=False)

# Create materials
# bpy.ops.material.new()
# bpy.data.materials["Material.001"].node_tree.nodes[
#     "Principled BSDF"
# ].subsurface_method = "BURLEY"
# bpy.data.materials["Material.001"].node_tree.nodes["Principled BSDF"].inputs[
#     0
# ].default_value = (0.8, 0.0406915, 0.0515805, 1)


for x in total_cubes:
    for y in total_cubes:
        location = (x * SPACING, y * SPACING, random.random() * SPACING)
        bpy.ops.mesh.primitive_cube_add(**cubes_params, location=location)

        # item = bpy.context.object

        # type_material = "Material.001" if random.random() < 0.5 else "Material"
        # item.data.materials.append(bpy.data.materials[type_material])
