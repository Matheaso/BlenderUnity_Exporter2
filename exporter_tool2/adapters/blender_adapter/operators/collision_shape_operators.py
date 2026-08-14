import bpy

from exporter_tool2.core.object_data import ObjectData
from exporter_tool2.core.types import ObjectType
from exporter_tool2.core.result import Result
from exporter_tool2.core.tools.collision import CollisionService, CollisionShape
from exporter_tool2.adapters.blender_adapter.logging.bl_result import handle_result
from exporter_tool2.core.object_data import ExportContext

#TODO: Needs more attention, those conversions are not looking good
class EXPORTER_OT_create_collision_shape(bpy.types.Operator):
    bl_idname = "exporter.create_collision_shape"
    bl_label = "Collision"
    bl_options = {'REGISTER', 'UNDO'}

    shape_type: bpy.props.StringProperty()

    def execute(self, context):
        self.report({'INFO'}, f"Create Collision Operator: {self.shape_type}")

        # TODO: Temp only, one object at the time
        obj = context.active_object
        root_collection = find_export_package(obj)

        if root_collection is None:
            return handle_result(self, Result.error("Export package not found"))

        collision_collection = root_collection.children.get("Collision")

        col_objs = tuple(
            ObjectData(
                asset_name=col_obj.name,
                asset_type=ObjectType(col_obj.type),
                pivot_location=col_obj.location,
                scale=col_obj.scale,
            )
            for col_obj in collision_collection.objects
        )

        export_context = ExportContext(
            tuple(col_objs),
            obj.name
        )
        shape = CollisionShape(self.shape_type)
        col_data = CollisionService.create_collision_shape(shape, export_context)

        if not col_data.success:
            return handle_result(self, col_data)

        if col_data.data.shape == CollisionShape.Cube:
            bpy.ops.mesh.primitive_cube_add()
        elif col_data.data.shape == CollisionShape.Sphere:
            bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3)
        elif col_data.data.shape== CollisionShape.Sphere:
            return handle_result(self, Result.warning("Not implemented"))
        elif col_data.data.shape == CollisionShape.Convex:
            return handle_result(self, Result.warning("Not implemented"))
        else:
            return handle_result(self, Result.error("Collision shape not supported"))

        shape = context.active_object

        setup_shape(obj, shape, col_data.data.collision_name)

        for collection in list(shape.users_collection):
            collection.objects.unlink(shape)

        collision_collection.objects.link(shape)

        return handle_result(self, Result.ok(""))


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


def setup_shape(obj, shape, shape_name):
    shape.name = shape_name
    shape.location = obj.location
    shape.rotation_euler = obj.rotation_euler
    shape.scale = obj.scale
    shape.display_type = 'WIRE'

def get_unique_name(base_name):
    index = 0

    while bpy.data.objects.get(f"{base_name}_{index:02d}") is not None:
        index += 1

    return f"{base_name}_{index:02d}"