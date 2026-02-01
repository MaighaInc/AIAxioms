def validate_output(output: str, expected_substring: str):
    assert expected_substring in output, (
        f"Validation failed! Expected '{expected_substring}' in '{output}'"
    )
    print("✓ Validation passed")
