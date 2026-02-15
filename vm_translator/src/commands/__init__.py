def register_all_VmCmd() -> None:
    # ここで import する（関数内importはこの用途で普通にアリ）
    import commands.arithmetic # pyright: ignore[reportUnusedImport] # noqa: F401
    import commands.function_call # pyright: ignore[reportUnusedImport] # noqa: F401
    import commands.memory_access # pyright: ignore[reportUnusedImport] # noqa: F401
    import commands.program_flow # pyright: ignore[reportUnusedImport] # noqa: F401

