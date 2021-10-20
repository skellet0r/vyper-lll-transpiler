from collections import deque
from copy import deepcopy
from itertools import count

from vyper.old_codegen.lll_node import LLLnode

# global object id generator
_object_id_generator = (f"#yul_object_{i}" for i in count())


class YulObject:
    @staticmethod
    def partition_lll(lll_node: LLLnode) -> tuple[LLLnode, dict[str, LLLnode]]:
        """Partition an LLLnode on the `lll` psuedo-opcode."""
        # create a deepcopy of the `lll_node` to prevent in place modification
        copy_lll_node = deepcopy(lll_node)

        # create the dict container of sub `lll` nodes to be returned
        sub_lll = dict()

        # create deque of tuples where each tuple holds the posiition in the tree and the node
        d = deque([([i], node) for i, node in enumerate(lll_node.args)])

        # loop continuously through the deque until we have exhausted it
        while len(d) > 0:
            # consume an element from the beginning of the deque
            pos, node = d.popleft()
            # if the item is an LLLnode, inspect to see if it's an `lll` node
            if isinstance(node, LLLnode):
                if node.value == "lll":
                    # we've got to name this object and substitute it in the LLLnode
                    identifier = next(_object_id_generator)
                    sub_lll[identifier] = node

                    ref = copy_lll_node
                    for idx in pos:
                        ref = ref.args[idx]

                    # modify the values
                    ref.value = identifier
                    ref.args = []
                    ref.location = "object"
                else:
                    # extend the deque to dig deeper for any `lll` nodes
                    d.extend([([*pos, i], _node) for i, _node in enumerate(node.args)])

        # return the new lllnode and the sub objects
        return (copy_lll_node, sub_lll)
