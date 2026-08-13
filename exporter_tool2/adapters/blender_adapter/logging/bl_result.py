from ....core.result import Result

def handle_result(operator, output: Result) -> set[str]:
    operator.report(
        {output.severity.value},
        output.message,
    )

    if output.success:
        return {'FINISHED'}
    else:
        return {'CANCELLED'}

