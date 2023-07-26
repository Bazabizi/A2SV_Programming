class LockingTree:

    def __init__(self, parent: List[int]):
        self.graph = defaultdict(list)
        for idx, num in enumerate(parent):
            if idx != 0:
                self.graph[num].append(idx)

        self.locked = defaultdict(int)
        self.ancestors = defaultdict(set)

        for idx, val in enumerate(parent):
            current = val
            while current != -1:
                self.ancestors[idx].add(current)
                current = parent[current]

    def lock(self, num: int, user: int) -> bool:
        if num not in self.locked:
            self.locked[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locked and self.locked[num] == user:
            self.locked.pop(num)
            return True
        return False

    def has_locked_descendant(self, node: int) -> bool:
        for child in self.graph[node]:
            if child in self.locked or self.has_locked_descendant(child):
                return True
        return False

    def can_upgrade(self, node: int) -> bool:
        if node in self.locked:
            return False
        for ancestor in self.ancestors[node]:
            if ancestor in self.locked:
                return False
        return self.has_locked_descendant(node)

    def upgrade(self, num: int, user: int) -> bool:
        if self.can_upgrade(num):
            self.locked[num] = user
            for child in self.graph[num]:
                self.unlock_descendants(child)
            return True
        return False

    def unlock_descendants(self, node: int):
        if node in self.locked:
            self.locked.pop(node)
        for child in self.graph[node]:
            self.unlock_descendants(child)

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)