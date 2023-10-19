import math

import bpy

bpy.ops.mesh.primitive_cube_add()

# Get reference to the current active object
active_object = bpy.context.active_object

# Scale the cube mesh
active_object.scale.x *= 0.5
active_object.scale.y *= 2
active_object.scale.z *= 0.1

# Apply the scale
bpy.ops.object.transform_apply(scale=True)

# Create variables for stacking rotation
ANGLE_STEP = 3
TOTAL_CUBES = 100
HEIGHT = 0.3
current_angle = ANGLE_STEP
cubes = range(int(360 / ANGLE_STEP))

# Stack and rotate the mesh
for cube in cubes:
    # Duplicate the mesh
    bpy.ops.object.duplicate(linked=True)

    # Get a reference to the current active object
    new_cube = bpy.context.active_object

    # Update the location of the object on the Z axis
    new_cube.location.z += new_cube.dimensions.z

    # Update the rotation
    new_cube.rotation_euler.z = math.radians(current_angle)

    # Update the angle for the next iteration
    current_angle += ANGLE_STEP
