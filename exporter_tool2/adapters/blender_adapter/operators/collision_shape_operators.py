import bpy

class EXPORTER_OT_create_box_shape(bpy.types.Operator):
    bl_idname = "exporter.create_box_collision_shape"
    bl_label = "Box"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, "Create Box Operator")

        #TODO: Temp only, one object at the time
        obj = context.active_object

        export_package_collection = find_export_package(obj)
        if export_package_collection is None:
            self.report({'ERROR'}, "Export package not found")
            return {"CANCELLED"}

        bpy.ops.mesh.primitive_cube_add()
        cube = context.active_object

        setup_shape(obj, cube)

        for collection in list(cube.users_collection):
            collection.objects.unlink(cube)

        collision_collection = export_package_collection.children.get("Collision")
        collision_collection.objects.link(cube)

        return {"FINISHED"}


class EXPORTER_OT_create_sphere_shape(bpy.types.Operator):
    bl_idname = "exporter.create_sphere_collision_shape"
    bl_label = "Sphere"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        self.report({'INFO'}, "Create Box Operator")

        #TODO: Temp only, one object at the time
        obj = context.active_object

        export_package_collection = find_export_package(obj)
        if export_package_collection is None:
            self.report({'ERROR'}, "Export package not found")
            return {"CANCELLED"}

        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3)
        sphere = context.active_object

        setup_shape(obj, sphere)

        for collection in list(sphere.users_collection):
            collection.objects.unlink(sphere)

        collision_collection = export_package_collection.children.get("Collision")
        collision_collection.objects.link(sphere)

        return {"FINISHED"}


def find_export_package(obj):

    collections = list(obj.users_collection)

    while collections:
        collection = collections.pop()

        if collection.name.startswith("EP_"):
            return collection

        parent = find_parent_collection(collection)

        if parent:
            collections.append(parent)

    return None


def find_parent_collection(child_collection):

    for collection in bpy.data.collections:
        if child_collection.name in collection.children:
            return collection

    return None


def setup_shape(obj, shape):
    shape_name = shape.name
    if shape_name == ("Icosphere"):
        shape_name = "Sphere"

    base_name = f"COL_{shape_name}"
    shape.name = get_unique_name(base_name)
    shape.location = obj.location
    shape.rotation_euler = obj.rotation_euler
    shape.scale = obj.scale
    shape.display_type = 'WIRE'

def get_unique_name(base_name):
    index = 0

    while bpy.data.objects.get(f"{base_name}_{index:02d}") is not None:
        index += 1

    return f"{base_name}_{index:02d}"