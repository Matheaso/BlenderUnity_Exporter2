from dataclasses import dataclass
from enum import Enum

from ..asset_data import AssetPackage
from ...core.result import Result


class CollisionShape(Enum):
    Cube = "CUBE"
    Sphere = "SPHERE"
    Capsule = "CAPSULE"
    Convex = "CONVEX"


@dataclass(frozen=True)
class CreateCollisionShape:
    shape: CollisionShape
    collision_name: str


class CollisionService:

    @staticmethod
    def create_collision_shape(
            shape: CollisionShape,

            # active object = name, rest are other colliders
            export_context: AssetPackage,
    ) -> Result[CreateCollisionShape]:

        existing_names = tuple(
            obj.name
            for obj in export_context.objects
        )

        collision_name = create_unique_name(
            f"COL_{shape.name.lower()}",
            existing_names,
        )

        shape_data = CreateCollisionShape(
            shape=shape,
            collision_name=collision_name,
        )

        return Result.ok(shape_data)


def create_unique_name(
        shape_name: str,
        existing_names: tuple[str, ...],
):
    index = 0

    while f"{shape_name}_{index:02d}" in existing_names:
        index += 1

    return f"{shape_name}_{index:02d}"
