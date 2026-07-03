def cmd_validate(args):
    """
    Standalone SHACL validation command
    MECE-structured implementation:
    1. Input Resolution
    2. Guard Conditions
    3. Graph Construction
    4. Validation Execution + Output
    """

    from pathlib import Path
    from rdflib import Graph
    from peculiarlibrarian.validation.shacl_validator import SHACLValidator

    #################################################################
    # 1. INPUT RESOLUTION (deterministic paths)
    #################################################################
    dataset_path = Path(args.dataset).expanduser().resolve()
    shapes_path = Path(args.shapes).expanduser().resolve()

    #################################################################
    # 2. GUARD CONDITIONS (fail fast preflight)
    #################################################################
    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    if not shapes_path.exists():
        raise FileNotFoundError(f"Shapes file not found: {shapes_path}")

    #################################################################
    # 3. GRAPH CONSTRUCTION (materialization)
    #################################################################
    graph = Graph()
    graph.parse(str(dataset_path), format=args.format)

    #################################################################
    # 4. VALIDATION EXECUTION + OUTPUT
    #################################################################
    validator = SHACLValidator()

    result = validator.validate(
        graph=graph,
        shapes_path=str(shapes_path)
    )

    print("[VALIDATION RESULT]")
    print(result)
