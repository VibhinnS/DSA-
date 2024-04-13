def delete(stack :list[int], target :int) -> list[int]:
    if not stack:
        return []
    if len(stack) == 1:
        return []
    
    