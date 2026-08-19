import bpy

from exporter_tool2.adapters.blender.blender_adapter import BlenderAdapter
from exporter_tool2.core.asset_data import AssetData
from exporter_tool2.core.types import ObjectType, AssetDomain
from exporter_tool2.core.result import Result
from exporter_tool2.core.modules.collision import CollisionService, CollisionShape
from exporter_tool2.adapters.blender.logging.bl_result import handle_result
from exporter_tool2.core.asset_data import AssetPackage

#TODO: Needs more attention, those conversions are not looking good
class EXPORTER_OT_create_collision_shape(bpy.types.Operator):
    bl_idname = "exporter.create_collision_shape"
    bl_label = "Collision"
    bl_options = {'REGISTER', 'UNDO'}

    shape_type: bpy.props.StringProperty()

    def execute(self, context):
        self.report({'INFO'}, f"Create Collision Operator: {self.shape_type}")

        # TODO: Temp only, one object at the time
        selection = BlenderAdapter.get_selected_object(context.active_object)
        if not selection:
            return handle_result(self, Result.error("No object selected"))

        root_collection = BlenderAdapter.get_export_package_from_selection(selection)

        if not root_collection:
            return handle_result(self, Result.error("Couldn't find root collection"))

        collision_module = root_collection.objects.get(AssetDomain.COLLISION.value)

        col_objs = tuple(
            AssetData(
                name=col_obj.name,
                object_type=ObjectType(col_obj.type),
                components=[]
            )
            for col_obj in collision_module.children
        )

        export_context = AssetPackage(
            tuple(col_objs),
        )
        shape = CollisionShape(self.shape_type)
        col_data = CollisionService.create_collision_shape(shape, export_context)

        if not col_data.success:
            return handle_result(self, col_data)

        if col_data.data.shape == CollisionShape.Cube:
            bpy.ops.mesh.primitive_cube_add()
        elif col_data.data.shape == CollisionShape.Sphere:
            bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=3)
        elif col_data.data.shape== CollisionShape.Capsule:
            return handle_result(self, Result.warning("Not implemented"))
        elif col_data.data.shape == CollisionShape.Convex:
            return handle_result(self, Result.warning("Not implemented"))
        else:
            return handle_result(self, Result.error("Collision shape not supported"))

        shape = context.active_object

        setup_shape(selection, shape, col_data.data.collision_name)

        for collection in list(shape.users_collection):
            collection.objects.unlink(shape)

        root_collection.objects.link(shape)

        module = BlenderAdapter.get_module_from_root(root_collection, AssetDomain.COLLISION)
        if not module:
            return handle_result(self, Result.error(f"Couldn't find module: {AssetDomain.COLLISION.value}"))
        shape.parent = module

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