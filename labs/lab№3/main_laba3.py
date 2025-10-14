from pprint import pprint

def gen_bin_tree(height=3, Root=13) -> dict:

    if height <= 1:
        return {"value": Root, "left": None, "right": None}
    
    left_child = gen_bin_tree(height - 1, Root + 1)
    right_child = gen_bin_tree(height - 1, Root - 1)

    return {
        "value": Root,
        "left": left_child,
        "right": right_child
    }

res = gen_bin_tree()


pprint(res)

