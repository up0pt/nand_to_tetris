def register_all_VmCmd() -> None:
    import commands.arithmetic # pyright: ignore[reportUnusedImport] # noqa: F401
    import commands.function_call # pyright: ignore[reportUnusedImport] # noqa: F401
    import commands.memory_access # pyright: ignore[reportUnusedImport] # noqa: F401
    import commands.program_flow # pyright: ignore[reportUnusedImport] # noqa: F401

